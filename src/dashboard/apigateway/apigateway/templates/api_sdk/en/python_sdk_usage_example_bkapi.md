Create a gateway {{api_name}} client and call the API {{resource_name}} Example of use：

```python
from bkapi.{{api_name_with_underscore}}.client import Client

# Create gateway client
client = Client(
    endpoint="{{ django_settings.BK_API_URL_TMPL }}",
    stage="prod",  # Please set to the actual stage name, otherwise it defaults to prod
)

# Requesting gateway resources, please modify the request according to the specific scenario and the parameters remain compatible with requests
client.api.{{resource_name}}(
    data={...},  # Set request parameters
    path_params={...},  # Setting the route parameters
    params={...},  # Setting up querystring
    headers={...},  # Setting the request header
    timeout=10,  # Set the current request timeout
)
```

The above is only an example, please modify the parameters and the way they are called according to the actual use.

The `endpoint` parameter when creating a gateway can be found in the specific gateway profile for the corresponding access address. If it is not set, it will automatically be probed using the following.

1. reading the `settings.BK_API_URL_TMPL` variable automatically if it is currently a Django project.
2. automatically generated by reading the `BK_API_URL_TMPL` environment variable (which is set by default in the BlueKing Developer Centre).

If `endpoint` is empty, the request will throw an `EndpointNotSetError` exception.

For Django projects, additional helper functions are provided in the `shortcuts` package.

- `get_client_by_request` to quickly generate a client from the `request` object in Django.

```python
from bkapi.{{api_name_with_underscore}}.shortcuts import get_client_by_request

# Automatically get BlueKing app info from django settings (app_code=settings.BK_APP_CODE, app_secret=settings.BK_APP_SECRET)
client = get_client_by_request(
    request, # automatically include user information if request contains user login state
    endpoint="{{ django_settings.BK_API_URL_TMPL }}", # If settings is configured with BK_API_URL_TMPL, it will be applied automatically, otherwise replace it with the actual gateway access address
    stage="prod", # Please set this to the actual stage name, otherwise it defaults to prod
)

# Please modify the request to suit the specific scenario
client.api.{{resource_name}}(...)
```

- `get_client_by_username`, for scenarios such as background tasks where the `request` object cannot be fetched directly, can be called to read the user's last cached login state, but may fail because the cache does not exist or the user state is invalid, etc.

```python
from bkapi.{{api_name_with_underscore}}.shortcuts import get_client_by_username

# Automatically get BlueKing app info from django settings (app_code=settings.BK_APP_CODE, app_secret=settings.BK_APP_SECRET)
client = get_client_by_username(
    username="admin", # username
    endpoint="{{ django_settings.BK_API_URL_TMPL }}", # If settings is configured with BK_API_URL_TMPL, it will be applied automatically, otherwise replace it with the actual gateway access address
    stage="prod", # Please set this to the actual stage name, otherwise it defaults to prod
)

# Please modify the request according to the specific scenario
client.api.{{resource_name}}(...)
```