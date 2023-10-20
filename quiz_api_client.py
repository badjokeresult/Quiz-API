import requests
import json

from db_worker import DbWorker


API_URL = "https://jservice.io/api/random?count="


class QuizAPIClient:
    def __init__(self):
        self.url: str = API_URL
        self.db_worker = DbWorker()

    def get_response_from_url(self, questions_num: int):
        questions_left = questions_num
        while True:
            response = requests.get(self.url + str(questions_left))
            if response.status_code != 200:
                raise ValueError("Error occured during requesting outer API-service")

            questions = json.loads(response.text)
            last_inserted_question = None
            for question in questions:
                saved_category = self.db_worker.get_category(int(question["category"]["id"]))
                if not saved_category:
                    self.db_worker.insert_category(question["category"])

                saved_question = self.db_worker.get_question(int(question["id"]))
                if not saved_question:
                    self.db_worker.insert_question(question)
                    last_inserted_question = json.dumps(question)
                    questions_left -= 1
                else:
                    questions_left += 1

            if questions_left == 0:
                break

        return json.loads(last_inserted_question)
