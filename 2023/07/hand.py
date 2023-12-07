from enum import Enum
from dataclasses import dataclass, field
from itertools import product

class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1

CARD_VALUE = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}

@dataclass(order=True)
class Hand:
    cards: list = field(compare=False)
    bid: int = field(compare=False)
    def __post_init__(self):
        self.hand_type = self.find_hand_type()
        self.score = self._score()
    
    def find_hand_type(self) -> HandType:
        hand_counts = {card: self.cards.count(card) for card in self.cards}
        max_count = max(hand_counts.values())
        if max_count == 5:
            return HandType.FIVE_OF_A_KIND
        if max_count == 4:
            return HandType.FOUR_OF_A_KIND
        if set(hand_counts.values()) == set([2,3]):
            return HandType.FULL_HOUSE
        if max_count == 3:
            return HandType.THREE_OF_A_KIND
        if sum(v==2 for v in hand_counts.values()) == 2:
            return HandType.TWO_PAIR
        if max_count == 2:
            return HandType.PAIR
        return HandType.HIGH_CARD
    
    def _score(self):
        score = self.hand_type.value
        for card in self.cards:
            score = 20 * score + CARD_VALUE[card]
        return score

JOKER_CARD_VALUE = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}

@dataclass(order=True)
class JokerHand:
    cards: list = field(compare=False)
    bid: int = field(compare=False)
    def __post_init__(self):
        self.hand_type = self.find_hand_type()
        self.score = self._score()
    
    def find_hand_type(self) -> HandType:
        if "J" not in self.cards:
            return Hand(self.cards, self.bid).hand_type
        indexes = [i for i, x in enumerate(self.cards) if x == "J"]
        possible_hands = []
        hand = list(self.cards)
        # no straights, so possible improvements come from more repeats
        considered_values = set(hand)
        for replacements in product(considered_values, repeat=len(indexes)):
            for i, r in zip(indexes, replacements):
                hand[i] = r
            possible_hands.append(Hand(hand, self.bid))
        return max((h.hand_type for h in possible_hands), key=lambda ht: ht.value)
    
    def _score(self):
        score = self.hand_type.value
        for card in self.cards:
            score = 20 * score + JOKER_CARD_VALUE[card]
        return score
