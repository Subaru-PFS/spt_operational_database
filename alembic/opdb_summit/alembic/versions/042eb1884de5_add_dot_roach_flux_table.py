"""add dot_roach_flux table

Revision ID: 042eb1884de5
Revises: 06febe7976d8
Create Date: 2026-03-17 10:02:00.695024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042eb1884de5'
down_revision = '06febe7976d8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('dot_roach_flux',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='PFS visit identifier'),
                    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Cobra identifier (1..2394)'),
                    sa.Column('flux', sa.REAL(), nullable=True,
                              comment='Raw extracted flux [ADU]'),
                    sa.Column('flux_norm', sa.REAL(), nullable=True,
                              comment='Flux normalized by lamp response'),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id']),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'cobra_id'),
                    sa.UniqueConstraint('pfs_visit_id', 'cobra_id'),
                    )


def downgrade():
    op.drop_table('dot_roach_flux')
