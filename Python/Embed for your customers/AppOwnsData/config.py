# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = 'cea6d89a-3938-45e5-be31-0593f0738e42'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '2f3396ad-8f31-444c-b74a-57b9a7461e5a'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '4ee04ec2-6076-420e-913e-0fd0134143d8'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'cd68aa09-0c73-4103-a097-abcb8ecf23b6'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'sTQ8Q~9Y.H-h3ZSqIjzyWhkeRjQnQngomfhXQaK5'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'avtar.sahani@ipsgroup.co.in'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'Shahani@55'


# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig2(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = 'cea6d89a-3938-45e5-be31-0593f0738e42'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '4bd89b19-4e0e-47ba-a68e-c840cb221ebe'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '4ee04ec2-6076-420e-913e-0fd0134143d8'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'cd68aa09-0c73-4103-a097-abcb8ecf23b6'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'sTQ8Q~9Y.H-h3ZSqIjzyWhkeRjQnQngomfhXQaK5'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'avtar.sahani@ipsgroup.co.in'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'Shahani@55'    