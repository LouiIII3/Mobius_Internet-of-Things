
import time
import requests

#post cin
def send_onem2m_data(data):
    url_send = "ip주소:포트번호/Mobius/컨테이너/DATA"
    
    headers_send = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SYbj2CzynVR',
        'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
    }
    
    data = {
        "m2m:cin": {
            "con" : data
        }
    }
    
    r_send = requests.post(url_send, headers = headers_send, json = data)
    
    try:
        r_send.raise_for_status()
        jr_send = r_send.json()
        print(jr_send['m2m:cin']['con'])
    except Exception as exc:
        print('There was a problem: %s' % (exc))

def read_onem2m_data():
    url_read = "ip주소:포트번호/Mobius/컨테이너/DATA/la"
    
    headers_read = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SYbj2CzynVR',
        'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
    }
    
    r_read = requests.get(url_read, headers = headers_read)
    
    try:
        r_read.raise_for_status()
        jr_read = r_read.json()
        
        if(jr_read['m2m:cin']['con'][-1] == "1"):
            print("LED ON")       
        else: 
            print("LED Off")  
    except Exception as exc:
        print('There was a problem: %s' % (exc))



try:
    
    while True:
        read_onem2m_data()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
