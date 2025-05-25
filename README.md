# Freebie Tracker

A simple app to track developer freebies (swag) from companies using Python and SQLAlchemy.

## Project Structure

freebie_tracker/
├── migrations/ # Database migration scripts
├── models.py # Models: Company, Dev, Freebie
├── seed.py # Seed initial data
├── debug.py # Interactive testing
├── database.py # DB setup and session
├── Pipfile
└── README.md


## Setup

1. Install dependencies and activate shell:  
   `pipenv install sqlalchemy ipython`  
   `pipenv shell`

2. Run migrations:  
   `python migrations/create_tables.py`

3. Seed the database:  
   `python seed.py`

4. Test your models:  
   `python debug.py`

---

## Summary

- **Company** and **Dev** connected via **Freebie** (many-to-many)  
- Add freebies, query relationships, and test functionality  

Have fun tracking your swag! 🎉
