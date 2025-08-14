import streamlit as st
import pandas as pd
st.set_page_config(page_title="OSMI Mental Health Analysis & Support Strategy Design for the Tech Workforce",page_icon="🧠", layout="wide")

st.title("🧠 OSMI Mental Health Data Analysis")

st.markdown("""
## Capstone Project 2025 | OpenLearn Cohort 1.0
            """)
st.markdown("""
Welcome to the interactive **Mental Health Analysis in Tech** web application.
Here we understand what the OSMI survey tell us about Mental Health in Tech

## 📄 Dataset Overview
- **Source:** Mental Health in Tech Survey  
- **Collected by:** [OSMI (Open Sourcing Mental Illness)](https://osmihelp.org)  
       
**Features:**
- 📊 **EDA:** Explore survey trends and insights into the cleaned dataset
- 🩺 **Treatment Prediction:** Predict if an employee will seek treatment or not
- 🎯 **Age Prediction:** Predict age of employee based on mental health & workplace features
- 👥 **Clustering Visualizer:** View user personas from clustering interpretation


""")

st.markdown("""
## 🧪 Project Case Study
While using this model, you'll consider yourself as a **Machine Learning Engineer** at *NeuronInsights Analytics* and you've been contracted by a coalition of leading tech companies including **CodeLab**, **QuantumEdge**, and **SynapseWorks**.  

**Roles:**
- Analyzing survey data from over **1,500 tech professionals**.  
- **Identifying risk patterns** based on various features.  
- Predicting whether a person **will seek treatment or not**.  
- Predicting **Age** of a person.  
""")

st.header("🔍 Key Questions Explored")

st.subheader("Q1. Who is most likely to suffer silently and avoid seeking treatment?")
st.markdown("""
**Answer:** Employees who are most likely to suffer silently and avoid seeking treatment are:

1. **Young Employees (Age 18-24):** According to the survey, this group reports high stress levels and are more likely to take leave due to mental health issues compared to older employees.
2. **Employees Without Mental Health Benefits:** Lack of access to mental health benefits results in untreated conditions, making employees hesitant to seek help.
3. **Workers with Limited Managerial Support:** Employees without adequate guidance on mental health conditions lack the courage to seek treatment.
4. **Remote Workers:** While remote work offers flexibility, it can lead to isolation and loneliness if not managed properly.
""")

st.subheader("Q2. How Do Factors Like Remote Work, Mental Health Benefits, and Managerial Support Influence Mental Well Being?")
st.markdown("""
**Answer:**

1. **Remote Work:** Reduces stress and workload but may increase isolation and burnout if not supported well. Lack of clear boundaries between work and personal life can worsen stress.
2. **Mental Health Benefits:** Access to mental health benefits is essential for seeking help and managing stress effectively.
3. **Managerial Support:** Clear communication, recognition, and flexibility from managers can significantly reduce stress and foster a positive environment.
""")

st.subheader("Q3. Can employee profiles be segmented to enable targeted outreach and HR intervention?")
st.markdown("""
**Answer:** Yes, employee profiles can be segmented to tailor mental health initiatives effectively:

1. **Demographic Segmentation:** Age, gender, and role can influence stress levels and treatment-seeking behaviour.
2. **Work Arrangement:** Remote workers may require more social interaction, while in-office employees may benefit from stress management workshops.
3. **Health Benefits Access:** Essential for seeking help and managing stress effectively.
4. **Managerial Support Levels:** High managerial support encourages employees to seek treatment.

**SOLUTION:** A data-driven approach using employee surveys, feedback, and analytics can help identify at-risk employees and design targeted interventions such as wellness programs and workshops.
""")

st.markdown(
    """<div style='text-align: center; color: teal; font_size:16px;'><strong>Made with ❤ by Anuditya Gupttaa</strong><br>  Capstone Project | OL Cohort 1.0</div>""",
    unsafe_allow_html=True
)

st.markdown("Select a page from the **sidebar** to navigate onto other pages and get started.")



