from services.voice_analysis_service import VoiceAnalysisService

voice_service = VoiceAnalysisService()

result = voice_service.analyze_voice(
    "../dataset/processed/interview_01/audio/interview_01.wav"
)

print(result)