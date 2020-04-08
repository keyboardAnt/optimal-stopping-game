from abc import ABC, abstractmethod, abstractproperty
from src.classes.cards import _Card, CardSimple
from src.classes.flags import _Flag, FlagSimple
from src import settings


class _Player(ABC):
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @abstractmethod
    def play(self, card: _Card) -> _Flag:
        pass


class PlayerStopFirst(_Player):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # assert '_num_of_red_cards' in kwargs
        # self._num_of_cards_remain: int = 2 * self._num_of_red_cards
        # self._num_of_red_cards_remain: int = self._num_of_red_cards
        self._num_of_cards_remain: int = 2 * settings.Deck.NUM_OF_RED_CARDS
        self._num_of_red_cards_remain: int = settings.Deck.NUM_OF_RED_CARDS

    def play(self, card: CardSimple) -> FlagSimple:
        return True


class PlayerStopLast(_Player):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # assert '_num_of_red_cards' in kwargs
        # self._num_of_cards_remain: int = 2 * set._num_of_red_cards
        # self._num_of_red_cards_remain: int = self._num_of_red_cards
        self._num_of_cards_remain: int = 2 * settings.Deck.NUM_OF_RED_CARDS
        self._num_of_red_cards_remain: int = settings.Deck.NUM_OF_RED_CARDS

    def play(self, card: CardSimple) -> FlagSimple:
        self._num_of_cards_remain -= 1
        while self._num_of_cards_remain > 0:
            return False
        return True


# class PlayerSmart(_Player):
    # def play(self, card: CardSimple) -> FlagSimple:
    #     self._num_of_cards_remain -= 1
    #     if card is True:
    #         self._num_of_red_cards_remain -= 1



    # def _is_at_least_half_of_remain_cards_are_red(self) -> bool:
    #     return self._num_of_red_cards_remain / self._num_of_cards_remain >= .5




