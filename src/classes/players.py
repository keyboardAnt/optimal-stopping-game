from abc import ABC, abstractmethod, abstractproperty
from src.classes.cards import _Card, CardSimple
from src.classes.flags import _Flag, FlagSimple
from src import settings
import numpy as np


class _Player(ABC):
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @abstractmethod
    def play(self, card: _Card) -> _Flag:
        pass


class PlayerStopFirst(_Player):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # self._num_of_total_cards_remain: int = 2 * settings.Deck.NUM_OF_RED_CARDS
        self._num_of_red_cards_remain: int = settings.Deck.NUM_OF_RED_CARDS

    def play(self, card: CardSimple) -> FlagSimple:
        return True


class PlayerStopLast(_Player):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._num_of_total_cards_remain: int = 2 * settings.Deck.NUM_OF_RED_CARDS
        # self._num_of_red_cards_remain: int = settings.Deck.NUM_OF_RED_CARDS

    def play(self, card: CardSimple) -> FlagSimple:
        self._num_of_total_cards_remain -= 1
        while self._num_of_total_cards_remain > 0:
            return False
        return True


class PlayerStopRandom(_Player):
    """
    Pick a random index in [0, # of cards in the deck - 1], and stop then.
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        num_of_cards: int = 2 * settings.Deck.NUM_OF_RED_CARDS
        self._idx: int = 0
        self._random_idx: int = np.random.randint(num_of_cards)

    def play(self, card: CardSimple) -> FlagSimple:
        if self._idx == self._random_idx:
            return True
        self._idx += 1
        return False


class PlayerStopWeakAdvantage(_Player):
    """
    Stop immediately when detecting a small advantage
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._num_of_total_cards_remain: int = 2 * settings.Deck.NUM_OF_RED_CARDS
        self._num_of_red_cards_remain: int = settings.Deck.NUM_OF_RED_CARDS
        self.WEAK_ADVANTAGE = .55

    def play(self, card: CardSimple) -> FlagSimple:
        self._num_of_total_cards_remain -= 1
        if card is True:
            self._num_of_red_cards_remain -= 1
        if self._num_of_red_cards_remain / self._num_of_total_cards_remain > self.WEAK_ADVANTAGE:
            return True
        return False

    # def _is_at_least_half_of_remain_cards_are_red(self) -> bool:
    #     return self._num_of_red_cards_remain / self._num_of_total_cards_remain >= .5




