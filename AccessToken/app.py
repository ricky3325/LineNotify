import requests
from requests.structures import CaseInsensitiveDict
class Connect:
  def __init__(self, code):
    self.url = "https://notify-bot.line.me/oauth/token"
    self.headers = CaseInsensitiveDict()
    self.headers["Accept"] = "application/json"
    self.codeInput = code
    print("Your Code: "+codeInput)
    payload = dict(grant_type='authorization_code', code=codeInput, redirect_uri='http://35.194.229.108:5000/getCode', client_id='OdvneRVOej87cv2iir9tma', client_secret='EPBYbso4W0ygDMP5ivTJWxsjsUqISAXL34UNh6BXT5B')
    resp = requests.post(url, data=payload)
    print(resp.text)
