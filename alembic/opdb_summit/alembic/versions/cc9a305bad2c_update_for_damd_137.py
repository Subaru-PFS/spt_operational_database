"""update for DAMD-137

Revision ID: cc9a305bad2c
Revises: b24ca6741816
Create Date: 2023-07-23 18:59:26.470416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc9a305bad2c'
down_revision = 'b24ca6741816'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pfs_design_fiber', sa.Column('target_pm_ra', sa.REAL(), nullable=True, comment='Proper motion of the target in R.A. [mas/yr]'))
    op.add_column('pfs_design_fiber', sa.Column('target_pm_dec', sa.REAL(), nullable=True, comment='Proper motion of the target in Dec. [mas/yr]'))
    op.add_column('pfs_design_fiber', sa.Column('target_parallax', sa.REAL(), nullable=True, comment='Parallax of the target [mas]'))
    op.add_column('pfs_design_fiber', sa.Column('epoch', sa.String(), nullable=True, comment='epoch'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pfs_design_fiber', 'epoch')
    op.drop_column('pfs_design_fiber', 'target_parallax')
    op.drop_column('pfs_design_fiber', 'target_pm_dec')
    op.drop_column('pfs_design_fiber', 'target_pm_ra')
    # ### end Alembic commands ###
