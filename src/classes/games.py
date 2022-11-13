from abc import ABC, abstractmethod
from typing import List, Type
from src.classes.players import _Player
from src.classes.cards import CardSimple
from src.classes.decks import _Deck, DeckSimple
from copy import copy
import numpy as np
from itertools import compress

class _Game(ABC):
    def __init__(
            self,
            deck: Type[_Deck],
            players: List[Type[_Player]]
    ) -> None:
        self._deck = deck
        self._players = copy(players)
        self._players_is_in_game = [True] * len(self._players)

    @abstractmethod
    def get_results(self) -> np.ndarray:
        pass


class GameSimple(_Game):
    """
    All cards are SimpleCards (booleans).
    Flags are FlagSimple (a boolean).
    Results are a np.ndarray at the size of the number of players. Each player get a boolean result.
    """
    def get_results(self) -> np.ndarray:
        num_of_players: int = len(self._players)
        results: np.ndarray = np.array(
            np.zeros(num_of_players),
            dtype=np.bool
        )
        card: CardSimple
        player: Type[_Player]
        players: List[Type[_Player]] = self._players
        assert len(players) > 0, 'No players'
        # Each turn
        for card_idx, card in enumerate(self._deck.get_iterable()):
            # Each player plays
            player_idx: int
            for player_idx, player in enumerate(self._players):
                if self._players_is_in_game[player_idx] is True:
                    # If a player raised a FlagSimple (i.e. a `True` variable)
                    if player.play(card) is True:
                        # Save to results if the player was right
                        if card.all():
                            results[player_idx] = True
                        # Remove the player from the list of remain players (this player end his game)
                        self._players_is_in_game[player_idx] = False
                        if sum(self._players_is_in_game) == 0:
                            return results
        assert sum(self._players_is_in_game) == 0, f"Players that didn't raise a Flag, although there're no more cards"
        return results




