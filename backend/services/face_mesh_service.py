import os
import json
import cv2
import mediapipe as mp


class FaceMeshService:

    def __init__(self):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )

    def process_frames(
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

            rgb = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2RGB
            )

            results = self.face_mesh.process(rgb)

            frame_info = {

                "frame": frame_name,

                "face_found": False,

                "landmarks": []

            }

            if results.multi_face_landmarks:

                frame_info["face_found"] = True

                face_landmarks = results.multi_face_landmarks[0]

                h, w, _ = image.shape

                for landmark in face_landmarks.landmark:

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    frame_info["landmarks"].append(
                        {
                            "x": x,
                            "y": y
                        }
                    )

                    cv2.circle(
                        image,
                        (x, y),
                        1,
                        (0, 255, 0),
                        -1
                    )

            metadata.append(frame_info)

            cv2.imwrite(
                os.path.join(output_folder, frame_name),
                image
            )

        metadata_path = os.path.join(
            metadata_folder,
            "face_mesh.json"
        )

        with open(metadata_path, "w") as file:

            json.dump(
                metadata,
                file,
                indent=4
            )

        print("\nFace Mesh Completed")

        print(f"Metadata saved at : {metadata_path}")

        return metadata