from flask import Flask
from flask import request
import webbrowser
from flask import redirect
import requests
import time
app = Flask(__name__)
client_id=56916
secret='a72efb336085286ec673c4b3c73b0517c18a1ba3'
@app.route("/")
def home():
    code = request.args.get('code')
    print(code)

    # # #post request
    # # clientData = {'client_id':client_id,'client_secret':secret,'code':code,'grant_type':'authorization_code'}
    # # accessUrl = 'https://www.strava.com/oauth/token'
    access_token=UseCode(code)
    
    # url='https://www.strava.com/api/v3/oauth/token?client_id=56916&client_secret=a72efb336085286ec673c4b3c73b0517c18a1ba3&code=a39a4dd1f047e74be086becfbfe7dea0b723c67c&grant_type=authorization_code' % code
    # print(url)
    # res=requests.post(url)
    # print(res.text)
    
    # accessTokenRequest = requests.post(accessUrl,data=clientData).json()["access_token"]
    # print("access token is "+accessTokenRequest)
    

    return redirect("https://mitaapi.heroku.com/extractData?code="+access_token,302)

# @app.route("/callback")
# def callback():
#     return "whatever!"
    
@app.route("/extractData")
def home2():
  return "redirecting"
def UseCode(code):
 

  #Retrieve the login code from the Strava server
  print("client " , client_id)
  print("client_secret " , secret)
  print("code " , code)
  #access_token = client.exchange_code_for_token(client_id=client_id,client_secret=secret, code=code)

  # this is for getting access_token
  clientData = {'client_id':client_id,'client_secret':secret,'code':code,'grant_type':'authorization_code'}
  accessUrl = 'https://www.strava.com/oauth/token'
  try:
    print("hey")
    atr=requests.post(accessUrl,data=clientData,verify=True).json()
    access_token=atr['access_token']
    print("access_token  ",access_token)
    return access_token
    
    
  except Exception as e:
      print("failed")
      print(e) 
      return -1 
#   accessTokenRequest = requests.post(accessUrl,data=clientData).json()
#   print(accessTokenRequest['access_token'])

#   print("access token granted " , accessTokenRequest)

#   access_token = accessTokenRequest
#   #athlete = client.get_athlete()
#   tokenHeader = {'authorization': 'Bearer ' + access_token}
# #   #url = 'https://www.strava.com/api/v3/athlete/36664707'
# #   #url = 'https://www.strava.com/api/v3/athlete/3662584/stats'



#   url = 'https://www.strava.com/api/v3/athlete'
#   r = requests.get(url, headers=tokenHeader)
#   print(" response json ",r.json())
#   athlete = r.json()
#   print("athlete username ",athlete["username"])
 
 
#   #print(("For %(id)s, I now have an access token %(token)s" %
  #   {'id': athlete.id, 'token': access_token}))

    
if __name__ == "__main__":
    print("Afs")
    app.run(debug=True)