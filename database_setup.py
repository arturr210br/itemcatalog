''' Whole project is based on the Udacity FSND course materials'''

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Division(Base):
    __tablename__ = 'division'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    driver = relationship('Driver', cascade='all, delete-orphan')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Driver(Base):
    __tablename__ = 'driver'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(5250))
    country = Column(String(200))
    rank = Column(String(8))
    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship(Division)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'country': self.country,
            'rank': self.rank,
        }


engine = create_engine('sqlite:///division.db')


Base.metadata.create_all(engine)
