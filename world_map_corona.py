codes=['ec','cd', 'zm','be','za', 'hn', 'id', 'dz', 'om', 'lu', 'mt', 'sr', 'ph', 'de', 'mn', 'sl', 'ba', 'ye', 'ci', 'bh', 'th', 'kw', 'dk', 'ie', 'tj', 'ml', 'mz', 're', 'gt', 'va', 'uz', 'lr', 'hk', 'sy', 'td', 'mu', 'al', 'co', 'ca', 'sc', 'et', 'bd', 'eh', 'ls', 'bi', 'cr', 'zw', 'cf', 've', 'bz', 'sk', 'ly', 'gw', 'tg', 'jp', 'in', 'ga', 'gq', 'sg', 'ps', 'uy', 'ae', 'ma', 'lk', 'ke', 'ee', 'tn', 'bw', 'np', 'mk', 'my', 'ni', 'gm', 'gl', 'ng', 'ne', 'ge', 'cu', 'bg', 'cm', 'mo', 'tw', 'sh', 'bt', 'na', 'sm', 'eg', 'bf', 'sv', 'cv', 'sd', 'ao', 'tz', 'la', 'st', 'kr', 'dj', 'se', 'sz', 'gb', 'gf', 'gu', 'tr', 'br', 'pg', 'gy', 'mm', 'at', 'bn', 'jm', 'gh', 'sn', 'cg', 'cy', 'mw', 'ar', 'az', 'ro', 'si', 'er', 'aq', 'iq', 'pa', 'no', 'by', 'yt', 'lt', 'it', 'ua', 'me', 'fr', 'af', 'cl', 'mx', 'is', 'do', 'sa', 'kg', 'ug', 'ad', 'pe', 'ir', 'pk', 'bo', 'us', 'gn', 'tm', 'rs', 'bj', 'jo', 'pl', 'li', 'kh', 'mv', 'rw', 'nz', 'ht', 'hu', 'so', 'cn', 'pt', 'nl', 'mc', 'fi', 'lv', 'il', 'ru', 'kz', 'pr', 'md', 'py', 'vn', 'tl', 'es', 'mr', 'gr', 'hr', 'au', 'cz', 'lb', 'am', 'mg', 'ch', 'kp']





import pandas as pd
import pygal.maps.world
from pygal.style import NeonStyle
import pickle

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import json
url='https://api.covid19api.com/summary'
uclient=ureq(url)
page_html=uclient.read()
uclient.close()     
page_soup=soup(page_html,"html.parser")
page_json=json.loads(page_soup.text)
test=pd.DataFrame(page_json['Countries'])
test['CountryCode']=test['CountryCode'].str.lower()

i=1
data=test[['CountryCode','TotalConfirmed']]
chart=pygal.maps.world.World(style=NeonStyle)
while i<=10000000:
    dreq=data[data['TotalConfirmed']>i]
    dreq=dreq[dreq['TotalConfirmed']<=10*i]
    names=dreq['CountryCode'].unique()
    creq=dict()
    for j in range(len(dreq)):
        creq[dreq.iloc[j,0]]=dreq.iloc[j,1]    
    chart.add('> '+str(i)+' and < '+str(10*i),creq)
    i*=10
response=chart.render_data_uri()


pickle.dump(response,open('./plots/worldmap.sav','wb'))
