import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    job_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("jobs.id"))
    code = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    job = orm.relation('Job')