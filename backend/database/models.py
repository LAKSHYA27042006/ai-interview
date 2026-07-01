from sqlalchemy import (
    Column,
    Integer,
    Float,
    String
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class InterviewResultDB(Base):

    __tablename__ = "interview_results"

    id = Column(Integer, primary_key=True)

    candidate_name = Column(String)

    overall_score = Column(Float)

    eye_contact_score = Column(Float)

    words_per_minute = Column(Float)

    vocabulary_score = Column(Float)

    recommendation = Column(String)
    feedback = Column(String)

    report_path = Column(String)