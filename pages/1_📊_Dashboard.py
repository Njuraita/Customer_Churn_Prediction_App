import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

st.title('Customer Churn Dashboard')

# ------ Set visualization view page
col1, col2, col3 = st.columns(3)
with col2:
    options = st.selectbox('Choose viz to display', options=['', 'EDA Dashboard', 'KPIs Dashboard'])

# Load data
@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv('data\cleaned_merged.csv')
    return data

# Display data
data = load_data()
st.dataframe(data.head())

# EDA Dashboard
if options == 'EDA Dashboard':
    st.subheader("EDA Dashboard")
    st.markdown(""" 
                - This dashboard provides an exploratory data analysis of the customer churn dataset.
                - The data includes customer demographics and usage patterns.
                 """)

    # 1. Countplot for churn distribution by contract type
    fig, ax = plt.subplots(figsize=(8, 6))  # Create figure and axis objects
    sns.countplot(x='Contract', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Contract Type')
    st.pyplot(fig)  # Pass figure explicitly

    # 2. Distribution of Monthly Charges
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data['MonthlyCharges'], kde=True, ax=ax)
    ax.set_title('Distribution of Monthly Charges')
    st.pyplot(fig)  # Pass figure explicitly

    # 3. Tenure vs Monthly Charges (Scatter Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='tenure', y='MonthlyCharges', hue='Churn', data=data, ax=ax)
    ax.set_title('Tenure vs Monthly Charges')
    st.pyplot(fig)  # Pass figure explicitly

    # 4. Churn by Internet Service (Bar Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='InternetService', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Internet Service Type')
    st.pyplot(fig)  # Pass figure explicitly

    # 5. Churn by Gender (Bar Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='gender', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Gender')
    st.pyplot(fig)  # Pass figure explicitly

    # 6. Churn by Senior Citizen Status (Bar Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='SeniorCitizen', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Senior Citizen Status')
    st.pyplot(fig)  # Pass figure explicitly


# KPIs Dashboard
if options == 'KPIs Dashboard':
    st.subheader("KPIs Dashboard")
    st.markdown(""" 
                - This dashboard provides key performance indicators (KPIs) of the customer churn dataset.
                - The KPIs include churn distribution, average charges, tenure, and more.
                - Below are visuals for the KPIs, each with a detailed explanation of the visual interpretation.
    
     **KPIs for our dashboard**:
            - *Contract Type*: Understanding the churn rate by contract type.
            - *Charges*: Evaluating the average monthly charges by contract type.
            - *Tenure*: Analyzing the average tenure of customers by contract type.
            - *Payment Methods*: Assessing the churn rate based on different payment methods.
            - *Total Charges*: Evaluating the total charges for customers by contract type.
            - *Internet Service*: Understanding churn based on the type of internet service provided to the customer.
             """)

    # Visualizations for KPIs

    # 1. Contract type vs churn distribution (using Matplotlib)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='Contract', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Contract Type')
    st.pyplot(fig)

    # 2. Average Monthly Charges by Contract Type (using Plotly)
    fig = px.bar(data, x='Contract', y='MonthlyCharges', title='Average Monthly Charges by Contract Type')
    st.plotly_chart(fig)

    # 3. Average Tenure by Contract Type (using Plotly)
    fig = px.box(data, x='Contract', y='tenure', title='Tenure Distribution by Contract Type')
    st.plotly_chart(fig)

    # 4. Churn Rate by Payment Method (using Plotly)
    fig = px.bar(data, x='PaymentMethod', color='Churn', title='Churn Rate by Payment Method')
    st.plotly_chart(fig)

    # 5. Average Total Charges by Contract Type (using Plotly)
    fig = px.bar(data, x='Contract', y='TotalCharges', title='Average Total Charges by Contract Type')
    st.plotly_chart(fig)

    # 6. Churn Rate by Internet Service (using Plotly)
    fig = px.bar(data, x='InternetService', color='Churn', title='Churn Rate by Internet Service')
    st.plotly_chart(fig)

