import pygal 
import pickle

from flask import Flask, render_template

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def home():
    return render_template("layout.html")

@app.route('/graph')
def plot():
    response = [None, None]
    response[0] = pickle.load( open('./plots/MP_Corona_Cases.sav', 'rb') )
    response[1] = pickle.load( open('./plots/MP_Districts_pie_chart.sav', 'rb') )
    return render_template("graph.html", response = response)

if __name__ == '__main__':
    app.run(debug=True)