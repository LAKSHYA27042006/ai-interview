import os

from models.analysis_result import InterviewResult

from services.audio_service import AudioExtractor
from services.frame_service import FrameExtractionService
from services.speech_service import SpeechService
from services.communication_analysis_service import CommunicationAnalysisService
from services.face_detection_service import FaceDetectionService
from services.face_mesh_service import FaceMeshService
from services.head_pose_service import HeadPoseService
from services.eye_contact_service import EyeContactService
from services.voice_analysis_service import VoiceAnalysisService
from services.confidence_score_service import ConfidenceScoreService


class InterviewPipeline:

    def __init__(self):

        self.audio_service = AudioExtractor()

        self.frame_service = FrameExtractionService()

        self.speech_service = SpeechService()

        self.communication_service = (
            CommunicationAnalysisService()
        )

        self.face_detection_service = (
            FaceDetectionService()
        )

        self.face_mesh_service = (
            FaceMeshService()
        )

        self.head_pose_service = (
            HeadPoseService()
        )

        self.eye_contact_service = (
            EyeContactService()
        )

        self.voice_service = (
            VoiceAnalysisService()
        )

        self.confidence_service = (
            ConfidenceScoreService()
        )

    def analyze_interview(self, video_path):

        result = InterviewResult()

        print("\n==============================")
        print("AI Interview Analysis Started")
        print("==============================")

        try:

            video_name = os.path.splitext(
                os.path.basename(video_path)
            )[0]

            base_folder = os.path.join(
                "../storage/processed",
                video_name
            )

            audio_folder = os.path.join(
                base_folder,
                "audio"
            )

            transcript_folder = os.path.join(
                base_folder,
                "transcript"
            )

            frames_folder = os.path.join(
                base_folder,
                "frames"
            )

            face_mesh_frames_folder = os.path.join(
                base_folder,
                "face_mesh_frames"
            )

            metadata_folder = os.path.join(
                base_folder,
                "metadata"
            )

            os.makedirs(
                base_folder,
                exist_ok=True
            )

            print("\nStep 1 : Audio Extraction")

            audio_path = (
                self.audio_service.extract_audio(
                    video_path,
                    audio_folder
                )
            )

            print("\nStep 2 : Frame Extraction")

            self.frame_service.extract_frames(
                video_path,
                frames_folder
            )

            print("\nStep 3 : Face Mesh Generation")

            self.face_mesh_service.process_frames(
                frames_folder,
                face_mesh_frames_folder,
                metadata_folder
            )

            face_mesh_json = os.path.join(
                metadata_folder,
                "face_mesh.json"
            )

            print("\nStep 4 : Speech Recognition")

            transcript_result = (
                self.speech_service.transcribe_audio(
                    audio_path,
                    transcript_folder
                )
            )

            print(
                f"Language Detected: "
                f"{transcript_result['language']}"
            )

            print("\nStep 5 : Communication Analysis")

            communication_metrics = (
                self.communication_service.analyze(
                    transcript_result["json_path"]
                )
            )

            result.communication.language = (
                communication_metrics["language"]
            )

            result.communication.word_count = (
                communication_metrics["word_count"]
            )

            result.communication.sentence_count = (
                communication_metrics["sentence_count"]
            )

            result.communication.duration_seconds = (
                communication_metrics[
                    "duration_seconds"
                ]
            )

            result.communication.words_per_minute = (
                communication_metrics[
                    "words_per_minute"
                ]
            )

            result.communication.vocabulary_score = (
                communication_metrics[
                    "vocabulary_score"
                ]
            )

            result.communication.filler_words = (
                communication_metrics[
                    "total_filler_words"
                ]
            )

            print(
                f"Words: "
                f"{communication_metrics['word_count']}"
            )

            print(
                f"WPM: "
                f"{communication_metrics['words_per_minute']}"
            )

            print(
                f"Vocabulary Score: "
                f"{communication_metrics['vocabulary_score']}"
            )

            print(
                f"Filler Words: "
                f"{communication_metrics['total_filler_words']}"
            )

            print("\nStep 6 : Head Pose Analysis")

            head_pose_results = (
                self.head_pose_service
                .estimate_head_pose(
                    face_mesh_json
                )
            )

            print(
                f"Head Pose Frames Processed: "
                f"{len(head_pose_results)}"
            )

            print("\nStep 7 : Eye Contact Analysis")

            eye_contact_result = (
                self.eye_contact_service
                .analyze_eye_contact(
                    head_pose_results
                )
            )

            result.vision.eye_contact_score = (
                eye_contact_result[
                    "eye_contact_score"
                ]
            )

            result.vision.total_frames = (
                eye_contact_result[
                    "total_frames"
                ]
            )

            print(
                f"Eye Contact Score: "
                f"{eye_contact_result['eye_contact_score']}%"
            )

            print("\nStep 8 : Voice Analysis")

            voice_metrics = (
                self.voice_service
                .analyze_voice(
                    audio_path
                )
            )

            result.audio.average_volume = (
                voice_metrics["avg_energy"]
            )

            result.audio.average_pitch = (
                voice_metrics["avg_pitch"]
            )

            result.audio.pitch_variation = (
                voice_metrics[
                    "pitch_variation"
                ]
            )

            result.audio.duration_seconds = (
                voice_metrics["duration"]
            )

            print(
                f"Average Energy: "
                f"{voice_metrics['avg_energy']}"
            )

            print(
                f"Average Pitch: "
                f"{voice_metrics['avg_pitch']}"
            )

            print(
                f"Pitch Variation: "
                f"{voice_metrics['pitch_variation']}"
            )

            print("\nStep 9 : Confidence Score")

            confidence_score = (
                self.confidence_service
                .calculate_score(
                    eye_contact_score=
                    eye_contact_result[
                        "eye_contact_score"
                    ],

                    words_per_minute=
                    communication_metrics[
                        "words_per_minute"
                    ],

                    vocabulary_score=
                    communication_metrics[
                        "vocabulary_score"
                    ],

                    filler_words=
                    communication_metrics[
                        "total_filler_words"
                    ],

                    avg_energy=
                    voice_metrics[
                        "avg_energy"
                    ],

                    pitch_variation=
                    voice_metrics[
                        "pitch_variation"
                    ]
                )
            )

            result.overall_score = (
                confidence_score
            )

            result.vision.confidence_score = (
                confidence_score
            )

            result.recommendation = (
                f"Confidence Score: "
                f"{confidence_score}/100"
            )

            print(
                f"Confidence Score: "
                f"{confidence_score}"
            )

            print("\n==============================")
            print("Pipeline Completed")
            print("==============================")

            return result

        except Exception as e:

            print(
                f"\nPipeline Error: "
                f"{str(e)}"
            )

            result.recommendation = (
                f"Pipeline failed: "
                f"{str(e)}"
            )

            return result