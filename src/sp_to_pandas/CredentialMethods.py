


def User_Credentials_Method( username, password, siteurl):
    # imports
    from office365.runtime.auth.user_credential import UserCredential
    from office365.sharepoint.client_context import ClientContext

    userctx = username
    passctx = password
    site_url = siteurl

    # Create Connection
    ctx = ClientContext(site_url).with_credentials(
        UserCredential(userctx, passctx))
    web = ctx.web.get().execute_query()

    return ctx,web

def Certificate_Credentials_Method(clientid, thumbprint, siteurl, certificate_path, tenant):
    # Imports
    from office365.sharepoint.client_context import ClientContext

    userctx = clientid
    passctx = thumbprint
    site_url = siteurl
    certificate_path = certificate_path
    tenant = tenant

    cert_settings = {
        'client_id': userctx,
        'thumbprint': passctx,
        'cert_path': certificate_path
    }

    # Create Connection
    ctx = ClientContext(site_url).with_client_certificate(
        tenant, **cert_settings)
    web = ctx.web.get().execute_query()
    return ctx,web


def App_Principle_Method(client_id, client_secret, site_url):
    # Imports
    from office365.sharepoint.client_context import ClientContext
    from office365.runtime.auth.client_credential import ClientCredential

    userctx = client_id
    passctx = client_secret
    site_url = site_url
    client_id = userctx
    client_secret = passctx

    # Create Connection
    creds = ClientCredential(client_id, client_secret)
    ctx = ClientContext(site_url).with_credentials(creds)
    web = ctx.web.get().execute_query()
    return ctx,web

def Certificate_CSV_Method(csv_location):
    # Imports
    from office365.sharepoint.client_context import ClientContext
    import pandas as pd

    Certdf = pd.read_csv(csv_location)

    # credentials
    # print("Enter the client_id for CTX")
    userctx = Certdf['client_id'][0]
    # print("Enter the thumbprint for CTX")
    passctx = Certdf['thumbprint'][0]
    # print("Enter the site_url  for CTX")
    site_url = Certdf['site_url'][0]
    # print("Enter the certificate_path for CTX")
    certificate_path = Certdf['certificate_path'][0]
    # print("Enter the tenant for CTX")
    tenant = Certdf['tenant'][0]
    cert_settings = {
        'client_id': userctx,
        'thumbprint': passctx,
        'cert_path': certificate_path
    }

    # Create Connection
    ctx = ClientContext(site_url).with_client_certificate(
        tenant, **cert_settings)
    web = ctx.web.get().execute_query()
    return ctx,web
