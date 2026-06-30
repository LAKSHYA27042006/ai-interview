from services.face_detection_service import FaceDetectionService

service = FaceDetectionService()

result = service.detect_faces(

    "../dataset/processed/interview_01/frames",

    "../dataset/processed/interview_01/faces",

    "../dataset/processed/interview_01/metadata"

)

print(f"\nFrames Processed : {len(result)}")