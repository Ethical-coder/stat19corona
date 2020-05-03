import pickle

from flask import Flask, render_template, request, flash, redirect


states=[ 'AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DN', 'DD', 'DL', 'GA','GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH', 'MN','ML', 'MZ', 'NL', 'OR', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UP','UT', 'WB']

statelists = {'Andaman & Nicobar Islands': 'AN', 'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR', 'Chandigarh': 'CH', 'Chhattisgarh': 'CT', 'Dadar & Nagar Haveli': 'DN', 'Daman & Diu': 'DD', 'Delhi': 'DL', 'Goa': 'GA', 'Gujrat': 'GJ', 'Haryana': 'HR', 'Himachal Pradesh': 'HP', 'Jammu & Kashmir': 'JK', 'Jharkhand': 'JH', 'Karnatak': 'KA', 'Kerela': 'KL', 'Lakshwadeep': 'LA', 'Laddakh': 'LD', 'Madhya Pradesh': 'MP', 'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML', 'Mizoram': 'MZ', 'Nagaland': 'NL', 'Odisha': 'OR', 'Pondicherry': 'PY', 'Punjab': 'PB', 'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TG', 'Tripura': 'TR', 'Uttar Pradesh': 'UP', 'Uttarakhand': 'UT', 'West Bengal': 'WB'}

app = Flask(__name__, template_folder = 'template')

@app.route('/', methods=['POST', 'GET'])
def home():

    response = dict()
    response['worldmap'] = pickle.load( open('./plots/worldmap.sav', 'rb') )
    response['country_line'] = pickle.load( open('./plots/Country_Line.sav', 'rb') )
    response['country_pie'] = pickle.load( open('./plots/Country_pie.sav', 'rb') )
    response['state_line'] = None
    response['state_pie'] = None
    if(request.method == 'POST'):
        state_code  = request.form.get('state_code')
        print('statecode' + str(state_code))
        response = dict()
        response['worldmap'] = pickle.load( open('./plots/worldmap.sav', 'rb') )
        response['country_line'] = pickle.load( open('./plots/Country_Line.sav', 'rb') )
        response['country_pie'] = pickle.load( open('./plots/Country_pie.sav', 'rb') )
        response['state_line'] = pickle.load(open('./plots/'+state_code+'_Line.sav', 'rb'))
        response['state_pie'] = pickle.load(open('./plots/'+state_code+'_Pie.sav', 'rb'))
        return render_template("index.html",response = response, statelists = statelists)
    return render_template("index.html", response = response, statelists = statelists)

if __name__ == '__main__':
    app.run(debug=True)
