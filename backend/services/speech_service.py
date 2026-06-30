import os
import json
import whisper


class SpeechService:

    def __init__(self, model_name="base"):
        """
        Load the Whisper model once when the service starts.
        """
        print(f"Loading Whisper model: {model_name}")
        self.model = whisper.load_model(model_name)
        print("Whisper model loaded successfully.")

    def transcribe_audio(self, audio_path, output_folder):
        """
        Transcribe audio and save the results.
        """

        os.makedirs(output_folder, exist_ok=True)

        result = self.model.transcribe(audio_path)

        transcript_txt = os.path.join(output_folder, "transcript.txt")
        transcript_json = os.path.join(output_folder, "transcript.json")

        # Save plain text
        with open(transcript_txt, "w", encoding="utf-8") as f:
            f.write(result["text"])

        # Save complete JSON output
        with open(transcript_json, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        return {
            "language": result["language"],
            "text": result["text"],
            "segments": result["segments"],
            "txt_path": transcript_txt,
            "json_path": transcript_json,
        }