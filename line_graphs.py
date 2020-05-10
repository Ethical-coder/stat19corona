code_to_name={'AN': 'Andaman & Nicobar Islands',
 'AP': 'Andhra Pradesh',
 'AR': 'Arunachal Pradesh',
 'AS': 'Assam',
 'BR': 'Bihar',
 'CH': 'Chandigarh',
 'CT': 'Chhattisgarh',
 'DD': 'Daman & Diu',
 'DL': 'Delhi',
 'DN': 'Dadar & Nagar Haveli',
 'GA': 'Goa',
 'GJ': 'Gujrat',
 'HP': 'Himachal Pradesh',
 'HR': 'Haryana',
 'JH': 'Jharkhand',
 'JK': 'Jammu & Kashmir',
 'KA': 'Karnatak',
 'KL': 'Kerela',
 'LA': 'Lakshwadeep',
 'LD': 'Laddakh',
 'MH': 'Maharashtra',
 'ML': 'Meghalaya',
 'MN': 'Manipur',
 'MP': 'Madhya Pradesh',
 'MZ': 'Mizoram',
 'NL': 'Nagaland',
 'OR': 'Odisha',
 'PB': 'Punjab',
 'PY': 'Pondicherry',
 'RJ': 'Rajasthan',
 'SK': 'Sikkim',
 'TG': 'Telangana',
 'TN': 'Tamil Nadu',
 'TR': 'Tripura',
 'UP': 'Uttar Pradesh',
 'UT': 'Uttarakhand',
 'WB': 'West Bengal'}

import pandas as pd
import pygal.maps.world
from pygal.style import NeonStyle
import pickle

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import json



url='https://api.covid19india.org/data.json'
uclient=ureq(url)
page_html=uclient.read()
uclient.close()

page_soup=soup(page_html,"html.parser")
page_json=json.loads(page_soup.text)

data=pd.DataFrame(page_json['cases_time_series'])

daily_confirmed=list()
daily_decreased=list()
daily_recovered=list()
confirmed=list()
recovered=list()
decreased=list()
for i in range(len(data)):
    daily_confirmed.append(int(data.iloc[i,0]))
    daily_decreased.append(int(data.iloc[i,1]))
    daily_recovered.append(int(data.iloc[i,2]))
    confirmed.append(int(data.iloc[i,4]))
    recovered.append(int(data.iloc[i,6]))
    decreased.append(int(data.iloc[i,5]))
    
graph=pygal.Line(fill=True, interpolate='cubic', style=NeonStyle,font_family='googlefont:Raleway')
graph.title='India corona cases'
graph.add('Total Confirmed Cases',confirmed)
graph.add('Total Decreased Cases',decreased)
graph.add('Total Recovered Cases',recovered)
graph.add('Daily Confirmed Cases',daily_confirmed)
graph.add('Daily Decreased Cases',daily_decreased)
graph.add('Daily Recovered Cases',daily_recovered)
graph.render_to_file('./plots/Country_Line.svg')


url='https://api.covid19india.org/states_daily.json'
uclient=ureq(url)
page_html=uclient.read()
uclient.close()

page_soup=soup(page_html,"html.parser")
page_json=json.loads(page_soup.text)

data=pd.DataFrame(page_json['states_daily'])
states=data.columns

for i in states:
    if i!='date' and i!='status' and i!='tt':
        data_con=data[data['status']=='Confirmed']
        data_con=data_con[i]
        data_dec=data[data['status']=='Deceased']
        data_dec=data_dec[i]
        data_rec=data[data['status']=='Recovered']
        data_rec=data_rec[i]
                

        total_con=list()
        total_dec=list()
        total_rec=list()
        daily_con=list()
        daily_dec=list()
        daily_rec=list()
        count_con=0
        count_dec=0
        count_rec=0
        for j in data_con:
            try:
                daily_con.append(int(j))
                count_con+=int(j)
                total_con.append(count_con)
            except:
                daily_con.append(0)
                total_con.append(0)
        
        for j in data_dec:
            try:
                daily_dec.append(int(j))
                count_dec+=int(j)
                total_dec.append(count_dec)
            except:
                daily_dec.append(0)
                total_dec.append(0)
        
        for j in data_rec:
            try:
                daily_rec.append(int(j))
                count_rec+=int(j)
                total_rec.append(count_rec)
            except:
                daily_rec.append(0)
                total_rec.append(0)
            
        graph=pygal.Line(fill=True, interpolate='cubic', style=NeonStyle,font_family='googlefont:Raleway')
        graph.title=str(code_to_name[i.upper()])+' Corona Cases'
        graph.add('total confirmed',total_con)
        graph.add('total deceased',total_dec)
        graph.add('total recovered',total_rec)
        graph.add('daily confirmed',daily_con)
        graph.add('daily deceased',daily_rec)
        graph.add('daily recovered',daily_dec)


        graph.render_to_file('./plots/'+i.upper()+'_Line.svg')




