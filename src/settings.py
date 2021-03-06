from typing import Final, List, Type
from src.classes.players import _Player, PlayerStopFirst, PlayerStopLast, PlayerStopRandom, PlayerStopWeakAdvantage
from src.classes.decks import _Deck, DeckSimple
from os.path import join


class Deck:
    CLASS: [_Deck] = DeckSimple
    NUM_OF_RED_CARDS: Final[int] = 1000

class Players:
    PLAYERS_TO_EVALUATE: List[Type[_Player]] = [
        PlayerStopFirst,
        PlayerStopLast,
        PlayerStopRandom,
        PlayerStopWeakAdvantage,
    ]


class Evaluate:
    NUM_OF_GAMES: int = 1000


class Files:
    OUTPUT_DIRPATH: Final[str] = join(
        '..',
        'out'
    )
