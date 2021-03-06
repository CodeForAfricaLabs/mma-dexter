"""raw-calais

Revision ID: 3e64188fb918
Revises: 3192831a2967
Create Date: 2015-11-18 12:19:08.631483

"""

# revision identifiers, used by Alembic.
revision = '3e64188fb918'
down_revision = '3192831a2967'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('raw_calais', mysql.LONGTEXT(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('documents', 'raw_calais')
    ### end Alembic commands ###
