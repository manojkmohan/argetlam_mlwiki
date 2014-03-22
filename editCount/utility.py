#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
from bs4 import BeautifulSoup
'''
url = 'http://ml.wikipedia.org/w/api.php'
headers = { 'User-Agent' : 'Womens edit a thon' }
values = {'format':'json','action':'query','titles':'Json','prop':'revisions','rvprop':'ids'}
data = urllib.urlencode(values)
req = urllib2.Request(url, headers=headers, data = data)
html = urllib2.urlopen(req).read()
print html

'http://ml.wikipedia/w/api.php?action=query&titles=Json&prop=revisions&rvprop=ids&format=json'
'''

infoUrl = 'https://ml.wikipedia.org/w/index.php?title=Vimla_Varma&action=info'
infoData = {'title':'','action':'info'}
infoHeaders = { 'User-Agent' : 'Womens edit a thon India' }

articleList = ['ചിത്ര പി. യു','അരുണിമ സിൻഹ','അൽതിയ ഗിബ്സൺ','ധ്വനി ദേശായി','സമിന ബെയ്ഗ്',"അനന്യ ചാറ്റർജി"]

articleEditInfo = {}
def getEditCount(html):
    soup = BeautifulSoup(html)
    return int(soup.findAll('tr',id='mw-pageinfo-edits')[0].findAll('td')[1].text)

def createInfoParams(article):
    infoData['title'] = article
    return urllib.urlencode(infoData)
    
def getArticleEditCount():
    for article in articleList:
        infoParams = createInfoParams(article)
        req = urllib2.Request(infoUrl, headers=infoHeaders, data = infoParams)
        html = urllib2.urlopen(req).read()
        print article, 'page received'
        articleEditInfo[article] = getEditCount(html)
    return articleEditInfo
