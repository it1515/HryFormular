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

class Vyvojari(CRUDModel, UserMixin):
    __tablename__ = 'vyvojari'

    id = Column(Integer, primary_key=True)
    vyvojar = Column(String(64), nullable=False, unique=True, index=True, doc="Nazev vyvojare")
    pocetTitulu = Column(Integer, nullable=False, index=False, doc="Pocet titulu")
    hry = relationship("Hry")

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_vyvojar(vyvojar):
        return db.session.query(Vyvojari).filter_by(vyvojar=vyvojar).scalar()

    # pylint: disable=R0201

