from dataclasses import dataclass, field


@dataclass
class CommunicationMetrics:

    language: str = ""

    word_count: int = 0

    sentence_count: int = 0

    duration_seconds: float = 0

    words_per_minute: float = 0

    vocabulary_score: float = 0

    filler_words: int = 0


@dataclass
class VisionMetrics:

    total_frames: int = 0

    faces_detected: int = 0

    eye_contact_score: float = 0

    head_pose_score: float = 0

    smile_score: float = 0

    confidence_score: float = 0


@dataclass
class AudioMetrics:

    average_volume: float = 0

    pitch_variation: float = 0

    pause_count: int = 0


@dataclass
class InterviewResult:

    communication: CommunicationMetrics = field(
        default_factory=CommunicationMetrics
    )

    vision: VisionMetrics = field(
        default_factory=VisionMetrics
    )

    audio: AudioMetrics = field(
        default_factory=AudioMetrics
    )

    overall_score: float = 0

    recommendation: str = ""

    llm_feedback: str = ""