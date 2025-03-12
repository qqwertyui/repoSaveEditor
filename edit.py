#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

import pbkdf2
import argparse
import json

secret = "Why would you want to cheat?... :o It's no fun. :') :'D"
blockLength = 16
iterations = 100

def decrypt(data, password, iv):
  key = pbkdf2.PBKDF2(password, iv, iterations).read(blockLength)
  cipher = AES.new(key, AES.MODE_CBC)
  return unpad(cipher.decrypt(data), blockLength)

def encrypt(data, password):
  iv = get_random_bytes(blockLength)
  key = pbkdf2.PBKDF2(password, iv, iterations).read(blockLength)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  return iv + cipher.encrypt(pad(data, blockLength))

def loadMap(filename):
  with open(filename, "rb") as f:
    d = f.read()

  iv = d[:blockLength]
  data = decrypt(d, secret, iv)[blockLength:]
  return json.loads(data)

def saveMap(filename, data):
  data = json.dumps(data).encode()
  
  with open(filename, "wb") as f:
    f.write(encrypt(data, secret))

def parseArgs():
  parser = argparse.ArgumentParser(prog="R.E.P.O save editor")
  parser.add_argument("input")
  parser.add_argument("-o", "--output")
  parser.add_argument("-v", "--verbose", action="store_true")
  parser.add_argument("-s", "--statement")

  return parser.parse_args()

def main():
  args = parseArgs()
  data = loadMap(args.input)

  if(args.statement):
    exec(args.statement)

  if(args.verbose):
    print(json.dumps(data, indent=4))

  if(args.output):
    saveMap(args.output, data)

if __name__ == "__main__":
  main()
