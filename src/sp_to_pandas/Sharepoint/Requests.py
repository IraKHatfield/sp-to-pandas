
'''
 Pulls a list off of sharepoint and places it into a data frame
'''


def PullAListFromSharpoint(self, listInput):

    import pandas as pd
    import numpy as np
    import office365
    import pyodbc
    from office365.runtime.auth.user_credential import UserCredential
    from office365.sharepoint.client_context import ClientContext
    import os
    import sys
    import regex as re

    targetList = self.ctx.web.lists.get_by_title(listInput)
    all_itemsParts = targetList.items.get_all(5000).execute_query()
     PartsUncleanedData = []
      indexer = -1
       for y in range(0, len(all_itemsParts)):
            indexer = indexer+1
            PartsUncleanedData.append(all_itemsParts[indexer].properties)

        df = pd.DataFrame(data=PartsUncleanedData)
        return df
