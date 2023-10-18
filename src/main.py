from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from quiz_api_client import QuizAPIClient

app = FastAPI()

db_engine = create_engine("postgresql://quizuser:5%6J2;ag@postgresql:5432/quizdb")

session_local = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


class Request(BaseModel):
    questions_num: int


@app.post("/api/v1/quiz/get_questions")
async def request_questions(request: Request):
    quiz_api_client = QuizAPIClient()
    return quiz_api_client.get_response_from_url(request.questions_num)
