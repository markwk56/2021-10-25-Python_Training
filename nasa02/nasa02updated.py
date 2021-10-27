#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2021-10-01'  ## start date for data
    enddate = '&end_date=2021-10-01' ## create a mechanism to utilize enddate
    mykey = '&api_key=8yXwY6rF7yi4iXitZ02r7t9cBvO2oNElGIYMIrMR' ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey
    neojson = (requests.get(neourl)).json()

    print(neojson)
    print(neojson.keys())

## call main
main()

