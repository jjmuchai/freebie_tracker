from database import session
from models import Company, Dev, Freebie

# Example tests
alice = session.query(Dev).filter_by(name='Alice').first()
bob = session.query(Dev).filter_by(name='Bob').first()
techcorp = session.query(Company).filter_by(name='TechCorp').first()

print(alice.companies)               # Alice's companies
print(techcorp.devs)                 # devs for TechCorp
print(alice.received_one('Mug'))     # True/False
print(Freebie.print_details(alice.freebies[0]))  # e.g. "Alice owns a Sticker from TechCorp."

# Test giving away a freebie
alice.give_away(bob, alice.freebies[0])
print(alice.freebies)  # Should not include the first freebie
print(bob.freebies)    # Should now include the first freebie
