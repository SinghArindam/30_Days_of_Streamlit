# pip install ydata_profiling

import streamlit as st
import pandas as pd
# Import ProfileReport from ydata_profiling, which is the successor to pandas_profiling
from ydata_profiling import ProfileReport
# Import the components module to embed HTML
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.header('`ydata-profiling` Report in Streamlit')

# Load the dataset
@st.cache_data # Cache the data loading
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

# URL of the dataset
DATA_URL = 'https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv'

df = load_data(DATA_URL)

if not df.empty:
    st.write("Generating Profile Report...")
    # Generate the profiling report using ydata-profiling
    # You can add arguments like title, minimal=True, explorative=True, etc.
    pr = ProfileReport(df, explorative=True, title='Pandas Profiling Report for Penguins Dataset')

    # Convert the report to an HTML string
    profile_report_html = pr.to_html()

    # Display the HTML report in Streamlit using components.html
    # Set height and width to None to use the full available space
    # Set scrolling to True to enable scrolling within the iframe
    st.write("Displaying Profile Report:")
    components.html(profile_report_html, height=1000, scrolling=True)
else:
    st.warning("Could not load data to generate the profile report.")