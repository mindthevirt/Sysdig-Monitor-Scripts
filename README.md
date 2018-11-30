# Sysdig Monitor scripts

All scripts within this repository require the Sysdig Python client https://github.com/draios/python-sdc-client.

## download_all_dashboards.py
Download all dashboards of a single user or a group of users.
<<<<<<< HEAD
The dashbaords will be stored in ZIP files (dashboards_<API-KEY>.zip), which are created per API user and stored where the script is being executed from.
=======
The dashboards will be stored in ZIP files, which are created per API user and stored where the script is being executed from.
>>>>>>> 5277069b7f3b281137b66f73c6fdf94851cc3ca7

Usage:
```python download_all_dashboards.py <sysdig-token/token-json-file>```


## restore_all_dashboards.py
Restore all dashboards of a single user or a group of users.
<<<<<<< HEAD
The ZIP files (dashboards_<API-KEY>.zip)  need to be in the same folder where the script is being execute from.
=======
The ZIP files need to be in the same folder where the script is being executed from.
>>>>>>> 5277069b7f3b281137b66f73c6fdf94851cc3ca7

Usage:
```python restore_all_dashboards.py <sysdig-token/token-json-file>```



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
