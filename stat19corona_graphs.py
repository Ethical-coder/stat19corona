import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pygal.style import NeonStyle
import pygal
import pickle
#importing url
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vSz8Qs1gE_IYpzlkFkCXGcL_BqR8hZieWVi-rphN1gfrO3H4lDtVZs4kd0C3P8Y9lhsT1rhoB-Q_cP4/pubhtml'
c=pd.read_html(url,header=0)

#for checking index of table which is having info. regarding states
index=1
index2=0
check1=1
check2=1
for i in range(0,len(c)):
    if 'TT' in c[i].columns and 'MP' in c[i].columns and 'UP' in c[i].columns and check1:
        index=i
        check1=0
        
    if 'State code' in c[i].columns and  'Detected District' in c[i].columns and check2:
        index2=i
        check2=0

states=c[index].columns[4:]



#interation for each state to plot line graph and pie graph of districs of states

for state in states:
    #processing data for plotting graph 
    data_state=c[index][['Status','Date',state]]
    data_state.fillna(0,inplace=True)
    data_state_confirmed=data_state[data_state['Status']=='Confirmed']
    data_state_recovered=data_state[data_state['Status']=='Recovered']
    data_state_decreased=data_state[data_state['Status']=='Deceased']
    total=0
    
    #adding for cumulative freq
    #preparing data of number of confirmed cases in state
    state_confirmed=list()
    for i in data_state_confirmed[state]:
        total+=i
        state_confirmed.append(total)
        
    #preparing data of number of recovered cases in state
    total=0
    state_recovered=list()
    for i in data_state_recovered[state]:
        total+=i
        state_recovered.append(total)

    #preparing data of number of fatality cases in state
    total=0
    state_decreased=list()
    for i in data_state_decreased[state]:
        total+=i
        state_decreased.append(total)
    
    #declearning and defining style for line graph

    graph=pygal.Line(fill=True, interpolate='cubic', style=NeonStyle,font_family='googlefont:Raleway')

    #plotting and saving line graph
    graph.add('Confirmed',state_confirmed)
    graph.add('Recovered',state_recovered)
    graph.add('Fatalities',state_decreased)

    #filtering country so as to plot districts of state and saving line graphs    
    if state=='TT':
        graph.title='Country Corona Cases'
        response=graph.render_data_uri()
        pickle.dump(response,open('./plots/Country_Line.sav','wb'))
    else:
        graph.title=state+' Corona Cases'
        response=graph.render_data_uri()
        pickle.dump(response,open('./plots/'+state+'_Line.sav','wb'))
        
        #pie graph of districts
        #data processing for pie chart creation
        data=c[index2]
        state_data=data[data['State code']==state]
        districts=state_data['Detected District'].dropna().unique()
        counts_number=state_data['Detected District'].value_counts()
        
        #declearing and alloting style to pie chart
        mp_pie_chart=pygal.Pie(inner_radius=0.4, style=NeonStyle,font_family='googlefont:Raleway')
        
        #plooting districts and defining title
        mp_pie_chart.title='Pie Chart Of Corona Positives In Districts Of '+state
        for i in districts:
            mp_pie_chart.add(i,counts_number[i])
        #saving pie chart
        response=mp_pie_chart.render_data_uri()
        pickle.dump(response,open('./plots/'+state+'_Pie.sav','wb'))
        
        
        
#Pie graph of states
data=c[index2]['State code']
state_count=data.value_counts()

pie_chart_country=pygal.Pie( inner_radius=0.4,style=NeonStyle,font_family='googlefont:Raleway')
pie_chart_country.title='Pie chart Of States Of India'
for u,v in state_count.items():
    pie_chart_country.add(u,v)
response=pie_chart_country.render_data_uri()
pickle.dump(response,open('./plots/Country_pie.sav','wb'))



