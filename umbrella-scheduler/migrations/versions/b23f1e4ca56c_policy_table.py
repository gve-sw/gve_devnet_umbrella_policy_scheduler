"""policy table

Revision ID: b23f1e4ca56c
Revises: 
Create Date: 2020-11-18 19:36:48.738988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b23f1e4ca56c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('policy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.String(length=10), nullable=True),
    sa.Column('policyId', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('start', sa.String(length=10), nullable=True),
    sa.Column('end', sa.String(length=10), nullable=True),
    sa.Column('target', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_policy_day'), 'policy', ['day'], unique=False)
    op.create_index(op.f('ix_policy_end'), 'policy', ['end'], unique=False)
    op.create_index(op.f('ix_policy_name'), 'policy', ['name'], unique=False)
    op.create_index(op.f('ix_policy_policyId'), 'policy', ['policyId'], unique=False)
    op.create_index(op.f('ix_policy_start'), 'policy', ['start'], unique=False)
    op.create_index(op.f('ix_policy_target'), 'policy', ['target'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_policy_target'), table_name='policy')
    op.drop_index(op.f('ix_policy_start'), table_name='policy')
    op.drop_index(op.f('ix_policy_policyId'), table_name='policy')
    op.drop_index(op.f('ix_policy_name'), table_name='policy')
    op.drop_index(op.f('ix_policy_end'), table_name='policy')
    op.drop_index(op.f('ix_policy_day'), table_name='policy')
    op.drop_table('policy')
    # ### end Alembic commands ###
