import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from pygal.style import NeonStyle
import pygal

#importing url
url='http://patientdb.covid19india.org/'
c=pd.read_html(url,header=0)

index=1
for i in range(1,len(c)):
    if 'TT' in c[i].columns and 'MP' in c[i].columns and 'UP' in c[i].columns:
        index=i
        break

states=c[index].columns[4:]




#graphs of states

for state in states:

    data_state=c[3][['Status','Date',state]]
    data_state.fillna(0,inplace=True)
    data_state_confirmed=data_state[data_state['Status']=='Confirmed']
    data_state_recovered=data_state[data_state['Status']=='Recovered']
    data_state_decreased=data_state[data_state['Status']=='Deceased']
    total=0
    
    #adding for cumulative freq
    state_confirmed=list()
    for i in data_state_confirmed[state]:
        total+=i
        state_confirmed.append(total)
        
        
    total=0
    state_recovered=list()
    for i in data_state_recovered[state]:
        total+=i
        state_recovered.append(total)

    
    total=0
    state_decreased=list()
    for i in data_state_decreased[state]:
        total+=i
        state_decreased.append(total)
    
    #declearning and defining style

    graph=pygal.Line(fill=True, interpolate='cubic', style=NeonStyle,font_family='googlefont:Raleway')

    #plotting and saving

    graph.add('Confirmed',state_confirmed)
    graph.add('Recovered',state_recovered)
    graph.add('Fatalities',state_decreased)
    
    if state=='TT':
        graph.title='Country Corona Cases'
        graph.render_to_file('Country Corona Cases.svg')
    else:
        graph.title=state+' Corona Cases'
        graph.render_to_file(state+' Corona Cases.svg')
        
        #pie graph of districts
        data=c[0]
        state_data=data[data['State code']==state]
        districts=state_data['Detected District'].dropna().unique()
        counts_number=state_data['Detected District'].value_counts()
        mp_pie_chart=pygal.Pie(inner_radius=0.4, style=NeonStyle,font_family='googlefont:Raleway')

        mp_pie_chart.title='Pie Chart Of Corona Positives In Districts Of '+state
        for i in districts:
            mp_pie_chart.add(i,counts_number[i])
    
        mp_pie_chart.render_to_file(state+' Districts_pie_chart.svg')
        
        
        
        
#Pie graph of states
data=c[0]['State code']
state_count=data.value_counts()

pie_chart_country=pygal.Pie( inner_radius=0.6,style=NeonStyle,font_family='googlefont:Raleway')
pie_chart_country.title='Pie chart Of States Of India'
for u,v in state_count.items():
    pie_chart_country.add(u,v)
pie_chart_country.render_to_file('Pie Chart Of States Of India.svg')




