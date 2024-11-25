import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Function to load history from the CSV file
def load_history():
    if not os.path.exists('data'):
        os.makedirs('data')
    if os.path.exists('data/history.csv'):
        history_df = pd.read_csv('data/history.csv')
    else:
        history_df = pd.DataFrame()  # Empty DataFrame if file doesn't exist
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
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history_entry = pd.DataFrame([{'username': username, 'action': action, 'timestamp': timestamp}])
    history_entry.to_csv('data/history.csv', index=False, mode='a', header=not os.path.exists('data/history.csv'))

# Main function to display the History Page
def main():
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

# Run the main function
if __name__ == '__main__':
    main()
