import json
import numpy as np
import cv2


class HeadPoseService:

    def __init__(self):

        self.landmark_ids = {
            "nose": 1,
            "chin": 152,
            "left_eye": 33,
            "right_eye": 263,
            "mouth_left": 61,
            "mouth_right": 291
        }

    def estimate_head_pose(self, face_mesh_json):

        with open(face_mesh_json, "r") as file:
            frames = json.load(file)

        results = []

        for frame_data in frames:

            if not frame_data.get("face_found", False):
                continue

            landmarks = frame_data["landmarks"]

            try:

                image_points = np.array([
                    (
                        landmarks[self.landmark_ids["nose"]]["x"],
                        landmarks[self.landmark_ids["nose"]]["y"]
                    ),
                    (
                        landmarks[self.landmark_ids["chin"]]["x"],
                        landmarks[self.landmark_ids["chin"]]["y"]
                    ),
                    (
                        landmarks[self.landmark_ids["left_eye"]]["x"],
                        landmarks[self.landmark_ids["left_eye"]]["y"]
                    ),
                    (
                        landmarks[self.landmark_ids["right_eye"]]["x"],
                        landmarks[self.landmark_ids["right_eye"]]["y"]
                    ),
                    (
                        landmarks[self.landmark_ids["mouth_left"]]["x"],
                        landmarks[self.landmark_ids["mouth_left"]]["y"]
                    ),
                    (
                        landmarks[self.landmark_ids["mouth_right"]]["x"],
                        landmarks[self.landmark_ids["mouth_right"]]["y"]
                    )
                ], dtype=np.float64)

                model_points = np.array([
                    (0.0, 0.0, 0.0),
                    (0.0, -330.0, -65.0),
                    (-225.0, 170.0, -135.0),
                    (225.0, 170.0, -135.0),
                    (-150.0, -150.0, -125.0),
                    (150.0, -150.0, -125.0)
                ], dtype=np.float64)

                width = 640
                height = 480

                focal_length = width

                camera_matrix = np.array([
                    [focal_length, 0, width / 2],
                    [0, focal_length, height / 2],
                    [0, 0, 1]
                ], dtype=np.float64)

                dist_coeffs = np.zeros((4, 1))

                success, rotation_vector, translation_vector = cv2.solvePnP(
                    model_points,
                    image_points,
                    camera_matrix,
                    dist_coeffs,
                    flags=cv2.SOLVEPNP_ITERATIVE
                )

                if not success:
                    continue

                rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

                pose_matrix = cv2.hconcat(
                    (rotation_matrix, translation_vector)
                )

                _, _, _, _, _, _, euler_angles = cv2.decomposeProjectionMatrix(
                    pose_matrix
                )

                euler_angles = euler_angles.flatten()

                pitch = float(euler_angles[0])
                yaw = float(euler_angles[1])
                roll = float(euler_angles[2])

                looking_forward = abs(yaw) < 30

                results.append({
                    "frame": frame_data["frame"],
                    "yaw": round(yaw, 2),
                    "pitch": round(pitch, 2),
                    "roll": round(roll, 2),
                    "looking_forward": looking_forward
                })

            except Exception as e:

                print(
                    f"Error in frame "
                    f"{frame_data['frame']}: {e}"
                )

                continue

        print(f"\nFrames Processed: {len(results)}")

        return results