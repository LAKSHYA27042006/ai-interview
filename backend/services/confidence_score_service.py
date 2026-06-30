class ConfidenceScoreService:

    def calculate_score(
        self,
        eye_contact_score,
        words_per_minute,
        vocabulary_score,
        filler_words,
        avg_energy,
        pitch_variation
    ):

        score = 0

        # Eye Contact (30 points)
        score += min(
            eye_contact_score * 0.30,
            30
        )

        # Speaking Speed (20 points)

        if 110 <= words_per_minute <= 170:
            score += 20
        elif 90 <= words_per_minute <= 200:
            score += 15
        else:
            score += 8

        # Vocabulary (20 points)

        score += min(
            vocabulary_score * 20,
            20
        )

        # Filler Words (10 points)

        if filler_words <= 5:
            score += 10
        elif filler_words <= 10:
            score += 7
        else:
            score += 3

        # Voice Energy (10 points)

        if avg_energy > 0.05:
            score += 10
        else:
            score += 5

        # Pitch Variation (10 points)

        if pitch_variation > 20:
            score += 10
        else:
            score += 5

        return round(score, 2)