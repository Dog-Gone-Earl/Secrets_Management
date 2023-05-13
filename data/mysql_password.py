#!/opt/datadog-agent/embedded/bin/python
#create mysql db
#create user/password

import json
import sys

secrets={"username": {"value": "username_entry", "error": None}, "password": {"value": "Datadog2023", "error": None}}

sys.stdout.write(json.dumps(secrets))

