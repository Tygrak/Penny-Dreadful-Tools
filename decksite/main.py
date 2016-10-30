import os

from flask import Flask, request, send_from_directory

from magic import oracle

from decksite.data import deck, people as ps
from decksite.views import AddForm, Card, Cards, Deck, Home, People, Person

APP = Flask(__name__)

@APP.route('/')
def home():
    view = Home(deck.latest_decks())
    return view.page()

@APP.route('/decks/<deck_id>')
def decks(deck_id):
    view = Deck(deck.load_deck(deck_id))
    return view.page()

@APP.route('/people')
def people():
    view = People(ps.load_people())
    return view.page()

@APP.route('/people/<person_id>')
def person(person_id):
    view = Person(ps.load_person(person_id))
    return view.page()

@APP.route('/cards')
def cards():
    view = Cards(oracle.load_cards())
    return view.page()

@APP.route('/cards/<name>')
def card(name):
    view = Card(oracle.load_cards([name])[0])
    return view.page()

@APP.route('/add')
def add_form():
    view = AddForm()
    return view.page()

@APP.route('/add', methods=['POST'])
def add_deck():
    decks.add_deck(request.form)
    return add_form()

@APP.route('/querytappedout')
def deckcycle_tappedout():
    from decksite.scrapers import tappedout
    if not tappedout.is_authorised():
        tappedout.login()
    tappedout.fetch_decks('penny-dreadful')
    return home()

@APP.route('/favicon<rest>')
def favicon(rest):
    return send_from_directory(os.path.join(APP.root_path, 'static/images/favicon'), 'favicon{rest}'.format(rest=rest))

def init():
    APP.run(host='0.0.0.0', debug=True)
