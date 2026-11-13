from alembic import op
import sqlalchemy as sa


revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    # USERS TABLE

    op.create_table(
        "users",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "username",
            sa.String(50),
            nullable=False
        ),

        sa.Column(
            "email",
            sa.String(255),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),

        sa.UniqueConstraint("email")
    )

    op.create_index(
        "ix_users_id",
        "users",
        ["id"]
    )

    op.create_index(
        "ix_users_email",
        "users",
        ["email"]
    )


    # PROJECTS TABLE

    op.create_table(
        "projects",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "name",
            sa.String(100),
            nullable=False
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),

        sa.UniqueConstraint("name")
    )

    op.create_index(
        "ix_projects_id",
        "projects",
        ["id"]
    )


    # TASKS TABLE

    op.create_table(
        "tasks",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "title",
            sa.String(100),
            nullable=False
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True
        ),

        sa.Column(
            "is_completed",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false()
        ),

        sa.Column(
            "project_id",
            sa.Integer(),
            sa.ForeignKey(
                "projects.id",
                ondelete="RESTRICT"
            ),
            nullable=False
        ),

        sa.Column(
            "assigned_user_id",
            sa.Integer(),
            sa.ForeignKey(
                "users.id",
                ondelete="SET NULL"
            ),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),

        sa.UniqueConstraint(
            "title",
            "project_id",
            name="uq_task_title_project"
        )
    )

    op.create_index(
        "ix_tasks_id",
        "tasks",
        ["id"]
    )


def downgrade():

    op.drop_index("ix_tasks_id", table_name="tasks")
    op.drop_table("tasks")

    op.drop_index("ix_projects_id", table_name="projects")
    op.drop_table("projects")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")