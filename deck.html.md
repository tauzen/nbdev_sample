# Deck


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

------------------------------------------------------------------------

<a
href="https://github.com/tauzen/nbdev_sample/blob/main/nbdev_sample/deck.py#L13"
target="_blank" style="float:right; font-size:smaller">source</a>

### Deck

>      Deck ()

*A deck of 52 cards not including jokers*

When we initially create a deck, all of the cards will be present:

``` python
deck = Deck()
deck
```

    A♣️;2♣️;3♣️;4♣️;5♣️;6♣️;7♣️;8♣️;9♣️;10♣️;J♣️;Q♣️;K♣️;A♦️;2♦️;3♦️;4♦️;5♦️;6♦️;7♦️;8♦️;9♦️;10♦️;J♦️;Q♦️;K♦️;A♥️;2♥️;3♥️;4♥️;5♥️;6♥️;7♥️;8♥️;9♥️;10♥️;J♥️;Q♥️;K♥️;A♠️;2♠️;3♠️;4♠️;5♠️;6♠️;7♠️;8♠️;9♠️;10♠️;J♠️;Q♠️;K♠️

That should be 52 cards

``` python
test_eq(len(deck), 52)
```

As a reminder, these are the suits we defined for
[`Card`](https://tauzen.github.io/nbdev_sample/card.html#card)

``` python
suits
```

    ['♣️', '♦️', '♥️', '♠️']

We can check if the Ace of Clubs is in the deck:

``` python
Card(1, 1) in deck
```

    True

------------------------------------------------------------------------

<a
href="https://github.com/tauzen/nbdev_sample/blob/main/nbdev_sample/deck.py#L23"
target="_blank" style="float:right; font-size:smaller">source</a>

### Deck.pop

>      Deck.pop (idx:int=-1)

*Remove one card from the deck*

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>Type</strong></th>
<th><strong>Default</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>idx</td>
<td>int</td>
<td>-1</td>
<td>The index of the card to remove, defaulting to the last card</td>
</tr>
</tbody>
</table>

``` python
deck = Deck()
test_eq(deck.pop(), Card(3, 13))
```

------------------------------------------------------------------------

<a
href="https://github.com/tauzen/nbdev_sample/blob/main/nbdev_sample/deck.py#L30"
target="_blank" style="float:right; font-size:smaller">source</a>

### Deck.remove

>      Deck.remove (card:nbdev_sample.card.Card)

*Remove a specific card from the deck*

<table>
<thead>
<tr class="header">
<th></th>
<th><strong>Type</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>card</td>
<td>Card</td>
<td>Cadr to remove</td>
</tr>
</tbody>
</table>

``` python
card23 = Card(2, 3)
deck.remove(card23)

assert card23 not in deck
```