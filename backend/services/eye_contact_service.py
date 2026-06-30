import json


class EyeContactService:

    def analyze_eye_contact(self, head_pose_results):

        total_frames = len(head_pose_results)

        if total_frames == 0:
            return {
                "eye_contact_score": 0,
                "forward_frames": 0,
                "total_frames": 0
            }

        forward_frames = sum(
            1 for frame in head_pose_results
            if frame["looking_forward"]
        )

        eye_contact_score = (
            forward_frames / total_frames
        ) * 100

        return {
            "eye_contact_score": round(
                eye_contact_score,
                2
            ),
            "forward_frames": forward_frames,
            "total_frames": total_frames
        }