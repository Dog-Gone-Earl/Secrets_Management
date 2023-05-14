#!/opt/datadog-agent/embedded/bin/python
#create mysql db
#create user/password

import json
import sys

secrets={"mysql_username": {"value": "datadog", "error": None}, "mysql_password": {"value": "Datadog2023", "error": None}}

sys.stdout.write(json.dumps(secrets))

