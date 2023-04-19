#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information """

    __tablename__ = 'reviews'
    """ check for database """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024),
                nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'),
                nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),
                nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """ initialize review """
        super().__init__(*args, **kwargs)
