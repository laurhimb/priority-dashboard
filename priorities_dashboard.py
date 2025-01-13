import streamlit as st
import pandas as pd

# Configure the page layout and title
st.set_page_config(
    page_title="Strategic Priorities Dashboard",
    layout="wide",  # This makes the dashboard use the full screen width
    initial_sidebar_state="expanded"  # Shows the sidebar by default
)

# Add a title and description
st.title("Strategic Priorities Dashboard")
st.write("Track and manage strategic initiatives in real-time")

# Create some sample data (later we'll read this from a CSV)
sample_data = {
    'project': ['Digital Transformation', 'Customer Experience', 'Data Security'],
    'priority': ['High', 'Medium', 'Critical'],
    'status': ['In Progress', 'Planning', 'In Progress'],
    'completion': [65, 20, 80]
}

# Convert the sample data to a pandas DataFrame
df = pd.DataFrame(sample_data)

# Display each priority as a card
for index, row in df.iterrows():
    # Create a container for each priority
    with st.container():
        # Use columns to create a card-like layout
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(row['project'])
        with col2:
            # Color-code the priority
            if row['priority'] == 'Critical':
                st.markdown('🔴 **Critical**')
            elif row['priority'] == 'High':
                st.markdown('🟠 **High**')
            else:
                st.markdown('🟡 **Medium**')
        
        # Show status and progress
        st.write(f"Status: {row['status']}")
        st.progress(row['completion'] / 100)
        st.write(f"Progress: {row['completion']}%")
        st.divider()