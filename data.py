import requests

question_data = requests.get("https://opentdb.com/api.php", params={"amount": 10, "type": "boolean", "category": 18})
question_data.raise_for_status()
question_data = question_data.json()
question_data = question_data["results"]