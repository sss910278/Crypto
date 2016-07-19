from urllib2 import urlopen
import string
import threading
import time
import smtplib

def Alert(Check):
    import smtplib
    if (Check == 'U'):
        info = Coin + ' Price Over ' + str(UP) + ' BTC'
    elif (Check == 'L'):
        info = 'Price below' + str(LOW)

    gmail_user = 'ss910278@gmail.com'
    gmail_pwd = 'thedaniel'

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_pwd)

    fromaddr = "ss910278@gmail.com"
    toaddrs = ['ss910278@gmail.com']
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n" % (fromaddr, ", ".join(toaddrs), u'Price Alert ! !'))
    smtpserver.sendmail(fromaddr, toaddrs, msg + info)
    smtpserver.quit()

def Coin_Monitor():
    global UP,LOW
    threading.Timer(5.0, Coin_Monitor).start()
    response = urlopen('https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_'+Coin)
    Data = response.read()
    Rate = string.rfind(Data,'rate')
    Price =  string.atof(Data[Rate+7:Rate+17])
    print 'Last ' + Coin + ' rate : ' + str(Price) + ' BTC ' + ' _____ ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if(Price >= UP):
        Alert('U')
        UP = UP + (UP-LOW)/2
        LOW = LOW + (UP-LOW)/2
    elif(Price <= LOW):
        Alert('L')
        UP = UP - (UP-LOW)/2
        LOW = LOW - (UP-LOW)/2

print('Enter the upper price threshold for alert ')
UP = float(raw_input())
print('Enter the lower price threshold for alert ')
LOW = float(raw_input())
print('Enter the coin you wish to monitor ')
Coin = raw_input()

START = Coin_Monitor()
