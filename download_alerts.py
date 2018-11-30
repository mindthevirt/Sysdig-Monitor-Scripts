#!/usr/bin/env python
#
# Print 'enabled' flag and name for all of the alerts created by the user
# Optionally dump the full Alerts list as a JSON object to a target file.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
json_dumpfilename = None
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
    sysdig_alert_dir_base = 'sysdig-alert-dir'
    token_dir = 'sysdig_alert_dir_base/'+ sdc_token
    json_dumpfilename = 'alerts_' + sdc_token + '.json'
    #
    # Instantiate the SDC client
    # For on-pmreises, add ssl_verify=False
    #
    sdclient = SdcClient(sdc_token, sdc_url='https://app.sysdigcloud.com')

    #
    # Fire the request.
    #
    res = sdclient.get_alerts()

    #
    # Show the list of alerts
    #
    if res[0]:
        data = res[1]
    else:
        print res[1]
        sys.exit(1)
    print '############################################################'
    print 'Getting alerts for API key %s' %sdc_token
    print '############################################################'
    for alert in data['alerts']:
        print 'enabled: %s, name: %s' % (str(alert['enabled']), alert['name'])

    with open(json_dumpfilename, "w") as f:
        json.dump(data, f, sort_keys=True, indent=4)
