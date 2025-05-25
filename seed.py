from database import session
from models import Company, Dev, Freebie

# Create some data
c1 = Company(name='TechCorp', founding_year=2000)
c2 = Company(name='DevGoods', founding_year=1995)

d1 = Dev(name='Alice')
d2 = Dev(name='Bob')

f1 = Freebie(item_name='Sticker', value=1, dev=d1, company=c1)
f2 = Freebie(item_name='T-Shirt', value=10, dev=d2, company=c1)
f3 = Freebie(item_name='Mug', value=5, dev=d1, company=c2)

# Save to database
session.add_all([c1, c2, d1, d2, f1, f2, f3])
session.commit()
print("Seed data created!")
