from services.emotion_service import EmotionService

emotion_service = EmotionService()

result = emotion_service.analyze_emotions(
    "../dataset/processed/interview_01/frames"
)

print(result)