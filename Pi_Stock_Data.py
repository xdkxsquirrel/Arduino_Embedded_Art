import time
import requests
import RPi.GPIO as pi_io

bit_coin_url = "https://blockchain.info/ticker"
KHC = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=KHC&apikey=51SPOTZF3G0EC0QE"
GG = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=GG&apikey=51SPOTZF3G0EC0QE"
TSLA = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey=51SPOTZF3G0EC0QE"

pi_pin = 21
pi_io.setmode(pi_io.BCM)
pi_io.setup(pi_pin, pi_io.OUT) 
pi_io.output(pi_pin, pi_io.LOW)
##########################################################################################
############                        RASPBERRY PI CONTROL               ################### 
def post_arduino_GPIO(status):
    if status :
        pi_io.output(pi_pin, pi_io.HIGH)
    else :
        pi_io.output(pi_pin, pi_io.LOW)


##########################################################################################
############                        MARKET DATA                        ###################    
def get_stock_price(url):
    response = requests.request("GET", url)
    return response.json()

def get_current_bitcoin_price():
    url = bit_coin_url
    response = requests.request("GET", url)
    return response.json()


##########################################################################################
############                        MAIN METHOD                        ################### 
def main():
    last = 0.0
    #stock = get_stock_price(TSLA)
    #print(stock["Global Quote"]["05. price"])
    while True:
        bitcoin_price = get_current_bitcoin_price()
        current = float(bitcoin_price["USD"]["last"])
        if current > last :
            print("1")
            post_arduino_GPIO(1)
        else :
            print("0")
            post_arduino_GPIO(0)
        last = current
        time.sleep(10)

main()
