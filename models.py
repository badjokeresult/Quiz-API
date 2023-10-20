import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = "question"

    id = sa.Column(sa.Integer, primary_key=True)
    answer = sa.Column(sa.String, nullable=False)
    question = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)
    category_id = sa.Column(sa.Integer, sa.ForeignKey("category.id"), nullable=False)


class Category(Base):
    __tablename__ = "category"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)
