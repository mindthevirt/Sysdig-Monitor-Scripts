# Sysdig Monitor scripts

All scripts within this repository require the Sysdig Python client https://github.com/draios/python-sdc-client.

## download_all_dashboards.py
Download all dashboards of a single user or a group of users

Usage:
```python download_all_dashboards.py <sysdig-token/token-json-file>```


## restore_all_dashboards.py
Restore all dashboards of a single user or a group of users

Usage:
```python restore_all_dashboards.py <sysdig-token/token-json-file>```



## Formatting of Token Json File

```
{
  "apikeys": [
    "XXXXX-XXXXX-XXXX-XXXXXa",
    "XXXXX-XXXXX-XXXX-XXXXXc"
  ]
}
```
