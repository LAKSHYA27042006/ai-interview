# AI Interview Evaluation System

## Overview
AI-powered interview assessment platform that evaluates candidates using Computer Vision and Natural Language Processing.

## Features
- Interview Video Upload
- Eye Contact Detection
- Vocabulary Analysis
- Speaking Rate Analysis
- Candidate Scoring
- Recommendation Engine
- PDF Report Generation
- Historical Interview Dashboard

## Tech Stack
Backend:
- FastAPI
- SQLAlchemy
- SQLite

Frontend:
- Streamlit

AI/ML:
- OpenCV
- MediaPipe
- Whisper
- NLP Analysis

## APIs
POST /analyze-upload
GET /interviews
GET /interviews/{id}
GET /download-report/{id}

## Future Enhancements
- Facial Emotion Detection
- Confidence Analysis
- Multi-Candidate Comparison
- LLM-Based Interview Feedback