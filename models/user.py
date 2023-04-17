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

    if getenv('HBNH_TYPE_STRORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128),
                nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="users",
                cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user",
                cascade="all, delete-orphan")
    else:
        email = ''
        password = ''
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
        """ hash password values """
        self._passsword = pwd
