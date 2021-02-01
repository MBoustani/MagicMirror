from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():

    # add your openweathermap API Key and city id
    # to get the API key go to link: https://home.openweathermap.org/api_keys
    openweathermap_API_Key = ""

    # to find the city ID download this file and search for you city, grab the id and put in city_id varaible
    # http://bulk.openweathermap.org/sample/city.list.json.gz
    city_id = ""

    return render_template('index.html',
                            city_id=city_id,
                            openweathermap_API_Key=openweathermap_API_Key)

if __name__ == '__main__':
    app.debug = True
    app.run()