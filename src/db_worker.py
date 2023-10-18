from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


DB_CONN_STR = "postgresql://quizuser:5%6J2;ag@localhost:5432/quizdb"


class DbWorker:
    db_engine = create_engine(DB_CONN_STR)
    session_local = sessionmaker(autoflush=False, autocommit=False, bind=db_engine)

    def insert_question(self, question: dict):
        db = self.session_local()

        db.add(
            Question(
                id=question["id"],
                answer=question["answer"],
                question=question["question"],
                created_at=question["created_at"],
                category_id=question["category_id"],
            )
        )

        db.commit()
        db.close()

    def insert_category(self, category: dict):
        db = self.session_local()

        db.add(
            Category(
                id=category["id"],
                title=category["title"],
                created_at=category["created_at"],
            )
        )

        db.commit()
        db.close()

    def get_question(self, question_id: int):
        db = self.session_local()
        question = db.query(Question).filter(Question.id == question_id).first()
        db.close()
        return question

    def get_category(self, category_id: int):
        db = self.session_local()
        category = db.query(Category).filter(Category.id == category_id).first()
        db.close()
        return category
