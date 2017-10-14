import urllib2
import json
import time
import os
import winsound
import math
import time
import atexit
import thread
import gdax


AlertEtherHF = float(raw_input("What is your Ether High Price Alert Target? "))
AlertEtherLF = float(raw_input("What is your Ether Low Price Alert Target? "))
counter = 0
os.system('cls' if os.name == 'nt' else "printf '\033c'")
public_client = gdax.PublicClient()

OMGHold = float(25)
ZRXHold = float(2500)

while True:
    counter+=1
    

    def btc():   
        try:
            BTCGDAX = public_client.get_product_ticker(product_id='BTC-USD')
            BTCPrice =BTCGDAX['bid']
            return float(BTCPrice)
        except:
            pass
    thread.start_new_thread(btc, ())
    
    def eth():   
        try:
            ETHGDAX = public_client.get_product_ticker(product_id='ETH-USD')
            ETHPrice =ETHGDAX['bid']
            return float(ETHPrice)
        except:
            pass
    thread.start_new_thread(eth, ())

    def neo():   
        try:
            response_neo = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/neo/")
            data_neo = json.load(response_neo)
            NEOPrice = float( data_neo[0]['price_usd'])
            return NEOPrice
        except:
            pass
    thread.start_new_thread(neo, ())

    def neoPR1():   
        try:
            response_neo = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/neo/")
            data_neo = json.load(response_neo)
            NEOPR1 = float( data_neo[0]['percent_change_1h'])
            return NEOPR1
        except:
            pass
    thread.start_new_thread(neoPR1, ())

    def neoPR24():   
        try:
            response_neo = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/neo/")
            data_neo = json.load(response_neo)
            NEOPR24 = float( data_neo[0]['percent_change_24h'])
            return NEOPR24
        except:
            pass
    thread.start_new_thread(neoPR24, ())
    

    def omg():   
        try:
            response_omg = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/omisego/")
            data_omg = json.load(response_omg)
            OMGPrice = float( data_omg[0]['price_usd'])
            return OMGPrice
        except:
            pass
    thread.start_new_thread(omg, ())

    def omgPR1():   
        try:
            response_omg = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/omisego/")
            data_omg = json.load(response_omg)
            OMGPricePR1 = float( data_omg[0]['percent_change_1h'])
            return OMGPricePR1
        except:
            pass
    thread.start_new_thread(omgPR1, ())

    def omgPR24():   
        try:
            response_omg = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/omisego/")
            data_omg = json.load(response_omg)
            OMGPricePR24 = float( data_omg[0]['percent_change_24h'])
            return OMGPricePR24
        except:
            pass
    thread.start_new_thread(omgPR24, ())
    
    def zrx():   
        try:
            response_zrx = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/0x/")
            data_zrx = json.load(response_zrx)
            ZRXPrice = float( data_zrx[0]['price_usd'])
            return ZRXPrice
        except:
            pass
    thread.start_new_thread(zrx, ())

    def zrxPR1():   
        try:
            response_zrx = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/0x/")
            data_zrx = json.load(response_zrx)
            ZRXPricePR1 = float( data_zrx[0]['percent_change_1h'])
            return ZRXPricePR1
        except:
            pass
    thread.start_new_thread(zrxPR1, ())

    def zrxPR24():   
        try:
            response_zrx = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/0x/")
            data_zrx = json.load(response_zrx)
            ZRXPricePR24 = float( data_zrx[0]['percent_change_24h'])
            return ZRXPricePR24
        except:
            pass
    thread.start_new_thread(zrxPR24, ())

    def stx():   
        try:
            response_stx = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/stox/")
            data_stx = json.load(response_stx)
            STXPrice = float( data_stx[0]['price_usd'])
            return STXPrice
        except:
            pass
    thread.start_new_thread(stx, ())


    

    def calcTH():
        
        OMGHold = float(25)
        ZRXHold = float(2500)
        OMGTotal = OMGHold*omg()
        ZRXTotal = ZRXHold*zrx()
        TotalHold = float(round(( OMGTotal+ZRXTotal),2))
        PercentChangeTotal = round(( ((TotalHold-500)/500)*100),2)
        return TotalHold
        
        
    thread.start_new_thread(calcTH, ())

    def calcPH():
        ProfitHold = float(calcTH()-317)
        return ProfitHold
    thread.start_new_thread(calcPH, ())

    def calcPCT():
        PercentChangeTotal = round(( ((calcTH()-317)/317)*100),2)
        return PercentChangeTotal
    thread.start_new_thread(calcPCT, ())

    def alert_fnc(threadname,delay):
        global AlertEtherHF
        global AlertEtherLF
        ETHPriceFNX = eth()
        
        ETHPRH = (((ETHPriceFNX-AlertEtherHF)/(AlertEtherHF)))
        ETHPRL = (((ETHPriceFNX-AlertEtherLF)/(AlertEtherLF)))
        if eth() > AlertEtherHF:
            if ETHPRH > 0.05:
                winsound.PlaySound('power.wav', winsound.SND_FILENAME)
                AlertEtherHF = ETHPriceFNX+2
            else:
                winsound.PlaySound('power.wav', winsound.SND_FILENAME)
                AlertEtherHF+=2
            
        if ETHPriceFNX < AlertEtherLF:
            if ETHPRL < -0.05:
                winsound.PlaySound('down.wav', winsound.SND_FILENAME)
                AlertEtherLF = ETHPriceFNX-2
            else:
                winsound.PlaySound('down.wav',winsound.SND_FILENAME)
                AlertEtherLF-=2
    try:
        thread.start_new_thread(alert_fnc, ("Thread-1", 2,))
    except:
        continue



    os.system('cls' if os.name == 'nt' else "printf '\033c'")



    def printFN():

        print "------------------------------------------------------------------------"
        print "Total Holdings:",calcTH(),"Percent Change:",calcPCT(),"%"," Total Profit:",calcPH()
        print "------------------------------------------------------------------------"
        print " "
        print "------------------------------------------------------------------------"
        print "The Price of Bitcoin is",btc()
        print "------------------------------------------------------------------------"

        print " "
        print "------------------------------------------------------------------------"
        print "The Price of Ethereum is",eth(),"[ Current Price Alert =","High:",AlertEtherHF,"Low:",AlertEtherLF,"]"
        print "------------------------------------------------------------------------"

        print " "
        print "------------------------------------------------------------------------"
        print "The Price of NEO is",neo()
        print "Percent change: |1 Hour = " + str(neoPR1())+"%|" + " |24 Hours = "+ str(neoPR24())+"%|"
        print "------------------------------------------------------------------------"

        print " "
        print "------------------------------------------------------------------------"
        print "The Price of OMG is",omg()
        print "Percent change: |1 Hour = " + str(omgPR1())+"%|" + " |24 Hours = "+ str(omgPR24())+"%|"
        print "------------------------------------------------------------------------"

        print " "
        print "------------------------------------------------------------------------"
        print "The Price of 0x is",zrx()
        print "Percent change: |1 Hour = " + str(zrxPR1())+"%|" + " |24 Hours = "+ str(zrxPR24())+"%|"
        print "------------------------------------------------------------------------"

    thread.start_new_thread(printFN, ())

    time.sleep(25)

    
