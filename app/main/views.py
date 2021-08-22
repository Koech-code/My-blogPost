from flask import render_template
from . import main

from ..requests import get_quotes

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting quotes
    quotes = get_quotes()
    
    return render_template('index.html', quotes=quotes, )
