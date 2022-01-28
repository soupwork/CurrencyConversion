# CurrencyConversion
connect to an API to do currency conversions, save as json text or screen output


exchangeratesAPI.py -h        
Exchange Rates via 'api.currencylayer.com'
usage: exchangeratesAPI.py [-h] [-c C] [-d D] [-l L] [-j J]

This is a short program to hit an api (/api.currencylayer.com) , pull conversions on dates from a csv and  
save the output in json format.

options:
  -h, --help  show this help message and exit
  -c C        conversion request, source-destination, default AUD-USD
  -d D        date in YYYY-MM-DD , for a single day conversion
  -l L        csv file for input with a list of dates, YYYY-MM-DD
  -j J        json file to save output
  -p P        path for both the input and output files

the input csv should be a list of dates YYYY-MM-DD. The program will need an api key, which can be
obtained from api.currencylayer.com .

running the program with no options will retrieve USD-AUD conversion for today, and output to the screen
sample run command 
  python exchangeratesAPI.py -d '2021-07-01' -j 'AUDUSD-2021jul01'
