class FeedbackService:

    @staticmethod
    def generate_feedback(
        eye_contact_score,
        words_per_minute,
        vocabulary_score
    ):

        strengths = []
        improvements = []

        if eye_contact_score >= 75:
            strengths.append(
                "Maintains strong eye contact"
            )
        else:
            improvements.append(
                "Improve eye contact during conversation"
            )

        if 120 <= words_per_minute <= 170:
            strengths.append(
                "Good speaking pace"
            )
        else:
            improvements.append(
                "Maintain a more consistent speaking pace"
            )

        if vocabulary_score >= 0.6:
            strengths.append(
                "Uses strong vocabulary"
            )
        else:
            improvements.append(
                "Use more professional vocabulary"
            )

        feedback = (
            "Strengths: "
            + ", ".join(strengths)
            + " | Improvements: "
            + ", ".join(improvements)
        )

        return feedback