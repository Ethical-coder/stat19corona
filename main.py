import pygal 
import pickle

from flask import Flask, render_template

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def home():
    return render_template("layout.html")

@app.route('/graph')
def plot():
    response = [None, None, None, None, None]
    response[0] = pickle.load( open('./plots/worldmap.sav', 'rb') )
    response[1] = pickle.load( open('./plots/Country_Line.sav', 'rb') )
    response[2] = pickle.load( open('./plots/Country_pie.sav', 'rb') )
    response[3] = pickle.load( open('./plots/MP_Line.sav', 'rb') )
    response[4] = pickle.load( open('./plots/MP_Pie.sav', 'rb') )
    return render_template("graph.html", response = response)

if __name__ == '__main__':
    app.run(debug=True)