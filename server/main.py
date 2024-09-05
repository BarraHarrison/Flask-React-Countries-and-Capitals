import os
import json
from flask import Flask, jsonify, render_template


app = Flask(__name__)


def load_countries_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file
    json_path = os.path.join(base_dir, '../countries.json')  # Adjust the relative path
    with open(json_path, 'r') as file:
        return json.load(file)['countries']

countries_data = load_countries_data()


@app.route('/homepage', methods=['GET'])
def home():
        return render_template('index.html')

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = [country['country'] for country in countries_data]
    return jsonify(countries)


@app.route('/countries-and-capitals', methods=['GET'])
def get_countries_and_capitals():
    return render_template('countries.html', countries=countries_data)


@app.route('/country/<country_name>', methods=['GET'])
def get_country_and_capital(country_name):
    country_name = country_name.title()  
    for country in countries_data:
        if country['country'].lower() == country_name.lower():
            return jsonify({country['country']: country['capital']})
    return jsonify({"error": "Country not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
