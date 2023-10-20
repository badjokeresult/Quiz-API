from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import *


DB_CONN_STR = "postgresql://quizuser:5%6J2;ag@postgresql:5432/quizdb"
DB_ENGINE = create_engine(DB_CONN_STR)
SESSION_MAKER = sessionmaker(autoflush=False, autocommit=False, bind=DB_ENGINE)


def manage_db_context(func):
    def wrapper(self, *args):
        db = SESSION_MAKER()
        try:
            func(self, db, *args)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    return wrapper


class DbWorker:
    @manage_db_context
    def insert_question(self, db: Session, question: dict) -> None:
        db.add(
            Question(
                id=question["id"],
                answer=question["answer"],
                question=question["question"],
                created_at=question["created_at"],
                category_id=question["category_id"],
            )
        )

    @manage_db_context
    def insert_category(self, db: Session, category: dict) -> None:
        db.add(
            Category(
                id=category["id"],
                title=category["title"],
                created_at=category["created_at"],
            )
        )

    @manage_db_context
    def get_question(self, db: Session, question_id: int):
        return db.query(Question).filter(Question.id == question_id).first()

    @manage_db_context
    def get_category(self, db: Session, category_id: int):
        return db.query(Category).filter(Category.id == category_id).first()
