from typing import Dict

from dis_snek import Snake
from dis_snek.models.application_commands import slash_command
from dis_snek.models.scale import Scale

from discordbot import command
from discordbot.command import MtgContext
from magic import fetcher, seasons
from magic.models import Card
from shared import fetch_tools


class History(Scale):
    @slash_command('history')
    @command.slash_card_option()
    async def history(ctx: MtgContext, card: Card) -> None:
        """Show the legality history of the specified card and a link to its all time page."""
        await ctx.single_card_text(card, card_history, show_legality=False)

    history.autocomplete('card')(command.autocomplete_card)

def card_history(c: Card) -> str:
    data: Dict[int, bool] = {}
    for format_name, status in c.legalities.items():
        if 'Penny Dreadful ' in format_name and status == 'Legal':
            season_id = seasons.SEASONS.index(
                format_name.replace('Penny Dreadful ', '')) + 1
            data[season_id] = True
    # data[seasons.current_season_num()] = c.legalities.get(seasons.current_season_name(), None) == 'Legal'
    s = '   '
    for i in range(1, seasons.current_season_num() + 1):
        s += f'{i} '
        s += ':white_check_mark:' if data.get(i, False) else ':no_entry_sign:'
        s += '   '
    s = s.strip()
    s += '\n<' + fetcher.decksite_url('/seasons/all/cards/{name}/'.format(
        name=fetch_tools.escape(c.name, skip_double_slash=True))) + '>'
    return s

def setup(bot: Snake) -> None:
    History(bot)
