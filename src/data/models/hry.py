from flask_login import UserMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


from ..database import db
from ..mixins import CRUDModel
from ..util import generate_random_token
from ...settings import app_config
from ...extensions import bcrypt


class Hry(CRUDModel, UserMixin):
    __tablename__ = 'hry'

    id = Column(Integer, primary_key=True)
    nazev = Column(String(64), nullable=False, unique=True, index=True, doc="Nazev hry")
    rok = Column(Integer, nullable=False, index=False, doc="Rok vydani")
    vyvojar_id = Column(Integer, ForeignKey('vyvojari.id'))


    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_nazev(nazev):
        return db.session.query(Hry).filter_by(nazev=nazev).scalar()

    # pylint: disable=R0201

