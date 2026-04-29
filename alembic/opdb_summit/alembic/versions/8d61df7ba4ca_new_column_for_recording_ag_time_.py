"""New column for recording AG time; tickets/INSTRM-2801

Revision ID: 8d61df7ba4ca
Revises: 26a4e346fbf1
Create Date: 2026-04-28 13:59:54.106135

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8d61df7ba4ca'
down_revision = '26a4e346fbf1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('agc_guide_offset', sa.Column('taken_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))


def downgrade():
    op.drop_column('agc_guide_offset', 'taken_at')
