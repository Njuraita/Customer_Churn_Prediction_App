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
    st.pyplot(fig)
    st.write("""
        **Observation**: Customers with month-to-month contracts exhibit a significantly higher churn rate 
        compared to those with longer-term contracts. This indicates that customers on short-term contracts are less loyal or less satisfied.
    """)

    # 2. Distribution of Monthly Charges
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data['MonthlyCharges'], kde=True, ax=ax)
    ax.set_title('Distribution of Monthly Charges')
    st.pyplot(fig)
    st.write("""
        **Observation**: The monthly charges appear to be right-skewed, with most customers falling in the lower 
        monthly charge range. Customers with higher monthly charges might be opting for premium services, which could correlate with churn behavior.
    """)

    # 3. Tenure vs Monthly Charges (Scatter Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='tenure', y='MonthlyCharges', hue='Churn', data=data, ax=ax)
    ax.set_title('Tenure vs Monthly Charges')
    st.pyplot(fig)
    st.write("""
        **Observation**: Customers with shorter tenures are more likely to churn, especially those with high monthly 
        charges. Longer-tenure customers are generally more stable, possibly due to satisfaction with services or longer-term contracts.
    """)

    # 4. Churn by Internet Service (Bar Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='InternetService', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Internet Service Type')
    st.pyplot(fig)
    st.write("""
        **Observation**: Fiber optic internet users tend to churn more frequently compared to DSL or no internet service. 
        This might indicate dissatisfaction with the fiber optic service or its pricing.
    """)

    # 5. Churn by Gender (Bar Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='gender', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Gender')
    st.pyplot(fig)
    st.write("""
        **Observation**: Churn rates do not show a significant difference between male and female customers, 
        suggesting that gender is not a strong factor in determining churn behavior.
    """)

    # 6. Churn by Senior Citizen Status (Bar Plot)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='SeniorCitizen', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Senior Citizen Status')
    st.pyplot(fig)
    st.write("""
        **Observation**: Senior citizens have a slightly higher churn rate compared to non-senior citizens. 
        This could be due to different usage needs or affordability concerns.
    """)

# KPIs Dashboard
if options == 'KPIs Dashboard':
    st.subheader("KPIs Dashboard")
    st.markdown(""" 
                - This dashboard provides key performance indicators (KPIs) of the customer churn dataset.
                - The KPIs include churn distribution, average charges, tenure, and more.
                 """)

    # 1. Contract type vs churn distribution (using Matplotlib)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='Contract', hue='Churn', data=data, ax=ax)
    ax.set_title('Churn Distribution by Contract Type')
    st.pyplot(fig)
    st.write("""
        **Observation**: Month-to-month contracts have the highest churn rate. Annual and bi-annual contracts have lower churn rates, 
        possibly due to commitment and discounts offered for long-term plans.
    """)

    # 2. Average Monthly Charges by Contract Type (using Plotly)
    fig = px.bar(data, x='Contract', y='MonthlyCharges', title='Average Monthly Charges by Contract Type')
    st.plotly_chart(fig)
    st.write("""
        **Observation**: Month-to-month customers generally have slightly higher monthly charges compared to longer-term contracts. 
        This could contribute to the higher churn rate among these customers.
    """)

    # 3. Average Tenure by Contract Type (using Plotly)
    fig = px.box(data, x='Contract', y='tenure', title='Tenure Distribution by Contract Type')
    st.plotly_chart(fig)
    st.write("""
        **Observation**: Longer-term contracts have customers with higher tenures, indicating stable and loyal customers. 
        Month-to-month customers tend to have lower tenures, reinforcing the link between short tenures and higher churn rates.
    """)

    # 4. Churn Rate by Payment Method (using Plotly)
    fig = px.bar(data, x='PaymentMethod', color='Churn', title='Churn Rate by Payment Method')
    st.plotly_chart(fig)
    st.write("""
        **Observation**: Electronic check users have the highest churn rates compared to other payment methods such as credit card or bank transfers. 
        This might indicate a need for improving the convenience of payment options.
    """)

    # 5. Average Total Charges by Contract Type (using Plotly)
    fig = px.bar(data, x='Contract', y='TotalCharges', title='Average Total Charges by Contract Type')
    st.plotly_chart(fig)
    st.write("""
        **Observation**: Total charges are significantly higher for long-term contract customers, 
        as they tend to stay with the service longer. Month-to-month customers show lower total charges due to their shorter tenure.
    """)

    # 6. Churn Rate by Internet Service (using Plotly)
    fig = px.bar(data, x='InternetService', color='Churn', title='Churn Rate by Internet Service')
    st.plotly_chart(fig)
    st.write("""
        **Observation**: Customers using fiber optic internet have a noticeably higher churn rate compared to those using DSL or no internet service. 
        This could be an opportunity to investigate customer dissatisfaction with fiber optic services.
    """)
