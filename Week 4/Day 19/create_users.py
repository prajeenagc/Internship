from app.database import SessionLocal, Base, engine
from app.models import User

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    alice = User(
        username="alice",
        role="user"
    )

    bob = User(
        username="bob",
        role="admin"
    )

    db.add_all([alice, bob])
    db.commit()

    db.refresh(alice)
    db.refresh(bob)

    print(f"Alice ID: {alice.id}, Role: {alice.role}")
    print(f"Bob ID: {bob.id}, Role: {bob.role}")

finally:
    db.close()