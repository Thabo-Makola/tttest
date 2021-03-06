"""added message table

Revision ID: 796c1cef8c89
Revises: f12440e39493
Create Date: 2020-09-04 00:42:20.880704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '796c1cef8c89'
down_revision = 'f12440e39493'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('direct_message', sa.String(length=9204), nullable=True),
    sa.Column('tutor', sa.String(length=15), nullable=True),
    sa.Column('lecturer', sa.String(length=15), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lecturer'], ['lecture.employee_number'], ),
    sa.ForeignKeyConstraint(['tutor'], ['tutor.id_number'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###
