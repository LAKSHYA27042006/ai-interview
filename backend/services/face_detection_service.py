import os
import json
import cv2
import mediapipe as mp


class FaceDetectionService:

    def __init__(self, confidence=0.5):

        self.mp_face_detection = mp.solutions.face_detection

        self.face_detector = self.mp_face_detection.FaceDetection(
            model_selection=1,
            min_detection_confidence=confidence
        )

    def detect_faces(
        self,
        frames_folder,
        output_folder,
        metadata_folder
    ):

        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(metadata_folder, exist_ok=True)

        metadata = []

        frame_files = sorted(os.listdir(frames_folder))

        print(f"\nProcessing {len(frame_files)} frames...\n")

        for frame_name in frame_files:

            frame_path = os.path.join(
                frames_folder,
                frame_name
            )

            image = cv2.imread(frame_path)

            if image is None:
                continue

            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            results = self.face_detector.process(rgb)

            frame_data = {
                "frame": frame_name,
                "face_detected": False,
                "confidence": 0,
                "bounding_box": None
            }

            if results.detections:

                for detection in results.detections:

                    bbox = detection.location_data.relative_bounding_box

                    h, w, _ = image.shape

                    x = int(bbox.xmin * w)
                    y = int(bbox.ymin * h)
                    width = int(bbox.width * w)
                    height = int(bbox.height * h)

                    confidence = round(
                        detection.score[0],
                        3
                    )

                    frame_data = {

                        "frame": frame_name,

                        "face_detected": True,

                        "confidence": confidence,

                        "bounding_box": {

                            "x": x,
                            "y": y,
                            "width": width,
                            "height": height
                        }

                    }

                    cv2.rectangle(
                        image,
                        (x, y),
                        (x + width, y + height),
                        (0, 255, 0),
                        2
                    )

                    cv2.putText(
                        image,
                        f"{confidence:.2f}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2
                    )

            metadata.append(frame_data)

            cv2.imwrite(
                os.path.join(output_folder, frame_name),
                image
            )

        metadata_path = os.path.join(
            metadata_folder,
            "face_detection.json"
        )

        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=4)

        print("Face Detection Completed")

        print(f"Metadata Saved : {metadata_path}")

        return metadata