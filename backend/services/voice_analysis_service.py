import librosa
import numpy as np


class VoiceAnalysisService:

    def analyze_voice(self, audio_path):

        y, sr = librosa.load(audio_path)

        duration = librosa.get_duration(
            y=y,
            sr=sr
        )

        rms = librosa.feature.rms(y=y)[0]

        avg_energy = float(np.mean(rms))

        pitches, magnitudes = librosa.piptrack(
            y=y,
            sr=sr
        )

        pitch_values = []

        for i in range(pitches.shape[0]):
            for j in range(pitches.shape[1]):

                pitch = pitches[i][j]

                if pitch > 0:
                    pitch_values.append(pitch)

        avg_pitch = (
            float(np.mean(pitch_values))
            if pitch_values
            else 0
        )

        pitch_variation = (
            float(np.std(pitch_values))
            if pitch_values
            else 0
        )

        return {
            "duration": round(duration, 2),
            "avg_energy": round(avg_energy, 4),
            "avg_pitch": round(avg_pitch, 2),
            "pitch_variation": round(
                pitch_variation,
                2
            )
        }