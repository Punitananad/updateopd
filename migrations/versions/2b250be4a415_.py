"""empty message

Revision ID: 2b250be4a415
Revises: cac3d335705c
Create Date: 2024-08-28 00:45:32.063302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b250be4a415'
down_revision = 'cac3d335705c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medicine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('dosage', sa.String(length=50), nullable=False),
    sa.Column('frequency', sa.String(length=50), nullable=False),
    sa.Column('duration', sa.String(length=50), nullable=False),
    sa.Column('remarks', sa.String(length=200), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patient_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medicine')
    # ### end Alembic commands ###
