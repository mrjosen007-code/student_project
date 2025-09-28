import streamlit as st
import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("students.db")
c = conn.cursor()

# Create a table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()

# ---------------- Add New Student ----------------
st.title("🎓 Student Management System")

st.subheader("Add a New Student")
name = st.text_input("Name")
email = st.text_input("Email")
course = st.text_input("Course")

if st.button("Add Student"):
    if name and email and course:
        c.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)", (name, email, course))
        conn.commit()
        st.success(f"Student {name} added successfully!")
    else:
        st.warning("Please fill in all fields")

