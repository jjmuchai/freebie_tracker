import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from database import Base, engine
import models


print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully!")
