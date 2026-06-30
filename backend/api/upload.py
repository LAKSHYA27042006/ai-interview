from fastapi import APIRouter, UploadFile, File
import shutil
import os

from schemas.upload_schema import UploadResponse
from utils.file_utils import (
    create_upload_folder,
    generate_unique_filename,
)

router = APIRouter()

create_upload_folder()


@router.post("/upload", response_model=UploadResponse)
async def upload_video(file: UploadFile = File(...)):

    filename = generate_unique_filename(file.filename)

    filepath = os.path.join("uploads", filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return UploadResponse(
        file_id=filename.split(".")[0],
        filename=filename,
        status="success",
        message="Video uploaded successfully",
    )