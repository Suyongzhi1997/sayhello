# -*- coding: utf-8 -*-
"""
    :author: Super (苏勇智)
    :url:
    :copyright: © 2020 Super
    :license: MIT, see LICENSE for more details.
"""
import click

from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('此操作将删除数据库，是否要继续？', abort=True)
        db.drop_all()
        click.echo('删除表.')
    db.create_all()
    click.echo('初始化数据库.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)
