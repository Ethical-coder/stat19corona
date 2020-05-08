

import pandas as pd
import pygal.maps.world
from pygal.style import NeonStyle
import pickle

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import json


# pie chart of districts
url='https://api.covid19india.org/v2/state_district_wise.json'
uclient=ureq(url)
page_html1=uclient.read()
uclient.close()


page_soup=soup(page_html1,"html.parser")
page_json=json.loads(page_soup.text)

pie1=pygal.Pie( inner_radius=0.4,style=NeonStyle,font_family='googlefont:Raleway')
pie1.title='Pie chart Of Indian states'

test1=pd.DataFrame(page_json)

for i in range(len(test1)):
    ans=0
    test=pd.DataFrame(test1.iloc[i,0])
    pie=pygal.Pie( inner_radius=0.4,style=NeonStyle,font_family='googlefont:Raleway')
    pie.title='Pie chart Of '+test1.iloc[i,1]

    for j in range(len(test)):
        ans+=int(test.iloc[j,1])
        pie.add(test.iloc[j,4],test.iloc[j,1])
    response=pie.render_data_uri()
    pickle.dump(response,open('./plots/'+test1.iloc[i,2]+'_Pie.sav','wb'))
    pie1.add(test1.iloc[i,1],ans)

response=pie1.render_data_uri()
pickle.dump(response,open('./plots/Country_pie.sav','wb'))  


empty_states={'DD','DN','LD','NL','SK'}
for state in empty_states:
	pie1=pygal.Pie( inner_radius=0.4,style=NeonStyle,font_family='googlefont:Raleway')
	pickle.dump(pie1.render_data_uri(),open('./plots/'+state+'_Pie.sav','wb'))
