"""

Revision ID: 7936332cb619
Revises: 316f08c19996
Create Date: 2020-06-28 10:36:01.495200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7936332cb619'
down_revision = '316f08c19996'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_index('ix_menu_order', table_name='menu')
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.create_index('ix_menu_order', 'menu', ['order'], unique=False)
    pass
    # ### end Alembic commands ###
