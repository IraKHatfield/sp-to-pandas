

class list_df:

    # Constructor

    def __init__(self, connection_object):

        if connection_object.connection_type == "user":
            self.User_Credentials(
                connection_object.username, connection_object.password, connection_object.siteurl)

    def User_Credentials(self, username, password, siteurl):
        # imports
        from office365.runtime.auth.user_credential import UserCredential
        from office365.sharepoint.client_context import ClientContext

        self.userctx = username
        self.passctx = password
        self.site_url = siteurl

        # Create Connection
        self.ctx = ClientContext(self.site_url).with_credentials(
            UserCredential(self.userctx, self.passctx))
        self.web = self.ctx.web.get().execute_query()

    def Certificate_Credentials(self, clientid, thumbprint, siteurl, certificate_path, tenant):
        # Imports
        from office365.sharepoint.client_context import ClientContext

        self.userctx = clientid
        self.passctx = thumbprint
        self.site_url = siteurl
        self.certificate_path = certificate_path
        self.tenant = tenant

        self.cert_settings = {
            'client_id': self.userctx,
            'thumbprint': self.passctx,
            'cert_path': self.certificate_path
        }

        # Create Connection
        self.ctx = ClientContext(self.site_url).with_client_certificate(
            self.tenant, **self.cert_settings)
        self.web = self.ctx.web.get().execute_query()

    def App_Principle(self, client_id, client_secret, site_url):
        # Imports
        from office365.sharepoint.client_context import ClientContext
        from office365.runtime.auth.client_credential import ClientCredential

        self.userctx = client_id
        self.passctx = client_secret
        self.site_url = site_url
        self.client_id = self.userctx
        self.client_secret = self.passctx

        # Create Connection
        self.creds = ClientCredential(self.client_id, self.client_secret)
        self.ctx = ClientContext(site_url).with_credentials(self.creds)
        self.web = self.ctx.web.get().execute_query()

    def Certificate_CSV(self, csv_location):
        # Imports
        from office365.sharepoint.client_context import ClientContext
        import pandas as pd

        Certdf = pd.read_csv(csv_location)

        # credentials
        # print("Enter the client_id for CTX")
        self.userctx = Certdf['client_id'][0]
        # print("Enter the thumbprint for CTX")
        self.passctx = Certdf['thumbprint'][0]
        # print("Enter the site_url  for CTX")
        self.site_url = Certdf['site_url'][0]
        # print("Enter the certificate_path for CTX")
        self.certificate_path = Certdf['certificate_path'][0]
        # print("Enter the tenant for CTX")
        self.tenant = Certdf['tenant'][0]
        self.cert_settings = {
            'client_id': self.userctx,
            'thumbprint': self.passctx,
            'cert_path': self.certificate_path
        }

        # Create Connection
        self.ctx = ClientContext(self.site_url).with_client_certificate(
            self.tenant, **self.cert_settings)
        self.web = self.ctx.web.get().execute_query()
