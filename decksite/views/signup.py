from typing import Optional

from flask import url_for
from flask_babel import gettext

from decksite.data.form import Form
from decksite.views.decklist_form import DecklistForm
from magic.models import Deck


class SignUp(DecklistForm):
    def __init__(self, form: Form, is_closed: bool, person_id: Optional[int], d: Optional[Deck]) -> None:
        super().__init__(form, person_id)
        self.is_closed = is_closed
        if d and d.is_in_current_run():
            deck_url = url_for('deck', deck_id=d.id)
            retire_url = url_for('retire')
            self.signed_up_msg_safe = f'You are already signed up to the league with <a href="{deck_url}">{d.name}</a>. Do you want to <a href="{retire_url}">Retire?</a>'

    def page_title(self) -> str:
        return '{league} Sign Up'.format(league=self.league['name'])

    def TT_MTGOTRADERS_SIGNUP_TIK(self) -> str:
        return gettext('When you complete a five match league run for the first time ever you will get 1 tik credit with MTGO Traders (at the end of the month). This credit will appear when you trade with one of their bots on Magic Online.')

    def TT_MTGO_USERNAME(self) -> str:
        return gettext('Magic Online Username')

    def TT_DECK_NAME(self) -> str:
        return gettext('Deck Name')

    def TT_DECKLIST(self) -> str:
        return gettext('Decklist')

    def TT_ENTER_OR_UPLOAD(self) -> str:
        return gettext('Enter or upload your decklist')

    def TT_SIGNUP(self) -> str:
        return gettext('Sign Up')

    def TT_YOUR_RECENT_DECKS(self) -> str:
        return gettext('Your Recent Decks')

    def TT_CHOOSE_DECK(self) -> str:
        return gettext('Select a recent deck to start from there')
