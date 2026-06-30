import os
import cv2


class FrameExtractionService:

    def extract_frames(
        self,
        video_path,
        output_folder,
        frame_interval=10
    ):
        """
        Extract frames from a video.

        Parameters
        ----------
        video_path : str
            Path to input video.

        output_folder : str
            Folder where extracted frames are saved.

        frame_interval : int
            Save one frame every N frames.
        """

        os.makedirs(output_folder, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise Exception(f"Cannot open video: {video_path}")

        fps = cap.get(cv2.CAP_PROP_FPS)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        duration = total_frames / fps

        print(f"\nFPS           : {fps:.2f}")
        print(f"Total Frames  : {total_frames}")
        print(f"Duration      : {duration:.2f} sec\n")

        frame_number = 0
        saved_frames = 0

        while True:

            success, frame = cap.read()

            if not success:
                break

            if frame_number % frame_interval == 0:

                filename = f"frame_{saved_frames:05d}.jpg"

                output_path = os.path.join(
                    output_folder,
                    filename
                )

                cv2.imwrite(output_path, frame)

                saved_frames += 1

            frame_number += 1

        cap.release()

        print("Frame Extraction Completed")
        print(f"Frames Saved : {saved_frames}")

        return {
            "fps": fps,
            "total_frames": total_frames,
            "duration": duration,
            "saved_frames": saved_frames
        }