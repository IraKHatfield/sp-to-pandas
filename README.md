# UNDER CONSTRUCTION

# sp-to-pandas

Pull Sharepoint lists directly into pandas DataFrames

# About

This is a thin wrapper around pandas and office365-rest-python-client that allows users to pull tabular data from sharepoint lists and document libraries directly into pandas dataframes without much effort.

# Usage

# Installation

# Authentication

## Connection Object

This object is designed to handle all forms of sharepoint authentication currently supported.

Example:

```json
connection_object = {
    'connection_type':"user"
    'username':"TestUser@Mail.com",
    'password':"Password",
    'siteurl':"https://tenant.sharepoint.com/sitename/",
    'tenant':"tenant"
    'client_id':"Id",
    'thumbprint':"thumbprint",
    'client secret':"secret"
    'certificate_path':"Path to My Certificate",
    'csv_path':"Path To CSV"

}
```

### Connection Type

#### Options Are As Follows:

User Credential Auth:'user'
Certificate Credential:'certificate'
App Principle Auth:'app'
Certificate CSV:'csv'

NOTE: Not all of these values will be used for a given authentication method. Below is a short list of what you need for each supported method

## User Credential Auth

```json
connection_object = {
    'username':"TestUser@Mail.com",
    'password':"Password",
    'siteurl':"https://tenant.sharepoint.com/sitename/"
}
```

NOTE: 2 factor auth will fail here. if the account you are using has 2 factor auth, please use another method

NOTE: This method has been depreciated by microsoft: https://learn.microsoft.com/en-us/entra/msal/python/advanced/username-password-authentication

## Certificate Credential Auth

```json
connection_object = {
    'siteurl':"https://tenant.sharepoint.com/sitename/",
    'tenant':"tenant"
    'client_id':"Id",
    'thumbprint':"thumbprint",
    'certificate_path':"Path to My Certificate",
}
```

NOTE: More information on creating creating certificate ect here: https://learn.microsoft.com/en-us/entra/identity-platform/msal-authentication-flows#certificates

## App Principle Auth

```json
connection_object = {
    'siteurl':"https://tenant.sharepoint.com/sitename/",
    'client_id':"Id",
    'client secret':"secret"

}
```

NOTE: More information on creating client id and secret here: https://learn.microsoft.com/en-us/entra/identity-platform/msal-authentication-flows#client-credentials

## Certificate CSV

```json
connection_object = {
    'csv_path':"Path To CSV"

}
```

### CSV Formate Requirments

UNDER CONSTRUCTION
