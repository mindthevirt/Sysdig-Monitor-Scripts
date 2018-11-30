# Sysdig Monitor scripts

All scripts within this repository require the Sysdig Python client https://github.com/draios/python-sdc-client.

## download_all_dashboards.py
The dashbaords will be stored in ZIP files (dashboards_API-KEY.zip), which are created per API user and stored where the script is being executed from.

Usage:
```python download_all_dashboards.py <sysdig-token/token-json-file>```


## restore_all_dashboards.py
Restore all dashboards of a single user or a group of users.
The ZIP files (dashboards_API-KEY.zip)  need to be in the same folder where the script is being execute from.

Usage:
```python restore_all_dashboards.py <sysdig-token/token-json-file>```


## download_alerts.py
The alerts will be stored in json files (dashboards_API-KEY.json), which are created per API user and stored where the script is being executed from.

Usage:
```python download_alerts.py <sysdig-token/token-json-file>```


## restore_alerts.py
Restore all alerts of a single user or a group of users.
The json files (alerts_API-KEY.json)  need to be in the same folder where the script is being execute from.

Usage:
```python restore_alerts.py <sysdig-token/token-json-file>```


## Formatting of Token Json File

```
{
  "apikeys": [
    "XXXXX-XXXXX-XXXX-XXXXXa",
    "XXXXX-XXXXX-XXXX-XXXXXb",
    "XXXXX-XXXXX-XXXX-XXXXXc"
  ]
}
```
