"""initial migration

Revision ID: 84e7120607a6
Revises: 
Create Date: 2022-10-09 18:08:53.363477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84e7120607a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_migrate_student',
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=15), nullable=True, comment='姓名'),
    sa.Column('age', sa.SmallInteger(), nullable=True, comment='年龄'),
    sa.Column('sex', sa.Boolean(), nullable=True, comment='性别'),
    sa.Column('email', sa.String(length=128), nullable=True, comment='邮箱地址'),
    sa.Column('money', sa.Numeric(precision=10, scale=2), nullable=True, comment='钱包'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_t_migrate_student_name'), 't_migrate_student', ['name'], unique=False)
    op.create_table('t_migrate_student_address',
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=50), nullable=True, comment='地址名称'),
    sa.Column('province', sa.String(length=50), nullable=True, comment='省份'),
    sa.Column('city', sa.String(length=50), nullable=True, comment='城市'),
    sa.Column('area', sa.String(length=50), nullable=True, comment='地区'),
    sa.Column('address', sa.String(length=500), nullable=True, comment='详细地址'),
    sa.Column('mobile', sa.String(length=15), nullable=True, comment='收货人电话'),
    sa.Column('student_id', sa.Integer(), nullable=True, comment='student外键'),
    sa.ForeignKeyConstraint(['student_id'], ['t_migrate_student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_migrate_student_address')
    op.drop_index(op.f('ix_t_migrate_student_name'), table_name='t_migrate_student')
    op.drop_table('t_migrate_student')
    # ### end Alembic commands ###