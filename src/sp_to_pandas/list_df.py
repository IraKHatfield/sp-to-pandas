
from spToPandas.src.sp_to_pandas.CredentialMethods import *
from spToPandas.src.sp_to_pandas.RequestMethods import *


class list_df:

    # Constructor Defines Connection Type
    def __init__(self, connection_object):
        self.connection_object = connection_object
        if connection_object['connection_type'] == 'user':
            self.User_Credentials(
                connection_object['username'], connection_object['password'], connection_object['siteurl'])
        elif connection_object['connection_type'] == 'certificate':
            self.Certificate_Credentials(connection_object['client_id'], connection_object['thumbprint'],
                                         connection_object['siteurl'], connection_object['certificate_path'], connection_object['tenant'])
        elif connection_object['connection_type'] == 'app':
            self.App_Principle(
                connection_object['client_id'], connection_object['client_secret'], connection_object['site_url'])
        elif connection_object['connection_type'] == 'csv':
            self.Certificate_CSV(connection_object['csv_path'])

    ## Connections ##

    def User_Credentials(self, username, password, siteurl):
        self.ctx, self.web = User_Credentials_Method(
            username, password, siteurl)

    def Certificate_Credentials(self, clientid, thumbprint, siteurl, certificate_path, tenant):
        self.ctx, self.web = Certificate_Credentials_Method(
            clientid, thumbprint, siteurl, certificate_path, tenant)

    def App_Principle(self, client_id, client_secret, site_url):
        self.ctx, self.web = App_Principle_Method(
            client_id, client_secret, site_url)

    def Certificate_CSV(self, csv_location):
        self.ctx, self.web = Certificate_CSV_Method(csv_location)

    def Reconnect(self):
        if self.connection_object['connection_type'] == 'user':
            self.User_Credentials(
                self.connection_object['username'], self.connection_object['password'], self.connection_object['siteurl'])
        elif self.connection_object['connection_type'] == 'certificate':
            self.Certificate_Credentials(self.connection_object['clientid'], self.connection_object['thumbprint'],
                                         self.connection_object['siteurl'], self.connection_object['certificate_path'], self.connection_object['tenant'])
        elif self.connection_object['connection_type'] == 'app':
            self.App_Principle(
                self.connection_object['client_id'], self.connection_object['client_secret'], self.connection_object['site_url'])
        elif self.connection_object['connection_type'] == 'csv':
            self.Certificate_CSV(self.connection_object['csv_path'])

    # Requests

    def PullAListFromSharpoint(self, listInput):
        df = PullAListFromSharpointMethod(self, listInput)
        return df

    def PullAListFromSharpointVersioned(self, listInput):

        df = PullAListFromSharpointVersionedMethod(self, listInput)
        return df

    def PullAListFromSharePointedVersionedThreaded(self, listInput):
        Local_connection_object = self.connection_object
        df = PullAListFromSharePointedVersionedThreadedMethod(
            self, Local_connection_object, listInput)
        return df

    '''
    Place any functions that request data from sharepoint
    '''

    # Transformation
    '''
    Place functions that transform data from raw sharpoint payload into dataframe
    '''

    # Data Sanitization Tools

    '''
    Place any functions that have to do with transforming data types. string to date exct
    Place any functons that have to do with verifying data
    '''

    # Data Filtering and Manipulation Tools

    '''
    place any functions that have to do with filtering
    place any functions that have to do with updating data
    '''
