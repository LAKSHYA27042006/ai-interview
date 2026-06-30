from models.analysis_result import InterviewResult

from services.audio_service import AudioExtractor
from services.frame_service import FrameExtractionService
from services.speech_service import SpeechService
from services.communication_analysis_service import CommunicationAnalysisService
from services.face_detection_service import FaceDetectionService
from services.face_mesh_service import FaceMeshService
from services.head_pose_service import HeadPoseService
from services.eye_contact_service import EyeContactService


class InterviewPipeline:

    def __init__(self):

        self.audio_service = AudioExtractor()

        self.frame_service = FrameExtractionService()

        self.speech_service = SpeechService()

        self.communication_service = CommunicationAnalysisService()

        self.face_detection_service = FaceDetectionService()

        self.face_mesh_service = FaceMeshService()

        self.head_pose_service = HeadPoseService()

        self.eye_contact_service = EyeContactService()

    def analyze_interview(self, video_path):

        result = InterviewResult()

        print("\n==============================")
        print("AI Interview Analysis Started")
        print("==============================")

        try:

            print("\nStep 1 : Audio Extraction")

            print("\nStep 2 : Frame Extraction")

            print("\nStep 3 : Speech Recognition")

            print("\nStep 4 : Communication Analysis")

            print("\nStep 5 : Face Detection")

            print("\nStep 6 : Face Mesh")

            print("\nStep 7 : Head Pose")

            face_mesh_json = (
                "../dataset/processed/interview_01/metadata/face_mesh.json"
            )

            head_pose_results = (
                self.head_pose_service
                .estimate_head_pose(face_mesh_json)
            )

            print(
                f"Head Pose Frames Processed: "
                f"{len(head_pose_results)}"
            )

            print("\nStep 8 : Eye Contact Detection")

            eye_contact_result = (
                self.eye_contact_service
                .analyze_eye_contact(head_pose_results)
            )

            result.vision.eye_contact_score = (
                eye_contact_result["eye_contact_score"]
            )

            result.vision.total_frames = (
                eye_contact_result["total_frames"]
            )

            result.recommendation = (
                f"Eye Contact Score: "
                f"{eye_contact_result['eye_contact_score']}%"
            )

            print(
                f"Eye Contact Score: "
                f"{eye_contact_result['eye_contact_score']}%"
            )

            print("\nPipeline Completed")

            return result

        except Exception as e:

            print(f"\nPipeline Error: {str(e)}")

            result.recommendation = (
                f"Pipeline failed: {str(e)}"
            )

            return result