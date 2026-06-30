from deepface import DeepFace
import cv2
import os


class EmotionService:

    def analyze_emotions(self, frames_folder):

        emotion_counts = {}

        frame_files = sorted(os.listdir(frames_folder))

        processed_frames = 0

        for frame_name in frame_files[::30]:
            # Analyze every 30th frame for speed

            frame_path = os.path.join(
                frames_folder,
                frame_name
            )

            try:

                result = DeepFace.analyze(
                    img_path=frame_path,
                    actions=["emotion"],
                    enforce_detection=False
                )

                emotion = result[0]["dominant_emotion"]

                emotion_counts[emotion] = (
                    emotion_counts.get(emotion, 0) + 1
                )

                processed_frames += 1

            except Exception:
                continue

        if not emotion_counts:

            return {
                "dominant_emotion": "Unknown",
                "emotion_distribution": {}
            }

        dominant_emotion = max(
            emotion_counts,
            key=emotion_counts.get
        )

        return {
            "dominant_emotion": dominant_emotion,
            "emotion_distribution": emotion_counts,
            "frames_processed": processed_frames
        }