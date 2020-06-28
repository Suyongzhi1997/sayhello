# -*- coding: utf-8 -*-
"""
    :author: Super (苏勇智)
    :url:
    :copyright: © 2020 Super
    :license: MIT, see LICENSE for more details.
"""
from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('您的消息已发送给全世界！')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)
