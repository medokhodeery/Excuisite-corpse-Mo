#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 08:56:42 2021

@author: mohammad
"""
import unittest
from typing import List, Dict
from mock import Mock, patch

class ConnectionDatabaseError(Exception):
    """Raised when the database connection fails."""
    pass

class TestDbError(Exception):
    """Raised when a unit test tries to connect to the database."""
    pass


def connect_to_db(connection_string: str):
    """
    Function that connects to the db.
    
    We will not give you access to the DB yet. So mock this function if you want to test it.

    TODO: add a unit test to verify that this function raises a ConnectionDatabaseError when a different connection string than 'test' is provided.
    TODO: add a unit test to verify that this function raises a TestDbError when a different connection string than 'test' is provided.
    """
    print("connection string: ", connection_string)
    if connection_string == "DRIVER={PostgreSQL Unicode};SERVER=www.wikipedia.com;SSL=true;SSLMode=require;DATABASE=wiki;UID=wikiuser;Connect Timeout=180;PWD=ashiknoor ":
        raise TestDbError("ERROR: YOU FORGOT TO MOCK connect_to_db")
    else:
        raise ConnectionDatabaseError("Can't connect to the databse!")




def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:
    """
    Function that gets the list of users from the database and returns them as a list of dict.

    Each user is formatted like that: { 'username': 'jonh Doe', 'birthday': '02/12/1985', 'role': 'admin' }
    The unit test should return at least 20 users.
    The unit test should check that all the users have a username, a birthday and a role.
    """
    db = connect_to_db(connection_string)
    users = db.get_user()
    return users


def add(num_1: int, num_2: int, num_3: int) -> int:
    """
    TODO: Add a unit test that tests ALL THE INT between 1 and 200. Every possibility should be tested! (your test can't use more than 10 lines)
    """
    return num_1 + num_2 + num_3




class TestString(unittest.TestCase):
    def test_connection(self):
        connection_string = Mock()
        #connection_string = input('insert connection string:')
        result = connect_to_db(connection_string)
        self.assertTrue(result)
        

    def  test_add(self):
        for num_1 in range(1,201):
            for num_2 in range (1,201):
                for num_3 in range(1,201):
                    sum = num_1 + num_2 + num_3
                    self.assertEqual(add(num_1,num_2,num_3), sum)
        
        


if __name__ == "__main__":
    unittest.main()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    