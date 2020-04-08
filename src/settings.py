from typing import Final, List, Type
from src.classes.players import _Player, PlayerStopFirst
from os.path import join


class Deck:
    NUM_OF_RED_CARDS: Final[int] = 100


class Evaluate:
    PLAYERS_TO_EVALUATE: List[Type[_Player]] = [
        PlayerStopFirst(_num_of_red_cards=Deck.NUM_OF_RED_CARDS),
    ]
    NUM_OF_GAMES: int = 5


class Files:
    OUTPUT_DIRPATH: Final[str] = join(
        '..',
        'out'
    )
