import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api import get_all_interviews

st.set_page_config(
    page_title="Candidate Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Candidate Analytics")

results = get_all_interviews()

if not results:
    st.warning("No interview data available.")
else:

    df = pd.DataFrame([
        {
            "Candidate": r["candidate_name"],
            "Score": r["overall_score"],
            "Recommendation": r["recommendation"]
        }
        for r in results
    ])

    st.subheader("Score Distribution")

    fig1 = px.histogram(
        df,
        x="Score",
        nbins=10,
        title="Interview Score Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader("Recommendation Breakdown")

    recommendation_counts = (
        df["Recommendation"]
        .value_counts()
        .reset_index()
    )

    recommendation_counts.columns = [
        "Recommendation",
        "Count"
    ]

    fig2 = px.pie(
        recommendation_counts,
        values="Count",
        names="Recommendation",
        title="Recommendation Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )