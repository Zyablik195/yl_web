import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    place = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    day = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    time = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    already = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    max = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)