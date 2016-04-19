import urllib
import lxml.html
connection = urllib.urlopen('http://www.20min.ch')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    if ('index.' in link):
        print link
