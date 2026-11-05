"""add pfs_config.dot_landing and pfs_config.dot_target

pfs_config.dot_landing
    Depth the ramp lands the dot cobras at, in dot fraction, from the pfsConfig
    convergence parameter dotLanding; NULL if no cobra was sent to a dot.
pfs_config.dot_target
    Depth the dot cobras should end at, in dot fraction, from the pfsConfig convergence
    parameter dotTarget: dot_landing without a blind push, NULL if no cobra was sent to
    a dot.

Revision ID: e7c3a9b2d5f1
Revises: d4a8e2f1b6c3
Create Date: 2026-11-05 21:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'e7c3a9b2d5f1'
down_revision = 'd4a8e2f1b6c3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pfs_config',
                  sa.Column('dot_landing', sa.REAL(), nullable=True,
                            comment='Depth the ramp lands the dot cobras at [dot fraction]; '
                                    'NULL if none was sent to a dot'))
    op.add_column('pfs_config',
                  sa.Column('dot_target', sa.REAL(), nullable=True,
                            comment='Depth the dot cobras should end at [dot fraction]; '
                                    'dot_landing without a blind push, NULL if none was '
                                    'sent to a dot'))


def downgrade():
    op.drop_column('pfs_config', 'dot_target')
    op.drop_column('pfs_config', 'dot_landing')
