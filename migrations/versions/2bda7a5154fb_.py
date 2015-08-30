"""empty message

Revision ID: 2bda7a5154fb
Revises: 140557b5dc55
Create Date: 2015-08-29 12:37:36.592814

"""

# revision identifiers, used by Alembic.
revision = '2bda7a5154fb'
down_revision = '140557b5dc55'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('phone', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ride',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_passengers', sa.Integer(), nullable=False),
    sa.Column('start_latitude', sa.Float(), nullable=False),
    sa.Column('start_longitude', sa.Float(), nullable=False),
    sa.Column('end_latitude', sa.Float(), nullable=False),
    sa.Column('end_longitude', sa.Float(), nullable=False),
    sa.Column('pickup_time', sa.DateTime(), nullable=False),
    sa.Column('travel_time', sa.Integer(), nullable=False),
    sa.Column('dropoff_time', sa.DateTime(), nullable=False),
    sa.Column('pickup_address', sa.String(length=255), nullable=False),
    sa.Column('dropoff_address', sa.String(length=255), nullable=False),
    sa.Column('on_campus', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    op.drop_table('ride')
    op.drop_table('user')
    ### end Alembic commands ###