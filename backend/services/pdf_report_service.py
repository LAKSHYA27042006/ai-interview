from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import os


class PDFReportService:

    def generate_report(
        self,
        result,
        output_path
    ):

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        doc = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "AI Interview Evaluation Report",
                styles["Title"]
            )
        )

        content.append(Spacer(1, 20))

        content.append(
            Paragraph(
                f"Overall Score: {result.overall_score}",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Recommendation: {result.recommendation}",
                styles["Normal"]
            )
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Communication Metrics",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Word Count: {result.communication.word_count}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Words Per Minute: {result.communication.words_per_minute}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Vocabulary Score: {result.communication.vocabulary_score}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Filler Words: {result.communication.filler_words}",
                styles["Normal"]
            )
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Vision Metrics",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Eye Contact Score: {result.vision.eye_contact_score}",
                styles["Normal"]
            )
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Audio Metrics",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Average Volume: {result.audio.average_volume}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Average Pitch: {result.audio.average_pitch}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Pitch Variation: {result.audio.pitch_variation}",
                styles["Normal"]
            )
        )

        doc.build(content)

        return output_path