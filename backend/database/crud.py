from database.database import SessionLocal
from database.models import InterviewResultDB


def save_interview_result(
    candidate_name,
    overall_score,
    eye_contact_score,
    words_per_minute,
    vocabulary_score,
    recommendation,
    feedback,
    report_path
):

    db = SessionLocal()

    try:

        result = InterviewResultDB(
    candidate_name=candidate_name,
    overall_score=overall_score,
    eye_contact_score=eye_contact_score,
    words_per_minute=words_per_minute,
    vocabulary_score=vocabulary_score,
    recommendation=recommendation,
    feedback=feedback,
    report_path=report_path
)

        db.add(result)
        db.commit()
        db.refresh(result)

        return result

    finally:

        db.close()


def get_all_results():

    db = SessionLocal()

    try:

        return db.query(
            InterviewResultDB
        ).all()

    finally:

        db.close()
def get_result_by_id(interview_id):
    db = SessionLocal()

    result = (
        db.query(InterviewResultDB)
        .filter(InterviewResultDB.id == interview_id)
        .first()
    )

    db.close()

    return result