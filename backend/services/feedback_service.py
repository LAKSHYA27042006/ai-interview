from groq import Groq


class FeedbackService:

    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def generate_feedback(
        self,
        communication_metrics,
        eye_contact_score,
        voice_metrics,
        confidence_score
    ):

        prompt = f"""
You are a senior technical recruiter.

Analyze the interview metrics and provide:

1. Strengths
2. Areas for Improvement
3. Overall Assessment
4. Interview Readiness Score (/100)

Metrics:

Words Per Minute: {communication_metrics['words_per_minute']}
Vocabulary Score: {communication_metrics['vocabulary_score']}
Filler Words: {communication_metrics['filler_words']}

Eye Contact Score: {eye_contact_score}

Average Pitch: {voice_metrics['avg_pitch']}
Pitch Variation: {voice_metrics['pitch_variation']}
Voice Energy: {voice_metrics['avg_energy']}

Confidence Score: {confidence_score}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content