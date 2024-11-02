"""A deck of playing cards"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 3
from fastcore.utils import *
from .card import *

# %% ../nbs/01_deck.ipynb 4
class Deck:
    "A deck of 52 cards not including jokers"
    def __init__(self): self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]
    def __len__(self): return len(self.cards)
    def __str__(self): return ";".join(map(str, self.cards))
    def __contains__(self, card): return card in self.cards
    __repr__=__str__

# %% ../nbs/01_deck.ipynb 13
@patch
def pop(self:Deck,
        idx:int=-1): # The index of the card to remove, defaulting to the last card
    "Remove one card from the deck"
    return self.cards.pop(idx)

# %% ../nbs/01_deck.ipynb 15
@patch
def remove(self:Deck,
           card:Card): # Cadr to remove
    "Remove a specific card from the deck"
    self.cards.remove(card)
