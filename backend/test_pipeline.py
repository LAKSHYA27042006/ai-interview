from services.interview_pipeline import InterviewPipeline

pipeline = InterviewPipeline()

result = pipeline.analyze_interview(
    "../dataset/raw_videos/interview_01.mp4"
)

print(result)