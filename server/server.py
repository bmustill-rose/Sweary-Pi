import json

from flask import Flask, render_template, request
import simple_websocket

import sounds
from audioLookup import audioLookup

def handleMessage(message):
 try:
  key = json.loads(message)['name']
  print("Received \"{}\"".format(key))
  sounds.playSound(audioLookup[key])
 except Exception as e:
  #print("Invalid message, received character that hasn't been mapped or other error during playback")
  print(e)
  pass

app = Flask(__name__)

@app.route("/", websocket=True)
def sweary():
 ws = simple_websocket.Server(request.environ)
 try:
  while True:
   message = ws.receive()
   handleMessage(message)
 except simple_websocket.ConnectionClosed:
  pass
 return ''

app.run(host='0.0.0.0')