import streamlit as st

# Configure the page layout and title
st.set_page_config(
    page_title="Backlog Remainder 2024",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark mode styling
st.markdown("""
    <style>
    .main, .stApp {
        background-color: #f97316;
        padding: 1rem;
    }
    
    .container {
        background-color: white;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .task-card {
        background-color: #1a1a1a;
        border-radius: 4px;
        padding: 0.75rem;
        margin: 0.5rem 0;
        color: white;
        font-family: monospace;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    
    .task-content {
        flex-grow: 1;
    }
    
    .task-description {
        color: #666;
        font-size: 0.9em;
        display: block;
        margin-top: 0.25rem;
        font-family: system-ui;
    }
    
    .priority-s {
        background-color: #22c55e;
        color: white;
        padding: 0.1rem 0.5rem;
        border-radius: 2px;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }
    
    .priority-m {
        background-color: #3b82f6;
        color: white;
        padding: 0.1rem 0.5rem;
        border-radius: 2px;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }
    
    .priority-l {
        background-color: #ef4444;
        color: white;
        padding: 0.1rem 0.5rem;
        border-radius: 2px;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }
    
    h1 {
        color: #581c87;
        text-align: center;
        font-size: 2rem;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    
    h2 {
        color: white;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .chevrons {
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<h1>BACKLOG REMAINDER 2024</h1>', unsafe_allow_html=True)

# Data structure
tasks = {
    'ongoing': [
        {"title": "Easypay", "priority": "L", "has_chevron": True},
        {"title": "Plan A", "description": "Set-up firms CTRL-F & National Dedicated", "priority": "M"},
        {"title": "Square migration", "priority": "M"},
        {"title": "Open minded hiring", "priority": "S", "has_chevron": True},
        {"title": "Automated onboarding", "description": "dig sig EHBO kit", "priority": "M", "has_chevron": True},
        {"title": "Bullhorn4SalesForce integration", "priority": "S"},
        {"title": "Business Central", "priority": "L"},
        {"title": "Contract ready", "description": "automated via OCR", "priority": "S", "has_chevron": True}
    ],
    'upNext': [
        {"title": "Tax Exemption", "description": "legal changes", "priority": "S"},
        {"title": "Legal changes", "priority": "S"},
        {"title": "ATS Integration", "description": "Connecting Expertise improvements", "priority": "S"},
        {"title": "RLPLYR", "priority": "S"},
        {"title": "Admin", "description": "planning improvements", "priority": "M"},
        {"title": "Job satisfaction data analysis", "description": "iimpact", "priority": "S"},
        {"title": "ATS integration", "description": "Jobtoolz", "priority": "M"}
    ]
}

def create_task_card(task):
    """Create a task card with monospace styling"""
    chevrons = ' >>' if task.get('has_chevron') else ''
    description = f'<div class="task-description">{task["description"]}</div>' if 'description' in task else ''
    
    return f"""
        <div class="task-card">
            <div class="task-content">
                /div {task['title']}{chevrons}
                {description}
            </div>
            <span class="priority-{task['priority'].lower()}">{task['priority']}</span>
        </div>
    """

# Create two-column layout
col1, col2 = st.columns(2)

# Ongoing tasks
with col1:
    st.markdown('<h2>Ongoing</h2>', unsafe_allow_html=True)
    for task in tasks['ongoing']:
        st.markdown(create_task_card(task), unsafe_allow_html=True)

# Up next tasks
with col2:
    st.markdown('<h2>Up next</h2>', unsafe_allow_html=True)
    for task in tasks['upNext']:
        st.markdown(create_task_card(task), unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="background-color: rgba(0,0,0,0.1); padding: 1rem; border-radius: 8px; text-align: center; color: white; margin-top: 2rem;">
        As IT, we aim to always work on our highest priority first. We work in a top/down manner in order to drive forward the items with the highest impact.
    </div>
    """, unsafe_allow_html=True)