#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import models
import hashlib
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128),
                nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user",
                cascade="all, delete-orphan")
    else:
        email = ''
        _password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """ intializes user """
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """ hash the password """
        self._passsword = pwd
