## greet
* greet
  - utter_greet

## bye
* bye
  - utter_bye

## Twitter Trends 01
* greet
    - utter_greet
* trend_query_loc{"location": "India"}
    - slot{"location": "India"}
    - action_get_trends
    - slot{"location": "India"}
* bye
    - utter_bye

## Twitter Trends 02
* greet
    - utter_greet
* trend_query_loc
    - utter_ask_location
* trend_query_loc{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_get_trends
    - slot{"location": "Chennai"}
* bye
    - utter_bye