"""Add fiducial_tweaked_x_mm and fiducial_tweaked_y_mm in fiducial_fiber_match

Revision ID: 306be143cb55
Revises: e8c13289241d
Create Date: 2025-06-17 17:11:16.500361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '306be143cb55'
down_revision = 'e8c13289241d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fiducial_fiber_match', sa.Column('fiducial_tweaked_x_mm', sa.REAL(), nullable=True, comment='Expected FF x-position on the PFI at the convergence [mm]'))
    op.add_column('fiducial_fiber_match', sa.Column('fiducial_tweaked_y_mm', sa.REAL(), nullable=True, comment='Expected FF y-position on the PFI at the convergence [mm]'))
    op.alter_column('fiducial_fiber_match', 'pfi_center_x_mm',
               existing_type=sa.REAL(),
               comment='Measured FF x-position on the PFI [mm]',
               existing_comment='Actual x-position on the PFI [mm]',
               existing_nullable=True)
    op.alter_column('fiducial_fiber_match', 'pfi_center_y_mm',
               existing_type=sa.REAL(),
               comment='Measured FF y-position on the PFI [mm]',
               existing_comment='Actual y-position on the PFI [mm]',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fiducial_fiber_match', 'pfi_center_y_mm',
               existing_type=sa.REAL(),
               comment='Actual y-position on the PFI [mm]',
               existing_comment='Measured FF y-position on the PFI [mm]',
               existing_nullable=True)
    op.alter_column('fiducial_fiber_match', 'pfi_center_x_mm',
               existing_type=sa.REAL(),
               comment='Actual x-position on the PFI [mm]',
               existing_comment='Measured FF x-position on the PFI [mm]',
               existing_nullable=True)
    op.drop_column('fiducial_fiber_match', 'fiducial_tweaked_y_mm')
    op.drop_column('fiducial_fiber_match', 'fiducial_tweaked_x_mm')
    # ### end Alembic commands ###
