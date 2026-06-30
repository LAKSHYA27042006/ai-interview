from services.audio_service import AudioExtractor

extractor = AudioExtractor()

audio_path = extractor.extract_audio(
    "../dataset/raw_videos/interview_01.mp4",
    "../dataset/processed/audio"
)

print(audio_path)