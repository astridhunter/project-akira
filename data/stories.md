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
* ask_twitter_trends{"location": "India"}
    - slot{"location": "India"}
    - action_get_twitter_trends
    - slot{"location": "India"}
* bye
    - utter_bye

## Twitter Trends 02
* greet
    - utter_greet
* ask_twitter_trends
    - utter_ask_location
* ask_twitter_trends{"location": "Chennai"}
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
* ask_weather{"location":"London"}
    - slot{"location": "London"}
    - action_get_weather
    - slot{"location": "London"}
* goodbye
    - utter_bye

## Weather Bot 02
* greet
    - utter_greet
* ask_weather{"location":"Paris"}
    - slot{"location": "Paris"}
    - action_get_weather
    - slot{"location": "Paris"}
* goodbye
    - utter_bye

## Number Fact 1
* greet
	- utter_greet
* ask_number_fact{"number":"7"}
	- slot{"number":"7"}
	- action_get_number_fact
* goodbye
	- utter_bye

## Number Fact 2
* ask_number_fact{"number":"9"}
    - slot{"number":"9"}
    - action_get_number_fact
