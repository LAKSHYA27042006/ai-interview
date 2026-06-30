import os

from services.feedback_service import FeedbackService

service = FeedbackService(
    api_key=os.getenv("GROQ_API_KEY")
)

feedback = service.generate_feedback(
    communication_metrics={
        "words_per_minute": 145,
        "vocabulary_score": 0.74,
        "filler_words": 4
    },
    eye_contact_score=62.33,
    voice_metrics={
        "avg_pitch": 885.53,
        "pitch_variation": 638.48,
        "avg_energy": 0.1109
    },
    confidence_score=82
)

print(feedback)