# SkillUP Application

## Overview

**SkillUP Application** is a Flask-based web application designed to help students, particularly those with disabilities, by providing resources such as job listings, user profiles, and a curriculum section. The application integrates Azure services and supports features like user authentication, job management, and file uploads.

## Key Features

1. **User Authentication**
   - Secure login using Flask-Login (development).
   - Azure Active Directory (AAD) integration (for production).
   
2. **User Profiles**
   - Users can view and update their profiles.
   - Optional profile picture upload using Azure Blob Storage (or local storage for development).

3. **Job Listings**
   - Displays available job opportunities for students.
   - Admins can add or update job postings.

4. **Curriculum Management**
   - View and manage course materials.
   - Admins can upload curriculum-related files (e.g., syllabi).
   - Supports Azure Blob Storage for syllabus uploads.

5. **Azure Integration**
   - **Azure SQL** for database management (in production).
   - **Azure Blob Storage** for file uploads (e.g., profile pictures, syllabus).
   - **Azure Active Directory (AAD)** for secure authentication (in production).

## Project Structure

The project is organized as follows:

```bash
backend/
├── app.py                # Main Flask application
├── config.py             # Configuration settings (handles environment variables)
├── models.py             # SQLAlchemy models (User, Job, Curriculum)
├── routes/
│   ├── auth.py           # Authentication routes (login, logout)
│   ├── profiles.py       # User profile routes
│   ├── jobs.py           # Job listing routes
│   └── curriculum.py     # Curriculum management routes
├── azure_blob.py         # Azure Blob Storage helper for file uploads
├── database.db           # SQLite database (for local development)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
