# Please install Anki first, then add the Add-on Anki Connect. Anki needs to be open while executing this application.

import requests
import json
import os
from datetime import datetime


def invoke(action, **params):
    request_payload = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    })
    response = requests.post('http://localhost:8765', data=request_payload)
    return json.loads(response.content)

def add_note_to_deck(front_content, back_content):
    note = {
        "deckName": "AWS Certified Solutions Architect",
        "modelName": "Basic",
        "fields": {
            "Front": front_content,
            "Back": back_content
        },
        "options": {
            "allowDuplicate": False
        },
        "tags": ["aws", "solutions-architect"]
    }
    result = invoke('addNote', note=note)
    if len(result) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in result:
        raise Exception('response is missing required error field')
    if 'result' not in result:
        raise Exception('response is missing required result field')
    if result['error'] is not None:
        raise Exception(result['error'])
    return result['result']

def format_answer(answer):
    # Check if the answer is a list
    if isinstance(answer, list):
        enumerated_answers = "<br>".join([f"{i+1}. {ans}" for i, ans in enumerate(answer)])
        return f"Answers:<br>{enumerated_answers}"
    else:
        return f"Answer: {answer}"
    
def read_json_and_add_note():
    with open("input.txt", "r") as file:
        data_json = json.load(file)

    # Save the content under a new name
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')  # YearMonthDayHourMinuteSecondMicrosecond
    if not os.path.exists("saved_jsons"):
        os.makedirs("saved_jsons")
    with open('saved_jsons/copy-input' + str(timestamp) + '.txt', 'w') as archive_file:
        json.dump(data_json, archive_file)
        
    for data in data_json:
        question = data["question"]
        options = "<br>".join([f"{i+1}. {option}" for i, option in enumerate(data["options"])])
        answer = format_answer(data["answer"])
        explanation = data["explanation"]
        result = explanation[0] if isinstance(explanation, list) and len(explanation) == 1 else explanation
        back_content = f"{answer}<br><br>Explanation:<br>{result}"
        front_content = f"{question}<br><br>Options:<br>{options}"
        return_statement = add_note_to_deck(front_content, back_content)

    return 1

# Example usage:
read_json_and_add_note()
