import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_video(video_file):

    files = {
        "video": (
            video_file.name,
            video_file,
            video_file.type
        )
    }

    response = requests.post(
        f"{BASE_URL}/analyze-upload",
        files=files
    )

    return response.json()


def get_all_interviews():

    response = requests.get(
        f"{BASE_URL}/interviews"
    )

    return response.json()


def get_interview_details(interview_id):

    response = requests.get(
        f"{BASE_URL}/interviews/{interview_id}"
    )

    return response.json()