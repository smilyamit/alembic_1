from __future__ import with_statement
from alembic import op
import sqlalchemy as sa
from alembic.context import get_context  # Import get_context

# Get the Alembic context
context = get_context()



revision = "ef5ec72c6065"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create the student_info table
    op.create_table(
        'student_info',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('age', sa.String),
        sa.Column('score', sa.Integer)
    )

    # Create the course_info table
    op.create_table(
        'course_info',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('course_name', sa.String)
    )

def downgrade():
    # Drop the student_info table
    op.drop_table('student_info')

    # Drop the course_info table
    op.drop_table('course_info')
