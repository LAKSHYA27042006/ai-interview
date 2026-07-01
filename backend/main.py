from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from services.feedback_service import FeedbackService
from services.interview_pipeline import InterviewPipeline
from services.pdf_report_service import PDFReportService
from services.recommendation_service import get_recommendation

from database.crud import (
    save_interview_result,
    get_all_results,
    get_result_by_id
)

import shutil
import os

app = FastAPI(
    title="AI Interview Evaluation System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = InterviewPipeline()
pdf_service = PDFReportService()


@app.get("/")
def home():

    return {
        "message": "AI Interview Evaluation System Running"
    }


@app.get("/interviews")
def interviews():

    return get_all_results()


@app.get("/interviews/{interview_id}")
def interview_details(interview_id: int):

    result = get_result_by_id(interview_id)

    if not result:
        return {"message": "Interview not found"}

    return {
        "id": result.id,
        "candidate_name": result.candidate_name,
        "overall_score": result.overall_score,
        "eye_contact_score": result.eye_contact_score,
        "words_per_minute": result.words_per_minute,
        "vocabulary_score": result.vocabulary_score,
        "recommendation": result.recommendation,
        "feedback": result.feedback,
        "report_path": result.report_path
    }


@app.post("/analyze")
def analyze_interview():

    video_path = (
        "../dataset/raw_videos/interview_01.mp4"
    )

    result = pipeline.analyze_interview(
        video_path
    )

    reports_dir = (
        "../storage/reports"
    )

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    report_path = os.path.join(
        reports_dir,
        "interview_01_report.pdf"
    )

    pdf_service.generate_report(
        result,
        report_path
    )

    overall_score = result.overall_score

    recommendation = get_recommendation(
        overall_score
    )
    feedback = FeedbackService.generate_feedback(
    result.vision.eye_contact_score,
    result.communication.words_per_minute,
    result.communication.vocabulary_score
)

    save_interview_result(
        candidate_name="interview_01",
        overall_score=overall_score,
        eye_contact_score=result.vision.eye_contact_score,
        words_per_minute=result.communication.words_per_minute,
        vocabulary_score=result.communication.vocabulary_score,
        recommendation=recommendation,
        report_path=report_path
    )

    return {
        "analysis": result,
        "report_path": report_path
    }


@app.post("/analyze-upload")
async def analyze_upload(
    video: UploadFile = File(...)
):

    upload_dir = "../storage/uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    video_path = os.path.join(
        upload_dir,
        video.filename
    )

    with open(video_path, "wb") as buffer:

        shutil.copyfileobj(
            video.file,
            buffer
        )

    result = pipeline.analyze_interview(
        video_path
    )

    reports_dir = (
        "../storage/reports"
    )

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    video_name = os.path.splitext(
        video.filename
    )[0]

    report_path = os.path.join(
        reports_dir,
        f"{video_name}_report.pdf"
    )

    pdf_service.generate_report(
        result,
        report_path
    )

    overall_score = result.overall_score

    recommendation = get_recommendation(
        overall_score
    )
    feedback = FeedbackService.generate_feedback(
    result.vision.eye_contact_score,
    result.communication.words_per_minute,
    result.communication.vocabulary_score
)

    save_interview_result(
        candidate_name=video_name,
        overall_score=overall_score,
        eye_contact_score=result.vision.eye_contact_score,
        words_per_minute=result.communication.words_per_minute,
        vocabulary_score=result.communication.vocabulary_score,
        recommendation=recommendation,
        feedback=feedback,
        report_path=report_path
    )

    return {
        "message": "Interview analyzed successfully",
        "analysis": result,
        "report_path": report_path
    }


@app.get("/download-report/{interview_id}")
def download_report(interview_id: int):

    result = get_result_by_id(interview_id)

    if not result:
        return {"message": "Interview not found"}

    return FileResponse(
        result.report_path,
        filename=f"{result.candidate_name}_report.pdf",
        media_type="application/pdf"
    )