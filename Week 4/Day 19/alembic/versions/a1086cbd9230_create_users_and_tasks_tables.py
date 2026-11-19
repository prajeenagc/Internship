"""create users and tasks tables

Revision ID: a1086cbd9230
Revises: c0af4f7d6706
Create Date: 2026-11-19 14:01:12.597267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1086cbd9230'
down_revision: Union[str, Sequence[str], None] = 'c0af4f7d6706'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
