#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 van <van@vanleno>
#
# Distributed under terms of the MIT license.

"""

"""
import sqlite3

with sqlite3.connect('blog.db') as connection:
    c = connection.cursor()
    c.execute("""
            CREATE TABLE posts
            (title TEXT, post TEXT)
            """)
    c.execute('INSERT INTO posts VALUES("Good","I\'m good")')
    c.execute('INSERT INTO posts VALUES("Well","I\'m well")')
    c.execute('INSERT INTO posts VALUES("Excellent","I\'m excellent")')
    c.execute('INSERT INTO posts VALUES("Ok","I\'m ok")')
