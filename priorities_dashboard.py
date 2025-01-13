import streamlit as st
import pandas as pd

# Configure the page layout and title with company styling
st.set_page_config(
    page_title="Backlog Remainder 2024",
    layout="wide",  # Use full width
    initial_sidebar_state="collapsed"  # Hide sidebar by default
)

# Custom CSS to match company styling
st.markdown("""
    <style>
    /* Main background and layout */
    .main, .stApp {
        background-color: #E67E22;
    }
    
    /* Project card styling */
    div[data-testid="stHorizontalBlock"] > div {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    /* Priority badge colors */
    .priority {
        padding: 4px 8px;
        border-radius: 4px;
        color: white;
        float: right;
    }
    .priority-s { background-color: #27AE60; }
    .priority-m { background-color: #3498DB; }
    .priority-l { background-color: #E74C3C; }
    
    /* Subtitle styling */
    .subtitle {
        color: #7F8C8D;
        font-size: 0.9em;
        margin-top: 4px;
    }
    
    /* Footer styling */
    .footer {
        background-color: rgba(0, 0, 0, 0.1);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-top: 30px;
    }

    /* Arrow indicator styling */
    .arrow {
        color: #95A5A6;
        font-weight: bold;
        margin-left: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title with company styling
st.markdown('<h1 style="text-align: center; color: #4A235A; font-size: 2.5em; margin-bottom: 2rem;">BACKLOG REMAINDER 2024</h1>', 
            unsafe_allow_html=True)

# Define project data structures
ongoing_projects = [
    {"name": "Easypay", "priority": "L", "has_arrow": True},
    {"name": "Plan A", "subtitle": "Set-up firms CTRL-F & National Dedicated", "priority": "M"},
    {"name": "Square migration", "priority": "M"},
    {"name": "Open minded hiring", "priority": "S", "has_arrow": True},
    {"name": "Automated onboarding", "subtitle": "dig sig EHBO kit", "priority": "M", "has_arrow": True},
    {"name": "Bullhorn4SalesForce integration", "priority": "S"},
    {"name": "Business Central", "priority": "L"},
    {"name": "Contract ready", "subtitle": "automated via OCR", "priority": "S", "has_arrow": True}
]

upcoming_projects = [
    {"name": "Tax Exemption", "subtitle": "legal changes", "priority": "S"},
    {"name": "Legal changes", "priority": "S"},
    {"name": "ATS Integration", "subtitle": "Connecting Expertise improvements", "priority": "S"},
    {"name": "RLPLYR", "priority": "S"},
    {"name": "Admin", "subtitle": "planning improvements", "priority": "M"},
    {"name": "Job satisfaction data analysis", "subtitle": "iimpact", "priority": "S"},
    {"name": "ATS integration", "subtitle": "Jobtoolz", "priority": "M"}
]

def create_project_card(project):
    """Creates a styled card for a project using HTML/CSS."""
    arrow = ' <span class="arrow">>></span>' if project.get('has_arrow', False) else ''
    subtitle = f'<div class="subtitle">{project["subtitle"]}</div>' if 'subtitle' in project else ''
    
    return f"""
    <div style="display: flex; justify-content: space-between; align-items: start;">
        <div style="flex-grow: 1;">
            <strong>{project['name']}{arrow}</strong>
            {subtitle}
        </div>
        <span class="priority priority-{project['priority'].lower()}">{project['priority']}</span>
    </div>
    """

# Create two-column layout
col1, col2 = st.columns(2)

# Ongoing projects column
with col1:
    st.markdown('<h2 style="color: white; margin-bottom: 1rem;">Ongoing</h2>', unsafe_allow_html=True)
    for project in ongoing_projects:
        st.markdown(create_project_card(project), unsafe_allow_html=True)

# Upcoming projects column
with col2:
    st.markdown('<h2 style="color: white; margin-bottom: 1rem;">Up next</h2>', unsafe_allow_html=True)
    for project in upcoming_projects:
        st.markdown(create_project_card(project), unsafe_allow_html=True)

# Footer message
st.markdown("""
    <div class="footer">
        As IT, we aim to always work on our highest priority first. We work in a top/down manner in order to drive forward the items with the highest impact.
    </div>
    """, unsafe_allow_html=True)
