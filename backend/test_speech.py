from services.speech_service import SpeechService

speech = SpeechService("base")

result = speech.transcribe_audio(
    "../dataset/processed/audio/interview_01.wav",
    "../dataset/processed/interview_01/transcript"
)

print("\n========== TRANSCRIPTION COMPLETED ==========")
print(f"Language : {result['language']}")
print(f"Transcript saved at : {result['txt_path']}")
print(f"JSON saved at : {result['json_path']}")
print("\nFirst 500 characters:\n")
print(result["text"][:500])