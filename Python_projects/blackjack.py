import random

#to print card in a non-list way
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    #to be able to return a print statement without the "value"
    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'

#create the deck
class Deck:
    def __init__(self):
        self.cards = [] #individual cards
        self.suits = ['diamonds', 'hearts', 'spades', 'clubs']
        self.ranks = [
            {"rank" : "A", "value" : 11},
            {"rank" : "2", "value" : 2},
            {"rank" : "3", "value" : 3},
            {"rank" : "4", "value" : 4},
            {"rank" : "5", "value" : 5},
            {"rank" : "6", "value" : 6},
            {"rank" : "7", "value" : 7},
            {"rank" : "8", "value" : 8},
            {"rank" : "9", "value" : 9},
            {"rank" : "10", "value" : 10},
            {"rank" : "J", "value" : 10},
            {"rank" : "Q",  "value" : 10},
            {"rank" : "K", "value" : 10},
            ]

        #create a each card with suit and rank
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank)) 

    #shuffle cards
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    #dealing cards for the player
    def deal(self, num): 
        cards_dealt = []
        for c in range(num):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

#hand of player or dealer   
class Hand:
    def __init__(self, dealer = False): #set to true or false to keep track of what hand it is;  default value false 
       self.card = []
       self.value = 0
       self.dealer = dealer

    def add_card(self, card_list):
        self.card.extend(card_list)

    def calc_value(self):
        self.value = 0
        has_ace = False

        #computing dealer and player hand and checking for ace
        for card in self.card:
            if card.rank["rank"]:
                card_value = int(card.rank["value"])
                self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        #ace = 1 if over 21
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self): #better to make a separate function to return value 
        self.calc_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer = False):
        print(f'''{"Dealer's'" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.card):
            #to hide the first card of the dealer
            if index == 0 and self.dealer and not show_all_dealer and not self.is_blackjack():
                print("hidden")
            else:    
                print(card)
        if not self.dealer:
            print("Value: ", self.get_value())
            print()
    
class BlackjackGame:
    def play(self):
        game_num = 0
        game_toplay = 0

        while game_toplay <= 0:
            try:
                game_toplay = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number.")
        
        while game_num < game_toplay:
            game_num += 1
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer = True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_num} of {game_toplay}")
            print()
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Hit(h) or stand(s)?  ")
                while choice not in ["h", "s", "stand", "hit"]:
                    choice = input("Please enter a valid choice (hit/h or stand/s): ")
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    print()
                    player_hand.display()
            
            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()

            #dealer deal another card
            while dealer_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_value = dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer = True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand: ", player_value)
            print("Dealer's hand", dealer_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThank you for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win! 🥳")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("You both have blackjack! A Tie. 😶")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack! You win! 🥳")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack! You lose! 😭")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 🥳")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie! 😶")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("You lose! 😭")
        return False

game = BlackjackGame()
game.play()