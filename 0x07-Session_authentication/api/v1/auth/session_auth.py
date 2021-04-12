#!/usr/bin/env python3
"""
Defining SessionAuth Classes
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    Class for SessionAuth inheriting from Auth()
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        if isinstance(user_id, str) is not True:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns User ID based on Session ID
        """
        if session_id is None:
            return None
        if isinstance(session_id, str) is not True:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a user instance based on a cookie value
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(session_cookie)
        usuario = User()
        usuario.get(user_id)
        return usuario

    def destroy_session(self, request=None):
        """
        Deletes the user session, makes a logout
        """
        if request is None: 
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is False:
            return False
        session_id = self.user_id_for_session_id(session_cookie)
        if session_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True