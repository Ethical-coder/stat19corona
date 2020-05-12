import pygal
import pickle

from flask import Flask, render_template
states=[ 'AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DN', 'DD', 'DL', 'GA','GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH', 'MN','ML', 'MZ', 'NL', 'OR', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UP','UT', 'WB']
state_list = {'Andaman & Nicobar Islands': 'AN', 'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR', 'Chandigarh': 'CH', 'Chhattisgarh': 'CT', 'Dadar & Nagar Haveli': 'DN', 'Daman & Diu': 'DD', 'Delhi': 'DL', 'Goa': 'GA', 'Gujrat': 'GJ', 'Haryana': 'HR', 'Himachal Pradesh': 'HP', 'Jammu & Kashmir': 'JK', 'Jharkhand': 'JH', 'Karnatak': 'KA', 'Kerela': 'KL', 'Lakshwadeep': 'LA', 'Laddakh': 'LD', 'Madhya Pradesh': 'MP', 'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML', 'Mizoram': 'MZ', 'Nagaland': 'NL', 'Odisha': 'OR', 'Pondicherry': 'PY', 'Punjab': 'PB', 'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TG', 'Tripura': 'TR', 'Uttar Pradesh': 'UP', 'Uttarakhand': 'UT', 'West Bengal': 'WB'}
app = Flask(__name__, template_folder = 'template')

@app.route('/')
def home():
    # response = dict()
    # response['worldmap'] = pickle.load( open('./plots/worldmap.sav', 'rb') )
    # response['country_line'] = pickle.load( open('./plots/Country_Line.sav', 'rb') )
    # response['country_pie'] = pickle.load( open('./plots/Country_pie.sav', 'rb') )
    # for i in states:
    # 	response[i+'_line'] = pickle.load( open('./plots/'+i+'_Line.sav', 'rb') )
    # 	response[i+'_pie'] = pickle.load( open('./plots/'+i+'_Pie.sav', 'rb') )
    return render_template("graph.html", state_list=state_list)

if __name__ == '__main__':
    app.run(debug=True)
