from spToPandas.src.sp_to_pandas.CredentialMethods import *






def PullAListFromSharpointMethod(self,listInput):
    '''

    Pulls a list off of sharepoint and places it into a data frame

    '''

    import pandas as pd
    import office365

    targetList = self.ctx.web.lists.get_by_title(listInput)
    all_itemsParts = targetList.items.get_all(5000).execute_query()
    PartsUncleanedData=[]
    indexer=-1
    for y in range(0,len(all_itemsParts)):
        indexer=indexer+1
        PartsUncleanedData.append(all_itemsParts[indexer].properties)

    df = pd.DataFrame(data=PartsUncleanedData)
    return df







def PullAListFromSharpointVersionedMethod(self,listInput):
    '''

    Pulls a list off of sharepoint and places it into a data frame

    '''
    import pandas as pd
    import office365

    targetList = self.ctx.web.lists.get_by_title(listInput)
    targetListVersioned = targetList.items.get_all(5000).expand(["Versions"]).execute_query()

    versioned_container = []
    for item in targetListVersioned:
        indexer=-1
        for version in item.properties['Versions']:
            indexer=indexer+1
            versioned_container.append(version.properties)

    versionedDf = pd.DataFrame(data=versioned_container)
    return versionedDf












def PullAListFromSharePointedVersionedThreadedMethod(self,Local_connection_object,tableNamePassed,max_workers=7):
    from itertools import repeat
    from concurrent.futures import ThreadPoolExecutor
    from office365.sharepoint.client_context import ClientContext


    def get_items_range(tableName1, start_index, end_index,Local_connection_object_Passed):

        from pandas import DataFrame
 
        if Local_connection_object_Passed['connection_type'] == 'user':
            ctx,webL = User_Credentials_Method(Local_connection_object_Passed['username'], Local_connection_object_Passed['password'], Local_connection_object_Passed['siteurl'])
        elif Local_connection_object_Passed['connection_type'] == 'certificate':
            ctx,webL = Certificate_Credentials_Method(Local_connection_object_Passed['clientid'], Local_connection_object_Passed['thumbprint'],Local_connection_object_Passed['siteurl'],
                                                       Local_connection_object_Passed['certificate_path'], Local_connection_object_Passed['tenant'])
        elif Local_connection_object_Passed['connection_type'] == 'app':
            ctx,webL = App_Principle_Method(Local_connection_object_Passed['client_id'],Local_connection_object_Passed['client_secret'], Local_connection_object_Passed['site_url'])
        elif Local_connection_object_Passed['connection_type'] == 'csv':
            ctx,webL = Certificate_CSV_Method(Local_connection_object_Passed['csv_path'])

        sp_list2 = ctx.web.lists.get_by_title(tableName1)

        itemsContainer = sp_list2.items.filter(f"ID gt {start_index} and ID lt {end_index}").top(5000).get()

        ctx.load(itemsContainer.expand(["Versions"]))
        ctx.execute_query()

        Returned_items_collection = list(itemsContainer)



        return Returned_items_collection


    import os, certifi

    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
    os.environ["SSL_CERT_FILE"] = certifi.where()
    import pandas as pd

    tableName = tableNamePassed

    max_workers=7

    if Local_connection_object['connection_type'] == 'user':
        ctxtop,webL = User_Credentials_Method(Local_connection_object['username'], Local_connection_object['password'], Local_connection_object['siteurl'])
    elif Local_connection_object['connection_type'] == 'certificate':
        ctxtop,webL = Certificate_Credentials_Method(Local_connection_object['clientid'], Local_connection_object['thumbprint'],Local_connection_object['siteurl'], Local_connection_object['certificate_path'], Local_connection_object['tenant'])
    elif Local_connection_object['connection_type'] == 'app':
        ctxtop,webL = App_Principle_Method(Local_connection_object['client_id'],Local_connection_object['client_secret'], Local_connection_object['site_url'])
    elif Local_connection_object['connection_type'] == 'csv':
        ctxtop,webL = Certificate_CSV_Method(Local_connection_object['csv_path'])

    sp_list = ctxtop.web.lists.get_by_title(tableName)

    batchSizeUsed = 5000


    ctxtop.load(sp_list, ["ItemCount"])
    ctxtop.execute_query()
    print("List length:", sp_list.properties["ItemCount"])
    listLenghtVar = sp_list.properties["ItemCount"]

    offsetter = 0
    i =-1
    batchStarts = []
    batchEnds = []
    for y in range(0,listLenghtVar):

        if(y-offsetter == 0):
            batchStarts.append(y)

        if(y-offsetter >= batchSizeUsed-1):
            batchEnds.append(y+2)
            offsetter = offsetter + batchSizeUsed
    batchEnds.append(y)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        DataFrameHolder = executor.map(get_items_range, repeat(tableName),  batchStarts,  batchEnds,repeat(Local_connection_object))
        ListOfItems = list(DataFrameHolder)

    holdingList = []

    for y in ListOfItems:
        for x in y:
            for z in x.properties['Versions']:
                holdingList.append(z.properties)

    ReturnedDF = pd.DataFrame(data = holdingList)

    return ReturnedDF






