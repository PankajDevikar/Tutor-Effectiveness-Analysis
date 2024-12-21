import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r'C:\data science material\my project\project_7\notebook\data\tutor_effectiveness_analysis.csv')


# Group data by tutor for performance analysis
tutor_performance = df.groupby('Tutor_Name').agg(
    average_engagement_score=('Engagement_Score', 'mean'),
    average_outcome_score=('Outcome_Score', 'mean'),
    average_feedback_score=('Feedback_Score', 'mean'),
    session_count=('Student_ID', 'count')
).reset_index()

# Title and Sidebar Header
st.title("📊 **Tutor Effectiveness Analysis Dashboard**")
st.sidebar.header("Select Metrics to Visualize")

# Sidebar options for choosing the metric
metric = st.sidebar.selectbox(
    "Choose Metric to Analyze",
    ("Engagement Score", "Outcome Score", "Feedback Score")
)

# Sidebar - Add a description or additional analysis
st.sidebar.markdown("""
This dashboard provides insights into tutor effectiveness based on different metrics:
- **Engagement Score**: Measures how engaged students are during the sessions.
- **Outcome Score**: Indicates student success after sessions.
- **Feedback Score**: Reflects the students' satisfaction.
""")

# Function to display the selected plot
def display_plot(metric):
    # Set the plot style
    sns.set(style="whitegrid")
    
    if metric == "Engagement Score":
        st.subheader("📊 **Average Engagement Score by Tutor**")
        fig, ax = plt.subplots(figsize=(10, 6))
        plot = sns.barplot(x='Tutor_Name', y='average_engagement_score', data=tutor_performance, palette='coolwarm')
        ax.set_title('Average Engagement Score by Tutor', fontsize=16)
        ax.set_xlabel('Tutor', fontsize=12)
        ax.set_ylabel('Average Engagement Score', fontsize=12)
        st.pyplot(fig)
    
    elif metric == "Outcome Score":
        st.subheader("📊 **Average Outcome Score by Tutor**")
        fig, ax = plt.subplots(figsize=(10, 6))
        plot = sns.barplot(x='Tutor_Name', y='average_outcome_score', data=tutor_performance, palette='Blues')
        ax.set_title('Average Outcome Score by Tutor', fontsize=16)
        ax.set_xlabel('Tutor', fontsize=12)
        ax.set_ylabel('Average Outcome Score', fontsize=12)
        st.pyplot(fig)
    
    elif metric == "Feedback Score":
        st.subheader("📊 **Average Feedback Score by Tutor**")
        fig, ax = plt.subplots(figsize=(10, 6))
        plot = sns.barplot(x='Tutor_Name', y='average_feedback_score', data=tutor_performance, palette='Purples')
        ax.set_title('Average Feedback Score by Tutor', fontsize=16)
        ax.set_xlabel('Tutor', fontsize=12)
        ax.set_ylabel('Average Feedback Score', fontsize=12)
        st.pyplot(fig)

# Display the selected plot
display_plot(metric)

# Footer Section with Additional Information
st.markdown("""
---
### 📚 **About the Data**
The dataset includes 1000 records of student-tutor sessions, capturing various aspects such as engagement, outcomes, and feedback for each session. This analysis helps assess the effectiveness of tutors based on student performance and satisfaction.

### ✨ **Key Insights**
- Compare engagement, outcome, and feedback scores across different tutors.
- Visualize how tutor effectiveness impacts student success.

**Developed by:** Pankaj Devikar
""")
