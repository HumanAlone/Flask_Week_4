"""empty message

Revision ID: 1654c2ae4f35
Revises: 
Create Date: 2021-01-10 03:40:57.265790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1654c2ae4f35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('time', sa.String(length=10), nullable=False),
    sa.Column('goal', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('about', sa.String(length=250), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('picture', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('free', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('about'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('weekday', sa.String(length=3), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers_goals',
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers_goals')
    op.drop_table('bookings')
    op.drop_table('teachers')
    op.drop_table('requests')
    op.drop_table('goals')
    # ### end Alembic commands ###
