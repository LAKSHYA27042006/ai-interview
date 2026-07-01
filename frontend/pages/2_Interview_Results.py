import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api import (
    get_all_interviews,
    get_interview_details
)

st.set_page_config(
    page_title="Interview Results",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interview Results Dashboard")

try:

    results = get_all_interviews()

    if not results:

        st.warning("No interview results found.")

    else:

        # Search Candidate

        search = st.text_input(
            "🔍 Search Candidate"
        )

        if search:

            results = [
                r for r in results
                if search.lower()
                in r["candidate_name"].lower()
            ]

        # DataFrame

        df = pd.DataFrame([
            {
                "ID": r["id"],
                "Candidate": r["candidate_name"],
                "Score": r["overall_score"],
                "Recommendation": r["recommendation"]
            }
            for r in results
        ])

        st.subheader("Candidate Summary")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        # Candidate Score Chart

        st.subheader("📈 Candidate Score Comparison")

        chart_df = pd.DataFrame([
            {
                "Candidate": r["candidate_name"],
                "Score": r["overall_score"]
            }
            for r in results
        ])

        fig = px.bar(
            chart_df,
            x="Candidate",
            y="Score",
            title="Overall Candidate Scores"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # Automatically show latest interview
        latest_interview_id = df.iloc[-1]["ID"]
        details = get_interview_details(
            int(latest_interview_id)
            )

        

        st.subheader("🎯 Candidate Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Overall Score",
            details["overall_score"]
        )

        col2.metric(
            "Eye Contact",
            details["eye_contact_score"]
        )

        col3.metric(
            "Vocabulary",
            details["vocabulary_score"]
        )

        st.divider()

        # Recommendation

        st.subheader("✅ Recommendation")

        if (
            details["recommendation"]
            == "Recommended"
        ):
            st.success(
                details["recommendation"]
            )
        else:
            st.warning(
                details["recommendation"]
            )

        st.divider()

        # Feedback

        st.subheader("💡 AI Feedback")

        st.info(
            details["feedback"]
        )

        st.divider()

        # PDF Download

        pdf_url = (
    f"http://127.0.0.1:8000/"
    f"download-report/{latest_interview_id}"
)

        st.link_button(
            "📄 Download PDF Report",
            pdf_url
        )

except Exception as e:

    st.error(
        f"Error connecting to backend: {str(e)}"
    )