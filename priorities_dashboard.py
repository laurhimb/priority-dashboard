import streamlit as st

# Configure the page layout and title
st.set_page_config(
    page_title="Backlog Remainder 2024",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match React styling
st.markdown("""
    <style>
    /* Main container styling */
    .main, .stApp {
        background-color: rgb(249, 115, 22);
        padding: 1.5rem;
    }
    
    /* Task item styling */
    .task-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
        background-color: white;
        border-radius: 0.5rem;
        border: 1px solid rgb(254, 215, 170);
    }
    
    .task-title {
        font-weight: 500;
        color: rgb(31, 41, 55);
    }
    
    .task-description {
        font-size: 0.875rem;
        color: rgb(107, 114, 128);
    }
    
    /* Priority indicators */
    .priority-indicators {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .priority-s {
        background-color: rgb(220, 252, 231);
        color: rgb(22, 101, 52);
        padding: 0.125rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
    }
    
    .priority-m {
        background-color: rgb(219, 234, 254);
        color: rgb(30, 64, 175);
        padding: 0.125rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
    }
    
    .priority-l {
        background-color: rgb(243, 232, 255);
        color: rgb(107, 33, 168);
        padding: 0.125rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
    }
    
    .chevrons {
        color: black;
        font-size: 0.875rem;
        letter-spacing: -0.3em;
        padding-right: 0.6em;
    }

    /* Section headers */
    .section-header {
        color: white;
        font-size: 1.875rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Footer styling */
    .footer {
        margin-top: 2rem;
        background-color: rgb(234, 88, 12);
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        color: white;
    }

    /* Grid layout */
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Data structure matching React state
tasks = {
    'ongoing': [
        {"id": "1", "title": "Easypay", "size": "L", "isHighPriority": True},
        {"id": "2", "title": "Plan A", "description": "Set-up firms CTRL-F & National Dedicated", "size": "M"},
        {"id": "3", "title": "Square migration", "size": "M"},
        {"id": "4", "title": "Open minded hiring", "size": "S", "isHighPriority": True},
        {"id": "5", "title": "Automated onboarding", "description": "dig sig EHBO kit", "size": "M", "isHighPriority": True},
        {"id": "6", "title": "Bullhorn4SalesForce integration", "size": "S"},
        {"id": "7", "title": "Business Central", "size": "L"},
        {"id": "8", "title": "Contract ready", "description": "automated via OCR", "size": "S", "isHighPriority": True}
    ],
    'upNext': [
        {"id": "9", "title": "Tax Exemption", "description": "legal changes", "size": "S", "hasAddition": True},
        {"id": "10", "title": "Legal changes", "size": "S"},
        {"id": "11", "title": "ATS Integration", "description": "Connecting Expertise improvements", "size": "S"},
        {"id": "12", "title": "RLPLYR", "size": "S"},
        {"id": "13", "title": "Admin", "description": "planning improvements", "size": "M"},
        {"id": "14", "title": "Job satisfaction data analysis", "description": "impact", "size": "S"},
        {"id": "15", "title": "ATS integration", "description": "Jobtoolz", "size": "M"}
    ]
}

def create_task_item(task):
    """Create HTML for a task item matching React component styling"""
    description = f"<span class='task-description'>({task['description']})</span>" if 'description' in task else ""
    addition = "<span>+</span>" if task.get('hasAddition') else ""
    chevrons = "<span class='chevrons'>>></span>" if task.get('isHighPriority') else ""
    
    return f"""
    <div class="task-item">
        <span style="color: rgb(156, 163, 175);">≡</span>
        <div style="flex-grow: 1;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span class="task-title">{task['title']}</span>
                {addition}
                {description}
            </div>
        </div>
        <div class="priority-indicators">
            {chevrons}
            <span class="priority-{task['size'].lower()}">{task['size']}</span>
        </div>
    </div>
    """

# Page title
st.markdown('<h1 style="text-align: center; color: rgb(88, 28, 135); font-size: 2.25rem; font-weight: 700; margin-bottom: 2rem;">BACKLOG REMAINDER 2024</h1>', 
            unsafe_allow_html=True)

# Create two-column layout
col1, col2 = st.columns(2)

# Ongoing tasks column
with col1:
    st.markdown('<h2 class="section-header">Ongoing</h2>', unsafe_allow_html=True)
    for task in tasks['ongoing']:
        st.markdown(create_task_item(task), unsafe_allow_html=True)

# Up next tasks column
with col2:
    st.markdown('<h2 class="section-header">Up next</h2>', unsafe_allow_html=True)
    for task in tasks['upNext']:
        st.markdown(create_task_item(task), unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        As IT, we aim to always work on our highest priority first. We work in a top/down manner in order to drive forward the items with the highest impact.
    </div>
    """, unsafe_allow_html=True)
