"""add iic_sequence.group_id

Revision ID: b13b0e542938
Revises: c61de880d72a
Create Date: 2022-09-15 21:48:06.047935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b13b0e542938'
down_revision = 'c61de880d72a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column('iic_sequence',
                  sa.Column('group_id', sa.Integer(), autoincrement=False, comment='Group identifier'))

    op.execute("UPDATE iic_sequence SET group_id = visit_set_id")
    op.alter_column('iic_sequence', 'group_id', nullable=False)

    # op.drop_table('test')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)
    # op.create_foreign_key(None, 'agc_exposure', 'pfs_visit', ['pfs_visit_id'], ['pfs_visit_id'])
    # op.alter_column('pfs_config', 'pfs_design_id',
    #            existing_type=sa.BIGINT(),
    #            nullable=False,
    #            autoincrement=False)
    # op.alter_column('pfs_config', 'visit0',
    #            existing_type=sa.INTEGER(),
    #            nullable=False,
    #            existing_comment='The first visit of the set',
    #            autoincrement=False)
    # ### end Alembic commands ###


def downgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('pfs_config', 'visit0',
    #            existing_type=sa.INTEGER(),
    #            nullable=True,
    #            existing_comment='The first visit of the set',
    #            autoincrement=False)
    # op.alter_column('pfs_config', 'pfs_design_id',
    #            existing_type=sa.BIGINT(),
    #            nullable=True,
    #            autoincrement=False)
    # op.drop_constraint(None, 'agc_exposure', type_='foreignkey')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    # op.create_table('test',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('value', sa.REAL(), autoincrement=False, nullable=True)
    # )
    # ### end Alembic commands ###