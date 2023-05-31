import json
import requests
from requests.exceptions import HTTPError
import shortuuid

serverIP = "192.168.0.4"

ae = "lamp_ae"
cnt = "COMMAND"
lbl = "findRoom1"

data = {
    "m2m:cnt": {
        "rn": cnt,
        "lbl": [lbl]
    }
}

if __name__ == "__main__":
    headers = {
        "Accept": "application/json",
        "X-M2M-RI": "req" + shortuuid.ShortUUID().random(length=10),
        "X-M2M-Origin": "/S" + ae,
        "Content-Type": "application/json;ty=3"
    }

    try:
        response = requests.request("post",
                                    "http://" + serverIP + ":7579/Mobius/" + ae + "?rcn=1",
                                    data=json.dumps(data),
                                    headers=headers,
                                    verify=False)

        print(response.text)

    except HTTPError as error:
        print(f"HTTP error occurred: {error}")
    except Exception as error:
        print(f"Other error occurred: {error}")