import requests
import json
import uuid

cs_dev_uri = "https://dev1.mbv3.hdfcbank.com/"
cs_uri = cs_dev_uri

def func_deregister(customerid):

    url = cs_uri + "user-status-service/user/tpt/deregister"

    payload = json.dumps({
    "request_id": "" + str(uuid.uuid4()) + "",
    "channel_id": "B11",
    "platform": "NBMB",
    "login_id": "" + customerid + "",
    "channel": "NB",
    "identifier": "CUSTOMER_ID",
    "maker_id": "string",
    "checker_id": "string",
    "maker_date": 0,
    "checker_date": 0,
    "mod_process": "string"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    print("REQUEST TO USER STATUS - DEREGISTER")
    print(payload)

    response = requests.request("POST", url, headers=headers, data=payload)
    print("RESPONSE FROM  USER STATUS - DEREGISTER")

    print(response.text)

def func_register(customerid):

    url =  cs_uri + "user-status-service/user/tpt/register"

    payload = json.dumps({
    "request_id": "" + str(uuid.uuid4()) + "",
    "channel_id": "B11",
    "platform": "NBMB",
    "customer_id": "" + customerid + "",
    "channel": "NB",
    "identifier": "CUSTOMER_ID",
    "customer_type": "DEFAULT",
    "tpt_limit": 2000,
    "authentication_type": "otp",
    "tpt_registration_time": 1686724980363
    })
    headers = {
    'Content-Type': 'application/json'
    }

    print("REQUEST TO USER STATUS - REGISTER")
    print(payload)

    response = requests.request("POST", url, headers=headers, data=payload)
    print("RESPONSE FROM  USER STATUS - REGISTER")

    print(response.text)

#### Enabling TPT customer wise
def func_enable(customerid):
    url = url = cs_uri + "bene-limits-service/user/limits/tpt/status/set"

    payload = json.dumps({
    "request_id": "" + str(uuid.uuid4()) + "",
    "customer_id": "" + customerid + "",
    "channel_id": "B11",
    "status": "ACTIVE"
    })
        
    headers = {
    'Content-Type': 'application/json'
    }

    print("REQUEST TO USER STATUS - ENABLE")
    print(payload)

    response = requests.request("PUT", url, headers=headers, data=payload)
    print("RESPONSE FROM  USER STATUS - ENABLE")
    print(response.text)

#### Setting TPT limit customer wise
def func_setLimit(customerid):
    url = url = cs_uri + "bene-limits-service/user/limits/tpt/limit/set"

    newLimt = 300000

    payload = json.dumps({
    "request_id": "" + str(uuid.uuid4()) + "",
    "customer_id": "" + customerid + "",
    "channel_id": "B11",
    "limit": newLimt
    })
        
    headers = {
    'Content-Type': 'application/json'
    }

    print("REQUEST TO USER TPT - LIMIT")
    print(payload)

    response = requests.request("PUT", url, headers=headers, data=payload)
    print("RESPONSE FROM USER TPT - LIMIT")
    print(response.text)

 

def func_doRegistration():
    # customerids = ["900478627","50040360","900478710","192598029","50196490","154342940","900478666","900478664","900478678","50003560","77707717","50179623","900477852","50000044","5264528","900478708","900478707","900478704","2727395","192598029","900478667","900478662","900478674","900478622","900478653","900478657","900478660","900478643","900478694","77707717","900478714 ","900485936","900485936","900478694","900478665","900478660","50191357","900478696","900485936","900478694","900478699","2799408","900478659","900478614","900488631 ","900488629","444928444","900485918","900478696","900478699","900478669","900478670","900478672","900478667","900478660","900478712","900478720","50233130","50199500","900478675","192598029","900478663","900478674","900478644","900478662","900478653","900478654","900478666","77707717","900478630","900478670"]
    customerids = ["50236368"]
    print("Process start")
    cs_uri = cs_dev_uri
    print("cs_uri : ", cs_uri)
    for customerid in customerids:
        print(customerid)
        func_deregister(customerid)
        print("")
        func_register(customerid)
        print("")
        func_enable(customerid)
        print("")
        func_setLimit(customerid)
        print("")
    print("Process end")

func_doRegistration()
