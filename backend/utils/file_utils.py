import os
import uuid


UPLOAD_FOLDER = "uploads"


def create_upload_folder():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def generate_unique_filename(filename: str):
    extension = filename.split(".")[-1]
    unique_name = f"{uuid.uuid4()}.{extension}"
    return unique_name