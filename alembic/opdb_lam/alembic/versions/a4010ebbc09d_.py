"""empty message

Revision ID: a4010ebbc09d
Revises: 910c4ead6bc1
Create Date: 2022-09-01 17:26:06.638215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4010ebbc09d'
down_revision = '910c4ead6bc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('agc_data', 'image_moment_00_pix',
               existing_type=sa.REAL(),
               comment='',
               existing_nullable=True)
    op.create_foreign_key(None, 'agc_exposure', 'pfs_visit', ['pfs_visit_id'], ['pfs_visit_id'])
    op.add_column('mcs_data', sa.Column('flags', sa.Integer(), nullable=True, comment='Flags about the fitted centroids parameters'))
    op.alter_column('pfs_config', 'pfs_design_id',
               existing_type=sa.BIGINT(),
               nullable=False,
               autoincrement=False)
    op.alter_column('pfs_config', 'visit0',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_comment='The first visit of the set',
               autoincrement=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pfs_config', 'visit0',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_comment='The first visit of the set',
               autoincrement=False)
    op.alter_column('pfs_config', 'pfs_design_id',
               existing_type=sa.BIGINT(),
               nullable=True,
               autoincrement=False)
    op.drop_column('mcs_data', 'flags')
    op.drop_constraint(None, 'agc_exposure', type_='foreignkey')
    op.alter_column('agc_data', 'image_moment_00_pix',
               existing_type=sa.REAL(),
               comment=None,
               existing_comment='',
               existing_nullable=True)
    # ### end Alembic commands ###
