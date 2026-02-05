"""
Initialize a sample SQL database with ticket data for the dashboard.
"""
import sqlite3
import os

def init_database():
    """Create and populate the tickets database with sample data."""
    db_path = os.path.join(os.path.dirname(__file__), 'helpdesk.db')
    
    # Create connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tickets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_number TEXT NOT NULL,
            technician TEXT NOT NULL,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            created_date TEXT NOT NULL
        )
    ''')
    
    # Clear existing data to allow re-initialization
    cursor.execute('DELETE FROM tickets')
    
    # Insert sample data
    sample_tickets = [
        ('TKT-001', 'John Smith', 'Open', 'High', '2024-01-15'),
        ('TKT-002', 'John Smith', 'Closed', 'Medium', '2024-01-16'),
        ('TKT-003', 'Sarah Johnson', 'Open', 'Low', '2024-01-17'),
        ('TKT-004', 'Mike Davis', 'In Progress', 'High', '2024-01-18'),
        ('TKT-005', 'John Smith', 'Closed', 'Medium', '2024-01-19'),
        ('TKT-006', 'Sarah Johnson', 'Open', 'High', '2024-01-20'),
        ('TKT-007', 'Mike Davis', 'Closed', 'Low', '2024-01-21'),
        ('TKT-008', 'Sarah Johnson', 'In Progress', 'Medium', '2024-01-22'),
        ('TKT-009', 'John Smith', 'Open', 'High', '2024-01-23'),
        ('TKT-010', 'Mike Davis', 'Closed', 'Medium', '2024-01-24'),
        ('TKT-011', 'Sarah Johnson', 'Open', 'Low', '2024-01-25'),
        ('TKT-012', 'Mike Davis', 'In Progress', 'High', '2024-01-26'),
    ]
    
    cursor.executemany('''
        INSERT INTO tickets (ticket_number, technician, status, priority, created_date)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_tickets)
    
    conn.commit()
    conn.close()
    
    print(f"Database initialized successfully at {db_path}")

if __name__ == '__main__':
    init_database()
