# HelpdeskAI Dashboard

A local, unified IT operations dashboard that aggregates data from TeamDynamix (Ticketing), Microsoft Intune (MDM), and a SQL Integrity system.

## Features

- **Operational Overview**: View ticket metrics and visualizations
  - Total tickets, open tickets, and technician counts
  - Bar chart showing tickets per technician
  - Raw ticket data viewer
- **Relationship Graph**: (Coming soon) Visualize relationships between tickets, technicians, and systems
- **AI Assistant**: (Coming soon) AI-powered insights and assistance

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the sample database:
```bash
python init_database.py
```

## Usage

Run the Streamlit dashboard:
```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`.

## Project Structure

- `app.py` - Main Streamlit dashboard application
- `init_database.py` - Database initialization script with sample data
- `requirements.txt` - Python dependencies
- `helpdesk.db` - SQLite database (auto-generated)

## Navigation

The dashboard includes:
- **Sidebar**: Navigation and information panel
- **Three tabs**: 
  - Operational Overview (with live SQL data)
  - Relationship Graph (placeholder)
  - AI Assistant (placeholder)
