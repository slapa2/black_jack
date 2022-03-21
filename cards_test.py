"""Cards Tests"""
import pytest
from cards import Card, CardValue, CardColour, CardsList, Deck, Hand, NoCardsException

# Cards
def test_card_str():
    """ test cards' str magic method"""
    card = Card(CardColour.SPADE, CardValue.ACE)
    assert str(card) == 'A♠'


def test_card_eq():
    """test cards' eq magic method"""
    card_1 = Card(CardColour.SPADE, CardValue.ACE)
    card_2 = Card(CardColour.SPADE, CardValue.ACE)
    card_3 = Card(CardColour.HEART, CardValue.ACE)
    card_4 = Card(CardColour.SPADE, CardValue.KING)

    assert card_1 == card_2
    assert card_1 != card_3
    assert card_1 != card_4


def test_cards_list_add_card():
    """test adding single card to card list"""
    card = Card(CardColour.SPADE, CardValue.ACE)
    card_list = CardsList()
    card_list.add_card(card)
    assert card_list.cards[0] == Card(CardColour.SPADE, CardValue.ACE)


def test_card_list_add_cards():
    """test adding many cards to card list"""
    card_1 = Card(CardColour.SPADE, CardValue.ACE)
    card_2 = Card(CardColour.SPADE, CardValue.KING)
    card_list = CardsList()
    card_list.add_cards([card_1, card_2])

    assert card_list.cards[0] == Card(CardColour.SPADE, CardValue.ACE)
    assert card_list.cards[1] == Card(CardColour.SPADE, CardValue.KING)


def test_card_list_remove_cards():
    """test removing cards from list"""
    card_1 = Card(CardColour.SPADE, CardValue.ACE)
    card_2 = Card(CardColour.SPADE, CardValue.KING)
    card_list = CardsList()
    card_list.add_cards([card_1, card_2])

    removed_cards = card_list.remove_cards()

    assert len(card_list.cards) == 0
    assert removed_cards[0] == Card(CardColour.SPADE, CardValue.ACE)
    assert removed_cards[1] == Card(CardColour.SPADE, CardValue.KING)


def test_take_last_card():
    """test taking last card from CardList"""
    card_1 = Card(CardColour.SPADE, CardValue.ACE)
    card_2 = Card(CardColour.SPADE, CardValue.KING)
    card_list = CardsList()
    card_list.add_cards([card_1, card_2])

    removed_card = card_list.take_last_card()

    assert len(card_list.cards) == 1
    assert card_list.cards[0] == Card(CardColour.SPADE, CardValue.ACE)
    assert removed_card == Card(CardColour.SPADE, CardValue.KING)


def test_shuffle_card_list():
    """test shuffling card list"""

    cards = [
        Card(CardColour.SPADE, CardValue.ACE),
        Card(CardColour.HEART, CardValue.ACE),
        Card(CardColour.DIMOND, CardValue.ACE),
        Card(CardColour.CLUB, CardValue.ACE),
        Card(CardColour.SPADE, CardValue.KING),
        Card(CardColour.HEART, CardValue.KING),
        Card(CardColour.DIMOND, CardValue.KING),
        Card(CardColour.CLUB, CardValue.KING),
        Card(CardColour.SPADE, CardValue.QUEEN),
        Card(CardColour.HEART, CardValue.QUEEN),
        Card(CardColour.DIMOND, CardValue.QUEEN),
        Card(CardColour.CLUB, CardValue.QUEEN),
        Card(CardColour.SPADE, CardValue.JACK),
        Card(CardColour.HEART, CardValue.JACK),
        Card(CardColour.DIMOND, CardValue.JACK),
        Card(CardColour.CLUB, CardValue.JACK)
    ]

    card_list_1 = CardsList()
    card_list_1.add_cards(cards)

    card_list_2 = CardsList()
    card_list_2.add_cards(cards)

    card_list_1.shuffle()

    assert any({x != y for x, y in zip(card_list_1.cards, card_list_2.cards)})


def test_no_cards_exception():
    """test if NoCardsException is risen when no cards ro take"""
    card_list = CardsList()
    with pytest.raises(NoCardsException):
        card_list.take_last_card()


# Deck
def test_adding_standard_52_cards_to_deck():
    """test creating new deck"""
    deck = Deck()
    deck.add_standard_52_cards_deck()
    assert len(deck.cards) == 52

    for card in deck.cards:
        assert deck.cards.count(card) == 1


# Hand
def test_adding_card_from_deck():
    """test adding one card from deck to hand"""
    deck = Deck()
    deck.add_standard_52_cards_deck()

    hand = Hand()
    hand.add_card_from_deck(deck)

    assert len(hand.cards) == 1
    assert len(deck.cards) == 51
    assert deck.cards.count(hand.cards[0]) == 0


def test_adding_many_cards_from_deck():
    """test adding many cards from deck to hand"""
    deck = Deck()
    deck.add_standard_52_cards_deck()

    hand = Hand()
    hand.add_cards_from_deck(deck, 10)

    assert len(hand.cards) == 10
    assert len(deck.cards) == 42

    for card in hand.cards:
        assert deck.cards.count(card) == 0


def test_len_of_hand():
    """test hand len function"""
    deck = Deck()
    deck.add_standard_52_cards_deck()
    hand = Hand()
    hand.add_cards_from_deck(deck, 10)

    assert len(hand) == 10
