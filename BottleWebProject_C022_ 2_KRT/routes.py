"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/method1')
@view('method1')
def contact():
    """Renders the method1 page."""
    return dict(
        title='Method1',
        message='Your method1 page.',
        year=datetime.now().year
    )

@route('/method2')
@view('method2')
def contact():
    """Renders the method2 page."""
    return dict(
        title='Method2',
        message='Your method2 page.',
        year=datetime.now().year
    )

@route('/method3')
@view('method3')
def contact():
    """Renders the method3 page."""
    return dict(
        title='Method3',
        message='Your method3 page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
