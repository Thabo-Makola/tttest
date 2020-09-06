"""added application table

Revision ID: 8f74c06b992d
Revises: 2df7283702ad
Create Date: 2020-09-02 10:16:16.299850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f74c06b992d'
down_revision = '2df7283702ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('applicaton_id', sa.Integer(), nullable=False),
    sa.Column('motivation', sa.String(length=2048), nullable=False),
    sa.Column('academic_record', sa.String(length=255), nullable=True),
    sa.Column('course', sa.String(length=50), nullable=True),
    sa.Column('tutor', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['course'], ['course.course_code'], ),
    sa.ForeignKeyConstraint(['tutor'], ['tutor.id_number'], ),
    sa.PrimaryKeyConstraint('applicaton_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application')
    # ### end Alembic commands ###