import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api import get_all_interviews

st.set_page_config(
    page_title="AI Interview Evaluation System",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Evaluation System")

st.markdown(
    "AI-powered candidate interview assessment using Computer Vision and NLP"
)

st.divider()

try:

    interviews = get_all_interviews()

    total_interviews = len(interviews)

    avg_score = (
        round(
            sum(i["overall_score"] for i in interviews)
            / total_interviews,
            2
        )
        if total_interviews > 0
        else 0
    )

    recommended_count = len(
        [
            i for i in interviews
            if i["recommendation"] == "Recommended"
        ]
    )

    top_score = (
        max(
            [i["overall_score"] for i in interviews]
        )
        if interviews
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Interviews",
        total_interviews
    )

    col2.metric(
        "Average Score",
        avg_score
    )

    col3.metric(
        "Recommended",
        recommended_count
    )

    col4.metric(
        "Highest Score",
        top_score
    )

    st.divider()

    if interviews:

        st.subheader("🏆 Candidate Leaderboard")

        leaderboard = pd.DataFrame(
            sorted(
                [
                    {
                        "Candidate": i["candidate_name"],
                        "Score": i["overall_score"],
                        "Recommendation": i["recommendation"]
                    }
                    for i in interviews
                ],
                key=lambda x: x["Score"],
                reverse=True
            )
        )

        st.dataframe(
            leaderboard,
            use_container_width=True
        )

        st.divider()

        st.subheader("📈 Candidate Performance")

        fig = px.bar(
            leaderboard,
            x="Candidate",
            y="Score",
            title="Overall Candidate Scores"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        st.subheader("📋 Recent Interviews")

        recent_df = pd.DataFrame([
            {
                "Candidate": i["candidate_name"],
                "Score": i["overall_score"],
                "Recommendation": i["recommendation"]
            }
            for i in interviews[-5:]
        ])

        st.dataframe(
            recent_df,
            use_container_width=True
        )

    else:

        st.info(
            "No interview records found. Upload an interview to get started."
        )

except Exception as e:

    st.error(
        f"Unable to connect to backend: {str(e)}"
    )

