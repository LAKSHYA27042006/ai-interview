from moviepy import VideoFileClip
import os


class AudioExtractor:

    def __init__(self):
        pass

    def extract_audio(self, video_path, output_folder):

        os.makedirs(output_folder, exist_ok=True)

        filename = os.path.splitext(os.path.basename(video_path))[0]

        output_path = os.path.join(
            output_folder,
            f"{filename}.wav"
        )

        print(f"Reading Video : {video_path}")
        print(f"Saving Audio  : {output_path}")

        video = VideoFileClip(video_path)

        video.audio.write_audiofile(
            output_path,
            codec="pcm_s16le"
        )

        video.close()

        print("✅ Audio Extraction Completed")

        return output_path