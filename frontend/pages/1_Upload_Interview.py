import streamlit as st
from utils.api import upload_video

st.set_page_config(
    page_title="Upload Interview",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Upload Interview Video")

st.markdown("""
Upload a candidate interview video and let the AI evaluate:

- Eye Contact
- Vocabulary Usage
- Speaking Rate
- Overall Performance
- Hiring Recommendation
""")

st.divider()

uploaded_video = st.file_uploader(
    "Choose Interview Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video:

    st.subheader("📹 Video Preview")

    st.video(uploaded_video)

    st.info(
        f"Selected File: {uploaded_video.name}"
    )

    if st.button(
        "🚀 Analyze Interview",
        use_container_width=True
    ):

        try:

            with st.spinner(
                "AI is analyzing the interview..."
            ):

                response = upload_video(
                    uploaded_video
                )

            st.success(
                "Interview analyzed successfully!"
            )

            st.balloons()

            # Extract analysis data
            analysis = response["analysis"]

            st.subheader("📊 Interview Summary")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Overall Score",
                analysis["overall_score"]
            )

            col2.metric(
                "Eye Contact Score",
                analysis["vision"]["eye_contact_score"]
            )

            col3.metric(
                "Vocabulary Score",
                analysis["communication"]["vocabulary_score"]
            )

            st.divider()

            st.info(
                "Go to the 'Interview Results Dashboard' page to view detailed results and download the PDF report."
            )

        except Exception as e:

            st.error(
                f"Analysis Failed: {str(e)}"
            )

else:

    st.warning(
        "Please upload an interview video."
    )