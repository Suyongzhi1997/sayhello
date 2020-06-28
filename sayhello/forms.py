# -*- coding: utf-8 -*-
"""
    :author: Super (苏勇智)
    :url:
    :copyright: © 2020 Super
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('消息', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('提交')
