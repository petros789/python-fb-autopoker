import cookielib
import urllib, urllib2
import re
import xml.dom.minidom
import time
from xml.dom.minidom import parse, parseString

if __name__ == '__main__':
    urlLogin = 'http://m.facebook.com/login.php'

    uid    = 'INSERT EMAIL'
    password = 'INSERT PASSWORD'

    fieldId   = 'email'
    fieldPass = 'pass'
    
    ButtonId = 'login'
    Button = 'submit'

    cj = cookielib.CookieJar()
    data = urllib.urlencode({fieldId:uid, fieldPass:password, ButtonId:Button})

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    urllib2.install_opener(opener)
    usock = opener.open(urlLogin)
    usock = opener.open(urlLogin, data)
    usock.close()
 
    usock = opener.open('http://m.facebook.com/pokes')
    pageSource = usock.read()
    usock.close()
    
    pattern = r'/a/notifications.php\?poke\=.*?(?=\")'
    regex = re.compile(pattern)
   
    while 1 == 1:
        print("Looping...")
        usock = opener.open('http://m.facebook.com/pokes')
        PokingData = (usock.read())
        usock.close()

        for match in regex.finditer(PokingData):
            url = match.group(0)
    	    redpill = (url).replace('&amp;', '&')
            print "POKE! %s: %s" % (match.start(), 'https://m.facebook.com' + redpill)
            usock = opener.open("http://m.facebook.com"+redpill)
            usock.close()
        time.sleep(5)
