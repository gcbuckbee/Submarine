# ---------------------------------------------------------------------------------
# Created 2016-Oct-31
# G. Buckbee
# ---------------------------------------------------------------------------------
# Card Game Objects, including:
#   * Card
#   * Card Collection (parent of:)
#      * Deck
#      * Hand
#   * Table
#   * Spot (a location on the table where cards can be shown)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
from random import shuffle
from operator import itemgetter, attrgetter, methodcaller


# =================================================================================
# Card Object
# =================================================================================
class Card:
    def __init__(self, Rank, Suit):
        self.faceUp = True
        self.faceDown = False
        self.suit = Suit
        self.rank = Rank
        self.cardValue = 0
        if self.suit == "Clubs" or self.suit == "Spades":
            self.color = "Black"
        else:
            self.color = "Red"

        # Assign cardValue for sorting and for hand ranks
            
        if self.rank == 'Ace':
            self.cardValue = 1
        elif self.rank == 'Two':
            self.cardValue = 2
        elif self.rank == 'Three':
            self.cardValue = 3
        elif self.rank == 'Four':
            self.cardValue = 4
        elif self.rank == 'Five':
            self.cardValue = 5
        elif self.rank == 'Six':
            self.cardValue = 6
        elif self.rank == 'Seven':
            self.cardValue = 7
        elif self.rank == 'Eight':
            self.cardValue = 8
        elif self.rank == 'Nine':
            self.cardValue = 9
        elif self.rank == 'Ten':
            self.cardValue = 10
        elif self.rank == 'Jack':
            self.cardValue = 11
        elif self.rank == 'Queen':
            self.cardValue = 12
        elif self.rank == 'King':
            self.cardValue = 13

        # Assign aceValue = 14 for ranking Ace highest
        
        if self.rank == "Ace":
            self.aceValue = 14
        else:
            self.aceValue = self.cardValue
            

        return
    
            
    def flip():
        return
        
    def draw():
        return
        

# =================================================================================
# Card Collection Object
#   A collection of cards, in sequence
# =================================================================================
class CardCollection:
    @classmethod
    def __init__(self):
        self.cards = []
        return
        
    def shuffle_cards(self):
        shuffle(self.cards)
        return

    def sort_cards(self, Key):
        if Key == "Rank":
            # sort based on Rank
            # Note use cardValue rather than alphabetical by Rank 
            self.cards.sort(key = attrgetter('cardValue'))
        elif Key == "Suit":
            # sort based on Suit
            self.cards.sort(key = attrgetter('suit'))
        elif Key == "Both":
            # sort based on both ranks and suit
            # (A234 of spades, then clubs, the hearts, then diamonds
            self.cards.sort(key = attrgetter('cardValue'))            
            self.cards.sort(key = attrgetter('suit'))
        elif Key == "AceHigh":
            #sort by rank with Ace as high card
            self.cards.sort(key = attrgetter('aceValue'))
        return

    def print_cards(self):
        for card in self.cards:
            eachCard = card
            print(eachCard.rank, "of", eachCard.suit, '=', eachCard.cardValue)        
        
    def addCard(self, cardName):
        self.cards.append(cardName)
        return
        
    def removeCard(self, index):
        del self.cards[index]
        return

    def dealCard(self, index):
        cardDealt = self.cards[index]
        self.removeCard(index)
        return cardDealt

    def count_cards(self):
        return len(self.cards)

        
    def draw():
    # Drawing on the screen....not to be confused with drawing a card from the deck...
        return
        
# =================================================================================
# Deck Object
# =================================================================================
class Deck(CardCollection) :
    def __init__(self):
        super().__init__()
        # create 52 card deck
        ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
        suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
        for suit in suits:
            for rank in ranks:
                newCard = Card(rank, suit)
                self.cards.append(newCard) 
        return

        
# =================================================================================
# Hand Object
# =================================================================================
class Hand(CardCollection):

    def dummy():
        return

    def evaluate(self):
    # Evaluate a hand, to determine its value
    # Hand values are, highest to lowest:
    #   Royal Flush
    #   Four of a kind
    #   Straight Flush
    #   Full House
    #   Flush
    #   Straight
    #   Three of a Kind
    #   Two Pair
    #   Pair
    #   High Card
        result = ""

        # First, determine if that there are 5 cards
        if self.countCards() != 5 :
            return 'Wrong Hand Size'
        if self.containsFlush():
            result = 'Flush'

        # Next, start checking from highest possible hand
        return result

    def containsStraight(self):
        return False

    def containsFlush(self):
        # Determine if all cards are the samesuit
        allSameSuit = True
        mySuit = self.cards[1].suit
        for thisCard in self.cards:
            if  thisCard.suit != mySuit:
                allSameSuit = False
        return allSameSuit
        


        
# =================================================================================
# Table Object
# =================================================================================
class Table():
    def __init__(self):
        return

# =================================================================================
# Spot Object
# =================================================================================
class Spot():
    def __init__(self):
        return

