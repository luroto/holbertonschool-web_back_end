#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Type, Dict

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Method for adding new users
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, *args, **kwargs) -> User:
        """
        Method for finding the first user using the keyword arguments
        """
        try:
            lista = self._session.query(User).filter_by(**kwargs).one()
            return lista
        except (AttributeError, NoResultFound, InvalidRequestError) as e:
            raise e

    def update_user(self, *args, **kwargs) -> None:
        """
        Method for updating User instance
        """
        try:
            user = self.find_user_by(kwargs.get('id'))
            if user is not None:
                for key, value in kwargs.items():
                    if key in user.__dict__ and key != 'id':
                        setattr(user, key, value)
        except(ValueError, NoResultFound) as e:
            raise e
