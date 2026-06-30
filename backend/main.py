from fastapi import FastAPI

from api.interview import router

app = FastAPI(
    title="AI Interview Evaluation System"
)

app.include_router(router)