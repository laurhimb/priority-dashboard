import streamlit as st

# Configure the page layout and title
st.set_page_config(
    page_title="Backlog Remainder 2024",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with fixed styling
st.markdown("""
    <style>
    .main, .stApp {
        background-color: #E67E22;
        padding: 1rem;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .card {
        background-color: #1E1E1E;
        color: white;
        border-radius: 4px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.75rem;
        font-family: 'Courier New', monospace;
        position: relative;
        min-height: 2.5rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .card-content {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        width: 100%;
    }
    
    .priority {
        position: absolute;
        top: 0.75rem;
        right: 0.75rem;
        padding: 0.15rem 0.5rem;
        border-radius: 2px;
        font-size: 0.8rem;
    }
    
    .priority-s { background-color: #27AE60; }
    .priority-m { background-color: #3498DB; }
    .priority-l { background-color: #E74C3C; }
    
    .subtitle {
        color: #666;
        font-size: 0.9em;
        margin-top: 0.5rem;
        font-family: system-ui;
        display: block;
    }
    
    .project-title {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .arrow {
        color: #666;
        margin-left: 0.25rem;
    }
    
    h1 {
        color: #4A235A;
        text-align: center;
        font-size: 2rem;
        margin: 1rem 0 2rem 0;
        font-weight: bold;
    }
    
    .section-title {
        color: white;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title
st.markdown('<h1>BACKLOG REMAINDER 2024</h1>', unsafe_allow_html=True)

# Project data
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
    """Creates a card with consistent styling and proper HTML structure"""
    arrow = ' >>' if project.get('has_arrow', False) else ''
    subtitle = f'<span class="subtitle">{project["subtitle"]}</span>' if 'subtitle' in project else ''
    
    return f"""
    <div class="card">
        <div class="card-content">
            <div class="project-title">
                /div
                {project['name']}{arrow}
            </div>
            <span class="priority priority-{project['priority'].lower()}">{project['priority']}</span>
        </div>
        {subtitle}
    </div>
    """

# Create two-column layout
col1, col2 = st.columns(2)

# Ongoing projects column
with col1:
    st.markdown('<div class="section-title">Ongoing</div>', unsafe_allow_html=True)
    for project in ongoing_projects:
        st.markdown(create_project_card(project), unsafe_allow_html=True)

# Upcoming projects column
with col2:
    st.markdown('<div class="section-title">Up next</div>', unsafe_allow_html=True)
    for project in upcoming_projects:
        st.markdown(create_project_card(project), unsafe_allow_html=True)