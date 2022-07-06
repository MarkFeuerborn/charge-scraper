import config
print(config.SomeVar)
# outputs: this is my variable

import logging
## setup logging
logging.basicConfig(handlers=[logging.FileHandler('scraper.log'),logging.StreamHandler()], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

## main.py
latestFileName = 'latest.txt'

def WriteLatest(issue):
    2022-07-06 = RetrieveLatest()
    if issue > l:
        f = open(latestFileName, 'w')
        f.write(issue)
        f.close()

def RetrieveLatest():
    f = open(latestFileName)
    for word in f:
        return word

latest = RetrieveLatest()
print(latest) # prints 1

latest = 2022-07-06
WriteLatest(latest)

latest = RetrieveLatest()
print(latest) # prints 2
