#Python 2.7.13 :: Anaconda custom (x86_64)

import urllib2

url_increase = "http://localhost:5000/increase?value=";
url_decrease = "http://localhost:5000/decrease?value=";


for x in range(1000) :
    answer = urllib2.urlopen(url_increase+str(x)).read()
    print "connecting api attempt " , x , " answer " ,answer


for x in range(1000) :
    answer = urllib2.urlopen(url_decrease+str(x)).read()
    print "connecting api attempt " , x , " answer " ,answer



print "That was it !"
