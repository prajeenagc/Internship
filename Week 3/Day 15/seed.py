from app.database import SessionLocal
from app import models


def seed_database():

    db = SessionLocal()

    try:

        user = db.query(models.User).filter(
            models.User.email == "john@example.com"
        ).first()

        if not user:
            user = models.User(
                username="john",
                email="john@example.com"
            )

            db.add(user)
            db.flush()

        project = db.query(models.Project).filter(
            models.Project.name == "Backend Development"
        ).first()

        if not project:
            project = models.Project(
                name="Backend Development",
                description="Backend API development project"
            )

            db.add(project)
            db.flush()

        task = db.query(models.Task).filter(
            models.Task.title == "Build REST API",
            models.Task.project_id == project.id
        ).first()

        if not task:
            task = models.Task(
                title="Build REST API",
                description="Create CRUD endpoints using FastAPI",
                project_id=project.id,
                assigned_user_id=user.id,
                is_completed=False
            )

            db.add(task)

        db.commit()

        print("Seed data inserted successfully!")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()