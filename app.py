"""
HelpdeskAI Dashboard - A unified IT operations dashboard
"""
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os

# Constants
DB_PATH = os.path.join(os.path.dirname(__file__), 'helpdesk.db')

# Page configuration
st.set_page_config(
    page_title="HelpdeskAI Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_db_connection():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def load_tickets_data():
    """Load ticket data from the database."""
    with get_db_connection() as conn:
        query = "SELECT * FROM tickets"
        df = pd.read_sql_query(query, conn)
    return df

def get_tickets_per_technician():
    """Get ticket count per technician."""
    with get_db_connection() as conn:
        query = """
            SELECT technician, COUNT(*) as ticket_count
            FROM tickets
            GROUP BY technician
            ORDER BY ticket_count DESC
        """
        df = pd.read_sql_query(query, conn)
    return df

# Sidebar navigation
st.sidebar.title("🎯 HelpdeskAI")
st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")

# Main title
st.title("HelpdeskAI Dashboard")
st.markdown("A unified IT operations dashboard aggregating data from TeamDynamix, Microsoft Intune, and SQL Integrity systems.")
st.markdown("---")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📊 Operational Overview", "🔗 Relationship Graph", "🤖 AI Assistant"])

# Tab 1: Operational Overview
with tab1:
    st.header("Operational Overview")
    
    # Check if database exists
    if not os.path.exists(DB_PATH):
        st.warning("⚠️ Database not found. Please run `python init_database.py` to initialize the database.")
    else:
        try:
            # Load data
            tickets_df = load_tickets_data()
            technician_stats = get_tickets_per_technician()
            
            # Display metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Tickets", len(tickets_df))
            with col2:
                open_tickets = len(tickets_df[tickets_df['status'] == 'Open'])
                st.metric("Open Tickets", open_tickets)
            with col3:
                st.metric("Technicians", len(technician_stats))
            
            st.markdown("---")
            
            # Tickets per Technician Bar Chart
            st.subheader("Tickets per Technician")
            fig = px.bar(
                technician_stats,
                x='technician',
                y='ticket_count',
                title='Total Tickets Assigned to Each Technician',
                labels={'technician': 'Technician', 'ticket_count': 'Number of Tickets'},
                color='ticket_count',
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                xaxis_title="Technician",
                yaxis_title="Number of Tickets",
                showlegend=False,
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Display raw data
            with st.expander("📋 View Raw Ticket Data"):
                st.dataframe(tickets_df, use_container_width=True)
                
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            st.info("Please ensure the database is properly initialized by running `python init_database.py`")

# Tab 2: Relationship Graph
with tab2:
    st.header("Relationship Graph")
    st.info("🚧 This feature is under development. It will visualize relationships between tickets, technicians, and systems.")
    st.markdown("""
    **Planned Features:**
    - Network graph showing ticket dependencies
    - Technician workload distribution
    - System integration mapping
    """)

# Tab 3: AI Assistant
with tab3:
    st.header("AI Assistant")
    st.info("🚧 This feature is under development. It will provide AI-powered insights and assistance.")
    st.markdown("""
    **Planned Features:**
    - Natural language queries about ticket data
    - Predictive analytics for ticket resolution times
    - Automated ticket categorization
    - Trend analysis and recommendations
    """)

# Sidebar information
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("""
This dashboard aggregates data from:
- TeamDynamix (Ticketing)
- Microsoft Intune (MDM)
- SQL Integrity System
""")
