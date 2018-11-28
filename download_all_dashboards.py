#!/usr/bin/env python
#
# Save/restore dashboards


import os
import sys
import zipfile
import json
import shutil
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        # print root
        for file in files:
            ziph.write(os.path.join(root, file))

def cleanup_dir(path):
    if os.path.exists(path) == False:
        return
    if os.path.isdir(path) == False:
        print 'Provided path is not a directory'
        sys.exit(-1)
    shutil.rmtree(path)

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token/token-json-file>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)



sdc_token = sys.argv[1]
sdc_tokens = []
if not '.json' in sdc_token:
    sdc_tokens.append(sdc_token)
else:
    with open(sdc_token) as f:
        data = json.load(f)
        for apikey in data['apikeys']:
            sdc_tokens.append(apikey)

for sdc_token in sdc_tokens:
    sysdig_dashboard_dir_base = 'sysdig-dashboard-dir'
    token_dir = 'sysdig-dashboard-dir/'+ sdc_token
    #
    # Instantiate the SDC client
    # For on-pmreises, add ssl_verify=False
    #
    sdclient = SdcClient(sdc_token, sdc_url='https://app.sysdigcloud.com')

    #
    # Fire the request.
    #
    res = sdclient.get_dashboards()

    #
    # Show the list of dashboards
    #
    if res[0]:
        data = res[1]
    else:
        print res[1]
        sys.exit(1)

    # Creating sysdig dashboard directory to store dashboards
    if not os.path.exists(sysdig_dashboard_dir_base):
        os.makedirs(sysdig_dashboard_dir_base)
    if not os.path.exists(token_dir):
        os.makedirs(token_dir)


    for db in data['dashboards']:
        file_path = os.path.join(token_dir, str(db['id']))
        f = open(file_path, 'w')
        f.write(json.dumps(db))
        print "Name: %s, # Charts: %d" % (db['name'], len(db['items']))
        f.close()

    zipf = zipfile.ZipFile(sdc_token, 'w', zipfile.ZIP_DEFLATED)
    zipdir(token_dir, zipf)
    zipf.close()

# Clean up any state in the directory
cleanup_dir(sysdig_dashboard_dir_base)
