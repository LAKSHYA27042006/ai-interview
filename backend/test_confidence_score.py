from services.confidence_score_service import ConfidenceScoreService

service = ConfidenceScoreService()

score = service.calculate_score(
    eye_contact_score=62.33,
    words_per_minute=140,
    vocabulary_score=0.72,
    filler_words=3,
    avg_energy=0.1109,
    pitch_variation=638.48
)

print("Confidence Score:", score)