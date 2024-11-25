import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Function to load history from the CSV file
def load_history():
    # Ensure the 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')  # Create the 'data' directory if it doesn't exist
    
    # Now check if the history file exists
    if os.path.exists('data/history.csv'):
        history_df = pd.read_csv('data/history.csv')
    else:
        history_df = pd.DataFrame()  # Return an empty DataFrame if the file doesn't exist
    return history_df

# Function to clear the history
def clear_history():
    if os.path.exists('data/history.csv'):
        os.remove('data/history.csv')
        st.success("History cleared successfully.")
    else:
        st.warning("History is already empty.")

# Function to append a history entry to the CSV file
def append_history(username, action):
    # Create a DataFrame with the new history entry
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history_entry = pd.DataFrame([{'username': username, 'action': action, 'timestamp': timestamp}])
    
    # Append the entry to the CSV file
    history_entry.to_csv('data/history.csv', index=False, mode='a', header=not os.path.exists('data/history.csv'))

# Main function to display the history page
def main():
    # Check if the user is logged in
    if 'name' not in st.session_state:
        st.error("You need to log in to access this page.")
    else:
        st.title('History Page')
        
        # Load history data
        history_df = load_history()
        
        # Display history data if available
        if not history_df.empty:
            st.write(history_df)
        else:
            st.warning("History is empty.")
        
        # Add a clear button to delete the history
        if st.button('Clear History'):
            clear_history()
        
        # Add logout button
        with st.sidebar:
            st.title("Logout")
            if st.button("Logout"):
                # Record logout action in history
                append_history(st.session_state['name'], 'logged out')
                del st.session_state["name"]
                st.success('You have been logged out successfully.')

        # Example: record a successful login action
        if 'name' in st.session_state:
            append_history(st.session_state['name'], 'logged in')

# Run the main function
if __name__ == '__main__':
    main()
