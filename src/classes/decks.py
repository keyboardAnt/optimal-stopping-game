from abc import ABC, abstractmethod
from typing import Iterable
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
        num_of_cards = 2 * self._num_of_red_cards
        return np.random.randint(
            2,
            size=num_of_cards,
            dtype=np.bool
        )

    def get_iterable(self) -> Iterable:
        return self._cards