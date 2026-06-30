from pydantic import BaseModel


class InterviewResponse(BaseModel):

    status: str

    message: str

    interview_id: str