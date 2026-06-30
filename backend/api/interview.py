from fastapi import APIRouter, UploadFile, File
import os
import shutil
import uuid
import json
from dataclasses import asdict

from services.interview_pipeline import InterviewPipeline

router = APIRouter()


@router.post("/analyze")
async def analyze_interview(file: UploadFile = File(...)):

    # Generate Interview ID
    interview_id = str(uuid.uuid4())

    # Create Upload Folder
    upload_dir = os.path.join(
        "..",
        "storage",
        "uploads",
        interview_id
    )

    os.makedirs(upload_dir, exist_ok=True)

    # Save Uploaded Video
    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run Interview Pipeline
    pipeline = InterviewPipeline()

    result = pipeline.analyze_interview(file_path)

    # Create Report Folder
    report_dir = os.path.join(
        "..",
        "storage",
        "reports",
        interview_id
    )

    os.makedirs(report_dir, exist_ok=True)

    # Save Result JSON
    report_path = os.path.join(
        report_dir,
        "result.json"
    )

    with open(report_path, "w") as report_file:
        json.dump(
            asdict(result),
            report_file,
            indent=4
        )

    return {
        "status": "success",
        "interview_id": interview_id,
        "filename": file.filename,
        "recommendation": result.recommendation,
        "report_path": report_path,
        "message": "Interview uploaded, processed, and report generated successfully."
    }