# 🛍️ Freebie Tracker

This is a small app to track all the developer freebies (swag!) given away at hackathons and events.  
Built with Python and SQLAlchemy.

---

## 🗂️ Project Folder Structure

freebie_tracker/
├── migrations/
│ ├── create_tables.py
│ └── ...
├── models.py
├── seed.py
├── debug.py
├── database.py
├── Pipfile
├── Pipfile.lock
└── README.md

---

## 1️⃣ database.py

This file sets up the **database engine, Base class, and session**:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebie_tracker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
2️⃣ models.py
Defines three main models:

Company

Dev

Freebie

Each model also includes methods for common actions.

python
Copy
Edit
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship('Freebie', back_populates='company')
    devs = relationship('Dev', secondary='freebies', back_populates='companies')

    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship('Freebie', back_populates='dev')
    companies = relationship('Company', secondary='freebies', back_populates='devs')

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()

class Freebie(Base):
    __tablename__ = 'freebies'
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."
3️⃣ migrations folder
Use this to create your tables:

migrations/create_tables.py

python
Copy
Edit
from database import Base, engine
from models import Company, Dev, Freebie

print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully!")
Run it:

bash
Copy
Edit
python migrations/create_tables.py
4️⃣ seed.py
Add initial data to the database:

python
Copy
Edit
from database import session
from models import Company, Dev, Freebie

c1 = Company(name='TechCorp', founding_year=2000)
c2 = Company(name='DevGoods', founding_year=1995)
d1 = Dev(name='Alice')
d2 = Dev(name='Bob')
f1 = Freebie(item_name='Sticker', value=1, dev=d1, company=c1)
f2 = Freebie(item_name='T-Shirt', value=10, dev=d2, company=c1)
f3 = Freebie(item_name='Mug', value=5, dev=d1, company=c2)

session.add_all([c1, c2, d1, d2, f1, f2, f3])
session.commit()
print("Seed data created!")
Run it:

bash
Copy
Edit
python seed.py
5️⃣ debug.py
Test your models and relationships interactively:

python
Copy
Edit
from database import session
from models import Company, Dev, Freebie

alice = session.query(Dev).filter_by(name='Alice').first()
bob = session.query(Dev).filter_by(name='Bob').first()
techcorp = session.query(Company).filter_by(name='TechCorp').first()

print(alice.companies)  # Alice's companies
print(techcorp.devs)    # Devs for TechCorp
print(alice.received_one('Mug'))  # True/False
print(alice.freebies[0].print_details())

alice.give_away(bob, alice.freebies[0])
print(alice.freebies)
print(bob.freebies)
Run it:

bash
Copy
Edit
python debug.py
6️⃣ Install Dependencies
Install the project dependencies:

bash
Copy
Edit
pipenv install sqlalchemy ipython
pipenv shell
🎯 Summary
✅ database.py: sets up database
✅ models.py: defines your models
✅ migrations/: creates tables
✅ seed.py: seeds the database
✅ debug.py: test everything interactively!

