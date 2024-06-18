import requests

parameters = {
    "amount": 18,
    "type": "boolean",
    "category": 18
}

trivia = requests.get(url="https://opentdb.com/api.php", params=parameters)
trivia.raise_for_status()  # Get a response if it fails.

data = trivia.json()
question_data = data["results"] # with this data formatted strangely i.e. HTML entities
# we need to unescape the html entities
# Fixed that in quiz_brain.py using html module and "unescaped()" function.



