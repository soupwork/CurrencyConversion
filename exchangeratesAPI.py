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

def callAPI(sourcelist, sourcecurrency, destcurrency):
    #sourcelist is a list of dates in text format
    jsonlist = [] #init json list
    #lazylazylazy
    #APIKEY='testtesttesttestblahblahblah'
    #muchmorebetter
    APIKEY=getpass.getpass(prompt="paste the api key here (hidden)")
    URLBASE='http://api.currencylayer.com/historical'
    for date in sourcelist:
        #
        url=f'{URLBASE}?access_key={APIKEY}&date={date}&currencies={sourcecurrency},{destcurrency}&format=1c'
        convert=requests.get(url)
        jsonlist.append(convert.json())
        time.sleep(1) #pause 1 second

    return(jsonlist)
    #end callAPI


# sample run command python exchangeratesAPI.py -d '2021-07-01' -j 'AUDUSD-2021jul01'

print("Exchange Rates via 'api.currencylayer.com'")
#
sourcepath='d:/dougsprogs/exchangerates/'
jsonfile=''
csvfile=''
today = date.today()
sourcecurrency=''
destcurrency=''
sourcelist = []
jsonlist=[]

inputargs=argparse.ArgumentParser(description='This is a short program to hit an api \
    (/api.currencylayer.com) , pull conversions on dates from a csv \
    and save the output in json format. ',
    epilog='the input csv should be a list of dates YYYY-MM-DD.\
    The program will need an api key, which can be obtained from api.currencylayer.com .')

inputargs.add_argument('-c', help='conversion request, source-destination, default AUD-USD')
inputargs.add_argument('-d', help='date in  YYYY-MM-DD , for a single day conversion')
inputargs.add_argument('-l', help='csv file for input with a list of dates, YYYY-MM-DD')
inputargs.add_argument('-j', help='json file to save output')
inputargs.add_argument('-p', help='file path for both input and output files')

cliargs = inputargs.parse_args()
currencies = cliargs.c
sourcedate = cliargs.d
sourcelist = cliargs.l 

if cliargs.p:
    sourcepath = cliargs.p
if cliargs.j:
    jsonfile = cliargs.j

if currencies:
    sourcecurrency,destcurrency = currencies.split('-')  
else:
    sourcecurrency = 'AUD' 
    destcurrency = 'USD'   

# a csv file provided on command line
if not sourcedate and sourcelist:
    with open((sourcepath + sourcelist), 'r' ) as sourcefile:
        sourcein = sourcefile.read()
        #sourcein is now a string spanning multiple lines
        #repurpose sourcelist to be the list of dates
        sourcelist = sourcein.split()

elif sourcedate:
    #create a one-element list
    sourcelist = [str(sourcedate)]

else: #no csv or date provided
    sourcelist=[str(today)]    
    print("no csv or date provided")
    print(f"source list is {sourcelist}")
    print(f"source list type is {type(sourcelist)}")

#Call the API
jsonlist = callAPI(sourcelist, sourcecurrency, destcurrency)

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