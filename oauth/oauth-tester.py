#%% [markdown]
### Setup 
# The script looks up values from an oauth-test.json file in the root directory along with this script.
#```json
# {
#    "auth_domain": "https://auth.domain",
#    "client_id": "client_id",
#    "client_secret": "client_secret"
# }
# ```

#%%
import os
jsonPath =  os.path.join(os.getcwd(), "oauth", "oauth-test.json")
print(jsonPath)
#%%
import json
data = {}
data['auth_domain']="auth.domain"
data['client_id']="client_id"
data['client_secret']="client_secret"

if not os.path.exists(jsonPath):
  with open(jsonPath, 'w') as outfile:
    json.dump(data, outfile)

#%%
# load oauth data
with open(jsonPath, mode='rb') as json_file:
    oauthData = json.loads(json_file.read())

#%%
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

#%%
auth_domain = oauthData["auth_domain"]
client_id = oauthData["client_id"]
client_secret = oauthData["client_secret"]
token_url = auth_domain + "/oauth/token"

# If your provider requires that you pass auth credentials in a Basic Auth header, you can do this instead:
# client = Client(client_id=client_id)
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url,
                          client_id=client_id,
                          client_secret=client_secret)

print(token)
# %%
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth(client_id, client_secret)
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, auth=auth)
json.dumps(token, indent=2)
#%%
