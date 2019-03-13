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