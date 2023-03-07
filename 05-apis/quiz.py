import random

import requests
import json
import html

url = 'https://opentdb.com/api.php?amount=10&type=multiple'

response = requests.get(url)

data = json.loads(response.text)

rows = data['results']

score = 0

for row in rows:
    print(html.unescape(row['question']))
    answers = []
    correct_pos = random.randint(0, 3)
    incorrect_index = 0
    print(html.unescape(row['correct_answer']))

    for i in range(4):
        if i == correct_pos:
            answers.append(html.unescape(row['correct_answer']))
        else:
            answers.append(html.unescape(row['incorrect_answers'][incorrect_index]))
            incorrect_index += 1
    counter = 1
    for answer in answers:
        print(str(counter) + ".", answer)
        counter += 1

    selection = int(input("Answer: "))
    if selection == correct_pos + 1:
        score += 1

print("SCORE:", score, "/ 10")
