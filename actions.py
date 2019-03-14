from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import tweepy

consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_token = 'ACCESS TOKEN'
access_token_secret = 'TOKEN SECRET'

class ActionGetTrends(Action):
    def name(self):
        return "action_get_twitter_trends"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('location')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        url_for_woeid = 'https://www.metaweather.com/api/location/search/?query=' + city

        try:
            request = json.loads(requests.get(url_for_woeid).text)
            woeid = request[0]
            woeid = woeid['woeid']

            trends1 = api.trends_place(woeid)
            data = trends1[0]
            trends = data['trends']
            names = [trend['name'] for trend in trends]
            top_5_names = names[0:4]
            trendsName = ' '.join(top_5_names)
            
            dispatcher.utter_message(trendsName)
        
        except tweepy.error.TweepError as err:
            dispatcher.utter_message("Sorry, I don't have access to that.")

        return [SlotSet("location", city)]

class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('location')
        api_key = "374b7fbffe367b0c2974e656fdeab696"
        
        skeleton = "https://api.openweathermap.org/data/2.5/weather?"
        complete_url = skeleton + "q=" + city + "&APPID=" + api_key
        
        response = requests.get(complete_url)

        data = response.json()
        
        x=data['main']
        temp = round(x['temp'] - 273.15, 2)
        place = data["name"]
        x = data['weather']
        desc = x[0]['main']

        weather_data = "It's {}*C currently in {}. The weather can be described as {}".format(temp, place, desc)
        dispatcher.utter_message(weather_data)

        return [SlotSet("location", city)]