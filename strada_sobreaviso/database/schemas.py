import datetime as _dt

import sqlalchemy as _sql

from strada_sobreaviso.database import config as _database


class Colaboradores(_database.Base):
    __tablename__ = 'colaboradores'

    id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    name = _sql.Column(_sql.String)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    squad_id = _sql.Column(_sql.ForeignKey('squads.id'))


class Squads(_database.Base):
    __tablename__ = 'squads'

    id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    name = _sql.Column(_sql.String, unique=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
