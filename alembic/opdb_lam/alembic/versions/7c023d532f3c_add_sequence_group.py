"""add_sequence_group

Revision ID: 7c023d532f3c
Revises: c677f4b7827d
Create Date: 2022-11-01 12:32:08.804372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c023d532f3c'
down_revision = 'c677f4b7827d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sequence_group',
    sa.Column('group_id', sa.Integer(), autoincrement=False, nullable=False, comment='Group identifier'),
    sa.Column('group_name', sa.String(), nullable=True, comment='Group name'),
    sa.Column('created_at', sa.DateTime(), nullable=True, comment='Creation time [YYYY-MM-DDThh:mm:ss]'),
    sa.PrimaryKeyConstraint('group_id')
    )
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)

    op.alter_column('iic_sequence', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_comment='Group identifier')

    op.execute("UPDATE iic_sequence SET group_id = NULL")
    op.create_foreign_key(None, 'iic_sequence', 'sequence_group', ['group_id'], ['group_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'iic_sequence', type_='foreignkey')
    op.alter_column('iic_sequence', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_comment='Group identifier')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    op.drop_table('sequence_group')
    # ### end Alembic commands ###