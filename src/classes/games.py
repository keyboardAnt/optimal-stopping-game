from abc import ABC, abstractmethod
from typing import List, Type, Iterable
from src.classes.players import _Player
from src.classes.cards import _Card, CardSimple
from src.classes.flags import _Flag, FlagSimple
from copy import copy
import numpy as np


class _Deck(ABC):
    def __init__(
            self,
            num_of_red_cards: int
    ) -> None:
        self._num_of_red_cards = num_of_red_cards
        self._cards: np.ndarray = self._generate()

    @abstractmethod
    def _generate(self) -> np.ndarray:
        """
        Generate the deck.
        """
        pass

    @abstractmethod
    def get_iterable(self) -> Iterable:
        pass


class DeckSimple(_Deck):
    """
    All cards are CardSimple (booleans).
    Exactly half of the cards are red (True).
    Each turn the next card is by ascending index order.
    """

    def _generate(self) -> np.ndarray:
        return np.random.randint(
            2,
            size=self._num_of_red_cards,
            dtype=np.bool
        )

    def get_iterable(self) -> Iterable:
        return self._cards


class _Game(ABC):
    def __init__(
            self,
            deck: Type[_Deck],
            players: List[Type[_Player]]
    ) -> None:
        self._deck = deck
        self._players = players

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
        print('num_of_players:', num_of_players)
        results: np.ndarray = np.array(
            np.zeros(num_of_players),
            dtype=np.bool
        )
        card: CardSimple
        player: Type[_Player]
        remain_players: List[Type[_Player]] = copy(self._players)
        assert len(remain_players) > 0, 'No players'
        # Each turn
        for card_idx, card in enumerate(self._deck.get_iterable()):
            print(f'card {card_idx}:', card)
            # Each player plays
            player_idx: int
            for player_idx, player in enumerate(remain_players):
                # If a player raised a FlagSimple (i.e. a `True` variable)
                if player.play(card) is True:
                    # Save to results if the player was right
                    if card.all():
                        print(f'player {player_idx} won')
                        results[player_idx] = True
                    else:
                        print(f'player {player_idx} lost')
                    # Remove the player from the list of remain players (this player end his game)
                    remain_players.remove(player)
                    print(f'player {player_idx} is out')
                    print(f'len(remain_players):', len(remain_players))
                    #
                    if len(remain_players) == 0:
                        print('All players are out')
                        return results
        return results




