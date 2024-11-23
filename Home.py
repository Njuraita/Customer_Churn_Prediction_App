# Import necessary libraries
import streamlit as st

# Configure the page
st.set_page_config(
    page_title='Customer Churn Prediction App',
    page_icon='👨‍💻',
    layout='centered',
    initial_sidebar_state='auto'
)

# Add custom CSS to adjust the width of the sidebar
st.markdown("""
    <style> 
        section[data-testid="stSidebar"] {
            width: 200px !important;
        }
    </style> 
""", unsafe_allow_html=True)

def main():

# Add an image to the homepage
    st.image("images\homeimage.jpeg", use_container_width=True)

    st.header('Customer Churn Prediction App')

    st.write(
        """
        Welcome to the **Customer Churn Prediction App**! This project is a web-based application that predicts customer churn using machine learning models. The app allows users/businessess to upload customer data, preprocess it, and run predictions to identify which customers are at risk of leaving/churning, helping the businessess take neccesssary action to prevent increased customer churn.
        """
    )

    # About the App
    st.subheader('About the App')
    st.write(
        """
        This application leverages historical data to predict the likelihood of customer churn. By analyzing customer demographics, subscription details, and account information, the app helps businesses:
        
        * Identify customers at risk of churning
        * Understand factors influencing churn
        * Implement strategies to retain valuable customers
        
        With a user-friendly interface and powerful predictive models, our app provides actionable insights to enhance customer retention strategies.
        """
    )

    # Key Features
    st.subheader('Key Features')
    st.markdown("""
        * **Data View**: Explore and analyze customer data to gain insights into churn patterns.
        * **Dashboard**: Visualize key metrics and trends through interactive charts and graphs.
        * **Predict**: Use our predictive models to estimate the likelihood of customer churn based on various factors.
        * **History**: Review past predictions and track changes over time.
        """)

    # Key Advantages
    st.subheader('Why Use This App?')
    st.markdown("""
        * **Accurate Predictions**: Benefit from state-of-the-art machine learning models for reliable churn forecasts.
        * **Intuitive Interface**: Navigate through a user-friendly interface designed for ease of use.
        * **Actionable Insights**: Gain insights into customer behavior and retention strategies.
        * **Continuous Improvement**: Regular updates and enhancements to keep up with the latest trends and technologies.
        """)

    # How to Run the App
    st.subheader('How to Get Started')
    st.write("Follow these steps to run the Customer Churn Prediction App:")
    st.code("""
        # Activate your virtual environment
        venv/Scripts/activate

        # Run the Streamlit app
        streamlit run app.py
        """, language="python")

    # Machine Learning Integration
    st.subheader('Machine Learning Models')
    st.write(
        """
        Our app integrates advanced machine learning models, including Gradient Boosting and Support Vector Machines (SVM). These models are trained on historical data to deliver accurate predictions and help businesses make informed decisions.
        """
    )

    # Need Assistance
    st.subheader('Need Help?')
    st.write(
        """
        If you encounter any issues or have questions, please don't hesitate to reach out:
        - **Email**: njerisharon06@gmail.com
        - **GitHub**: [GitHub Repository](https://github.com/Njuraita/Customer_Churn_Prediction_App2.git)
        - **LinkedIn**: [Connect on LinkedIn](www.linkedin.com/in/sharon-njeri-njuraita)
        """
    )

if __name__ == '__main__':
    main()
