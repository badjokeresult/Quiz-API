from fastapi import FastAPI
from pydantic import BaseModel

from quiz_api_client import QuizAPIClient

app = FastAPI()


class Request(BaseModel):
    questions_num: int


@app.post("/api/v1/quiz/get_questions")
async def request_questions(request: Request) -> str:
    quiz_api_client = QuizAPIClient()
    print(quiz_api_client)
    return quiz_api_client.get_response_from_url(request.questions_num)
