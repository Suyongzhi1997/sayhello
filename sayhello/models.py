# -*- coding: utf-8 -*-
"""
    :author: Super (苏勇智)
    :url:
    :copyright: © 2020 Super
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime

from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
