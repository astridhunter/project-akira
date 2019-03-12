# Artificial Knowledge and Information Retrieval Assistant

Note: This project is in early phases of its development 

In short, Akira is an information retrieval bot. On top of that, we plan to add the logic for information synthesis and general conversational skills. 
The core idea is to build a bot that assists the user in doing online research for them, for writing an article, creating content or gathering more information about something interactively and engagingly.

Basic objectives include creation of a bot that can:
- Retrieve key information from online sources based on the queries of the user.
- Help a content creator in ideation and development.
- Answer general questions that a user can ask.
- Ask typical questions to the user about their thoughts on the topic in research.
- Can draft short sentences of its own to assist in content creation.
- Suggest new ideas for viral content creation based on latest online trends.

The bot is being built in python using the open source rasa stack. Stay tuned as we update the project from time to time.

### General Instructions

The follows commands can be used in terminal/cmd/anaconda prompt

- To train the nlu model:

`python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose`

- To train the core dialog management model:

`python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policies.yml`

- To run the bot in cmd/anaconda prompt/terminal:

`python -m rasa_core.run -d models/dialogue -u models/current/nlu/ --endpoints endpoints.yml`

- To run the bot in interactive learning mode:

`python -m rasa_core.train interactive --core models/dialogue --nlu models/current/nlu --endpoints endpoints.yml`

### Developer Instructions
Current Objectives: 
- Add more nlu data for different general conversational intents
- Add more general conversational stories
- Implement various custom actions into akira
- Modify the domain file accordingly
