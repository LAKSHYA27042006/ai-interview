from services.frame_service import FrameExtractionService

service = FrameExtractionService()

result = service.extract_frames(
    "../dataset/raw_videos/interview_01.mp4",
    "../dataset/processed/interview_01/frames",
    frame_interval=15
)

print(result)