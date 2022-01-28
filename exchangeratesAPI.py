# shebang
# Dougs quick and unlovely program to get currency conversions
# give me a list of dates, and i'll retreive the usd/aud conversion rates
# give me a list of dates, amounts, source currency, and destination currency, and I'll do a conversion
# http://api.currencylayer.com/
#
#will display to the screen, or save as json text file
#
#
import requests
import getpass
import json
import argparse
from datetime import date
import time

"""This is a short program to hit an api (/api.currencylayer.com) , pull conversions on dates from a csv
    and save the output in json format. the input csv should be a list of dates YYYY-MM-DD.
    The program will need an api key, which can be obtained from api.currencylayer.com ."""

#sample url http://api.currencylayer.com/historical?access_key=blahblahblah&date=2010-04-18&currencies=USD,AUD,CAD,PLN,MXN&format=1c
#
# sample run command python exchangeratesAPI.py -d '2021-07-01' -j 'AUDUSD-2021jul01.json'
# APIKEY=input("paste in the api key here. i won't save it. i promise.")
print("Exchange Rates via 'api.currencylayer.com'")
#lazylazylazy
#APIKEY='blahblahblahblahblah'
#muchmorebetter
APIKEY=getpass.getpass(prompt="paste the api key here (hidden)")
URLBASE='http://api.currencylayer.com/historical'
#
sourcepath='d:/dougsprogs/exchangerates/'
jsonfile=''
csvfile='testdays.csv'
dt_source=date.today()
sourcecurrency='AUD'
destcurrency='USD'
testdate='2020-01-07'
sourcelist = []

jsonlist=[]
inputargs=argparse.ArgumentParser()
inputargs.add_argument('-c', help='conversion request, source-destination, default AUD-USD')
inputargs.add_argument('-d', help='date in  YYYY-MM-DD')
inputargs.add_argument('-l', help='csv file with a list of dates, YYYY-MM-DD')
inputargs.add_argument('-j', help='json file to save output')
#inputargs.add_argument('-csv', help='csv file date,sourceamt,source currency,dest currency')

cliargs = inputargs.parse_args()
currencies = cliargs.c
sourcedate = cliargs.d
sourcelist = cliargs.l 
jsonfile = cliargs.j

if currencies:
    sourcecurrency,destcurrency = currencies.split('-')   

if sourcedate:
    sourcelist = [sourcedate]

elif sourcelist and not sourcedate:
    csvfile = sourcelist

#no need to open a file for a single date
if not sourcedate:
    with open((sourcepath + csvfile), 'r' ) as sourcefile:
        sourcein = sourcefile.read()
        #sourcein is now a string spanning multiple lines
        sourcelist = sourcein.split()

for checkdate in sourcelist:
    #
    url=f'{URLBASE}?access_key={APIKEY}&date={checkdate}&currencies={sourcecurrency},{destcurrency}&format=1c'
    print ("url = ", url)
    convert=requests.get(url)
    jsonlist.append(convert.json())
    time.sleep(1) #pause 1 second
    print (f"json convert is {convert}")
    print(f"json list is {jsonlist}")

if jsonfile:
    print(f"writing json file {jsonfile}")
    with open((sourcepath + jsonfile + '.json'), 'a') as fileout:
        for element in jsonlist:
            json.dump(element,fileout)
            print(element)
    print(f"filename-path will be {sourcepath + jsonfile + '.json'}")
else:
    print("no json filename")    
    for element in jsonlist:
        print(element)
#if __name__ == "__main__":
    #print("startiing from __main__")