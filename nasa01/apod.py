#!/usr/bin/env python3
import requests

## Define APOD 
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=8yXwY6rF7yi4iXitZ02r7t9cBvO2oNElGIYMIrMR'    ## your key goes in place of DEMO_KEY

## Call the webservice
apodurlobj = requests.get(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.json()

## display our Pythonic data
print("\n\nConverted Python data")
print(apodread)

print(apodread['url'])
print(apodread.keys())
for key in apodread.keys():
    print(key)

