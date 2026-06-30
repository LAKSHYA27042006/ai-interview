from services.head_pose_service import HeadPoseService
from services.eye_contact_service import EyeContactService

head_pose_service = HeadPoseService()

head_pose_results = head_pose_service.estimate_head_pose(
    "../dataset/processed/interview_01/metadata/face_mesh.json"
)

eye_contact_service = EyeContactService()

result = eye_contact_service.analyze_eye_contact(
    head_pose_results
)

print(result)