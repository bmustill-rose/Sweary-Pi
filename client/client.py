import argparse
import json

import simple_websocket

parser = argparse.ArgumentParser()
parser.add_argument("address", help="The IP address of the Pi")
args = parser.parse_args()
try:
 ws = simple_websocket.Client("ws://{}:5000/".format(args.address))
except Exception as e:
  print("Error connecting to {}. {}".format(args.address, e))
  exit()
print("Connected to {}. Type a character or more and press enter or press control + c to quit".format(args.address))
while True:
 for i in input(">"):
  ws.send(json.dumps({"name": i}))
ws.close()