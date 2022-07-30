"""empty message

Revision ID: 0966f4b2a718
Revises: 719da49ffb0c
Create Date: 2022-06-04 17:12:03.755036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0966f4b2a718'
down_revision = '719da49ffb0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.Column('password', sa.String(length=500), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('posts',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('users')
    # ### end Alembic commands ###