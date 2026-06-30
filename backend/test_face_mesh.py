from services.face_mesh_service import FaceMeshService

service = FaceMeshService()

result = service.process_frames(

    "../dataset/processed/interview_01/frames",

    "../dataset/processed/interview_01/face_mesh",

    "../dataset/processed/interview_01/metadata"

)

print()

print(f"Frames Processed : {len(result)}")