import pygal 
import pickle

from flask import Flask, render_template
states=[ 'AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DN', 'DD', 'DL', 'GA','GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH', 'MN','ML', 'MZ', 'NL', 'OR', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UP','UT', 'WB']

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def home():
    return render_template("layout.html")

@app.route('/graph')
def plot():
    response = dict()
    response['worldmap'] = pickle.load( open('./plots/worldmap.sav', 'rb') )
    response['country_line'] = pickle.load( open('./plots/Country_Line.sav', 'rb') )
    response['country_pie'] = pickle.load( open('./plots/Country_pie.sav', 'rb') )
    for i in states:
    	response[i+'_line'] = pickle.load( open('./plots/'+i+'_Line.sav', 'rb') )
    	response[i+'_pie'] = pickle.load( open('./plots/'+i+'_Pie.sav', 'rb') )
    return render_template("graph.html", response = response)

if __name__ == '__main__':
    app.run(debug=True)