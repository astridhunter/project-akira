## greet
* greet
    - utter_greet

## bye
* bye
    - utter_bye

## thank
* thank
    - utter_welcome

## Twitter Trends 01
* greet
    - utter_greet
* twitter_trend_query{"location": "India"}
    - slot{"location": "India"}
    - action_get_twitter_trends
    - slot{"location": "India"}
* bye
    - utter_bye

## Twitter Trends 02
* greet
    - utter_greet
* twitter_trend_query
    - utter_ask_location
* twitter_trend_query{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_get_twitter_trends
    - slot{"location": "Chennai"}
* bye
    - utter_bye

## Weather Bot 01
* greet
   - utter_greet
* ask_weather
   - utter_ask_location
* ask_weather{"city":"London"}
   - slot{"city": "London"}
   - action_get_weather
* goodbye
   - utter_goodbye

## Weather Bot 02
* greet
   - utter_greet
* ask_weather{"city":"Paris"}
   - slot{"city": "Paris"}
   - action_get_weather
* goodbye
   - utter_goodbye 