import json

from services.head_pose_service import HeadPoseService


with open(
    "../dataset/processed/interview_01/metadata/face_mesh.json",
    "r"
) as f:
    data = json.load(f)

print("Face Mesh Records:", len(data))

if len(data) > 0:
    print("Landmarks in first frame:", len(data[0]["landmarks"]))

head_pose_service = HeadPoseService()

results = head_pose_service.estimate_head_pose(
    "../dataset/processed/interview_01/metadata/face_mesh.json"
)

print("Results Length:", len(results))

if len(results) > 0:
    print("Sample Result:")
    print(results[0])
else:
    print("No head pose results generated")