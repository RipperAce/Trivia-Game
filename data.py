import requests
import html

QUESTION_COUNT = 10
QUESTION_TYPE = "boolean"

Parameter = {"amount": QUESTION_COUNT, "type": QUESTION_TYPE, "category": 19}

questionResponse = requests.get(url="https://opentdb.com/api.php", params=Parameter)
questionResponse.raise_for_status()

data = questionResponse.json()
question_data = data["results"]
questions = []
answers = []

for question in question_data:
    questions.append(html.unescape(question["question"]))
    answers.append(question["correct_answer"])