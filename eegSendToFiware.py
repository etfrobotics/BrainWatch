import requests
import json
from datetime import datetime

class PythonRequest():
    def __init__(self):
        with open('msg_json_BW.json') as f_bw_json:
            self.bw_data = json.loads(f_bw_json.read())  
    def sendToFiware(self,data):
        self.bw_data[0]["status"]["value"] = str(data)
        now = datetime.now()
        self.bw_data[0]["status"]["observedAt"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        requests.post("http://147.91.72.130:1026/ngsi-ld/v1/entityOperations/upsert",json=self.bw_data,headers={"Content-Type":"application/json"})




