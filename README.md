# Magic Mirror 
Checkout my blog on Medium https://medium.com/@MaziBoustani/build-your-own-smart-mirror-just-under-300-4d5ad1c833bf

Source code for building your own magic mirror webiste

## Step1:

Install python Flask

`pip install flask`

## Step2: 

Get the source code:

`$ git clone https://github.com/MBoustani/MagicMirror.git`

`$ cd MagicMirror`

## Step3:

Configure weather API:

Register on OpenWeatherMap API and get a key.

https://home.openweathermap.org/api_keys

To find your city code id open this file and look for you city, then grab the `id`.

http://bulk.openweathermap.org/sample/city.list.json.gz 

Open file `app.py` and add `openweathermap_API_Key` and `city_id` values.


## Step4:

Run the flask webserver

`python app.py`

## Step5:

Open the browser and go to the link: http://localhost:5000/
Wait around 30 seconds for all information to show up.
