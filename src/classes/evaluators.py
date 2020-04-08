from __future__ import annotations
from typing import List, Type
from src.classes.players import _Player
from src.classes.results import _ResultsOfGame, ResultsOfGameSimple, _ResultsOfEvaluator, ResultsOfEvaluatorSimple
from src.classes.games import GameSimple, _Deck, DeckSimple
from src.classes import utils
from src import settings
from typing import Final
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
import sys

# class _EvaluatorConfig(ABC):
#     pass


# class EvaluatorConfigSimple(_EvaluatorConfig):
#     num_of_red_cards: Final[int] = settings.Deck.NUM_OF_RED_CARDS
#     players_to_evaluate: Final[List[Type[_Player]]] = settings.Evaluate.PLAYERS_TO_EVALUATE
#     num_of_games: Final[int] = settings.Evaluate.NUM_OF_GAMES
#     evaluation_unique_name: Final[str] = utils.generate_unique_filename()
#     deck_class: Final[DeckSimple] = DeckSimple
    # deck_class: Final[DeckSimple] = DeckSimple(
    #     num_of_red_cards=num_of_red_cards
    # )


class _Evaluator(ABC):
    def __init__(
            # self,
            # config: _EvaluatorConfig
            self
    ) -> None:
        # self._config = config
        self._results: _ResultsOfEvaluator = self._get_empty_results()

    @abstractmethod
    def get_results(self) -> _ResultsOfEvaluator:
        pass

    @abstractmethod
    def _get_empty_results(self) -> _ResultsOfEvaluator:
        pass



class EvaluatorSimple(_Evaluator):
    """

    """
    def get_results(self) -> ResultsOfEvaluatorSimple:
        # num_of_games: int = self._config.num_of_games
        # deck_class: Final[Type[_Deck]] = self._config.deck_class
        # num_of_red_cards: Final[int] = self._config.num_of_red_cards
        # players_to_evaluate: List[Type[_Player]] = self._config.players_to_evaluate
        num_of_games: int = settings.Evaluate.NUM_OF_GAMES
        deck_class: Final[Type[_Deck]] = settings.Deck.CLASS
        num_of_red_cards: Final[int] = settings.Deck.NUM_OF_RED_CARDS
        players_to_evaluate: List[Type[_Player]] = settings.Players.PLAYERS_TO_EVALUATE
        games: List[GameSimple] = [
            GameSimple(
                # deck=deck_class(
                #     num_of_red_cards=num_of_red_cards
                # ),
                deck=deck_class(settings.Deck.NUM_OF_RED_CARDS),
                players=[player() for player in players_to_evaluate]
            ) for _ in range(num_of_games)
        ]
        for game_idx, game in enumerate(games):
            # print('-' * 20)
            # print(f'starting game:', game_idx)
            sys.stdout.write(f'\rGame: {game_idx}')
            sys.stdout.flush()
            game_results: ResultsOfGameSimple = game.get_results()
            self._results.iloc[game_idx, :] = game_results
        return self._results

    def _get_empty_results(self) -> ResultsOfGameSimple:
        players_names = self._get_players_names()
        print('=' * 40)
        print('players:', players_names)
        num_of_players = len(players_names)
        # num_of_games = self._config.num_of_games
        num_of_games = settings.Evaluate.NUM_OF_GAMES
        return pd.DataFrame(
            data=np.zeros((
                num_of_games,
                num_of_players
            )),
            columns=players_names,
            dtype=np.bool
        )

    def _get_players_names(self) -> List[str]:
        # return [type(player).__name__ for player in self._config.players_to_evaluate]
        return [player.__name__ for player in settings.Players.PLAYERS_TO_EVALUATE]