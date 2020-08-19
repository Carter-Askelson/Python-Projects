import random
import sys

chips = 1000
final_value = 0
def script():
    string_hand = []
    pay_in = 100
    blackjack = False
    global chips
    class Card(object):
        suits = ["Spades",
                 "Hearts",
                 "Diamonds",
                 "Clubs"]

        values = [None, None, "2", "3",
                  "4", "5", "6", "7",
                  "8", "9", "10",
                  "Jack", "Queen",
                  "King", "Ace"]

        def __init__(self, v, s):
            """suit + value are ints"""
            self.value = v
            self.suit = s

        def __repr__(self):
            v = self.values[self.value] + " of " \
             + self.suits[self.suit]
            return v

    class Deck(object):
        def __init__(self):
            self.cards = []
            for i in range(2,15):
                for j in range(4):
                    self.cards.append(Card(i, j))
                random.shuffle(self.cards)

    class Player(object):
        def __init__(self):
            self.player_hand = []
            self.hand_value = 0
            self.almost_bust = 0
        def hit(self):
            self.player_hand.append(deck.cards[-1])
            deck.cards.pop()
            print("You were dealt a ", self.player_hand[-1])
            print()
            string_hand.append(str(self.player_hand[-1]))
            string_hand[-1].replace("[","")
            string_hand[-1].replace("]","")
            string_hand.append("\n")
            if self.player_hand[-1].value in range(11, 14):
                self.hand_value += 10
            elif self.player_hand[-1].value == 14:
                self.hand_value += 11
            else:
                self.hand_value += self.player_hand[-1].value
            if len(self.player_hand) > 1:
                print("Your hand consists of\n", " ".join(string_hand))
            ace_count = " ".join(string_hand).count("Ace")
            if self.hand_value > 21:
                if ace_count > self.almost_bust:
                    print("To prevent a Bust, your Ace became a one\n")
                    self.hand_value -= 10
                    self.almost_bust += 1
                else:
                    bust()
            if self.hand_value == 21:
                if len(self.player_hand) == 2:
                    global blackjack
                    blackjack = True
                    print("Blackjack!\nLets see if the House can match you.")
                else:
                    print("Your hand's value is 21, so you now stand")
                self.stand()
            if len(self.player_hand) > 1:
                show_card()
        def double_down(self):
            global chips
            chips -= pay_in
            print("You slide another ", bet, " chips in and draw one last card")
            print("Current Chip Count:", chips)
            print()
            self.hit()
            self.stand()
        def stand(self):
            global final_value
            final_value += self.hand_value
            endgame()
    class Dealer(object):
        def __init__(self):
            self.dealer_hand = []
            self.table_value = 0
            self.almost_bust = 0
            self.string_house_hand = []
        def hit(self):
            self.dealer_hand.append(deck.cards[-1])
            deck.cards.pop()
            self.string_house_hand.append(str(self.dealer_hand[-1]))
            self.string_house_hand[-1].replace("[","")
            self.string_house_hand[-1].replace("]","")
            self.string_house_hand.append("\n")
            if len(self.dealer_hand) == 1:
                print("The Dealer starts the Game\nThe Dealer drew a card and laid it face-down\n")
            else:
                print("The Dealer drew a ", self.dealer_hand[-1])
                print()
            if self.dealer_hand[-1].value in range(11, 14):
                self.table_value += 10
            elif self.dealer_hand[-1].value == 14:
                self.table_value += 11
            else:
                self.table_value += self.dealer_hand[-1].value
        def endgame(self):
            global chips
            print("The Dealer flips the House's face-down card and it is: ", self.dealer_hand[0])
            print("The House's hand consists of\n", " ".join(self.string_house_hand))
            while self.table_value < 17:
                self.hit()
                print("The House's hand consists of\n", " ".join(self.string_house_hand))
                ace_count = " ".join(self.string_house_hand).count("Ace")
                if self.table_value > 21:
                    if ace_count > self.almost_bust:
                        print("To prevent a Bust, the House's Ace became a one\n")
                        self.table_value -= 10
                        self.almost_bust += 1
                        continue
                    print("The House Busted at: ", self.table_value)
                    print()
                    print("You won!")
                    if blackjack == True:
                        chips += bet * 2.5
                    else:
                        chips += bet * 2
                    restart()
            print("The House stood at: ", self.table_value, "And you stood at: ", final_value)
            print()
            if final_value - self.table_value > 0:
                print("You won!")
                chips += bet * 2
                restart()
            else:
                if final_value == self.table_value:
                    print("The House always wins ties.")
                print("Sorry, you lose.")
                restart()
    deck = Deck()
    player1 = Player()
    dealer = Dealer()
    def show_card():
        print("The Dealer's face-up card is a\n ", dealer.dealer_hand[-1])
    def endgame():
        dealer.endgame()
    def restart():
        global final_value
        final_value = 0
        dealer.table_value = 0
        print("Your Chip count is: ", chips)
        if chips < pay_in:
             print("You are broke and don't have the chips for the pay-in for this table.")
             sys.exit()
        while True:
            restart_game = input("Would you like to play again or Cashout? (y/n): ")
            restart_game = restart_game.lower()
            print()
            if restart_game == "y" or restart_game == "yes":
                script()
            elif restart_game == "n" or restart_game == "no":
                print("We'll deal you out.  Thanks for playing!")
                sys.exit()
            else:
                print("Invalid Input.")
    def bust():
        print("Sorry you busted!")
        restart()
    print("Starting a game of Blackjack, the Computer will be the Dealer.")
    print("The Dealer gestures and says \"The pay-in for this table is", pay_in,"chips.\"\n")
    if chips < pay_in:
        print("Your chip count is:", chips)
        print("\nThe Dealer puts his deck of cards down and mutters \"How 'bout you head on home?  Lady Luck obviously doesn't got your back today.\"")
        sys.exit()
    print("Your chip count is:", chips)
    while True:
        bet = input("What's your bet? ")
        if bet == "walk away" or bet == "walk out" or bet == "cash out":
            print("\nThe Dealer shrugs his shoulders and quips \"You'll be back, people like you always do.\"")
            sys.exit()
        bet = int(bet)
        if bet < pay_in:
            print("\nThe Dealer rolls his eyes and grunts \"You gotta pay if you wanna play at my table.\"\n")
        elif bet >= pay_in:
            print("\nThe Dealer grins, nods his head, and starts shuffling the cards.\n")
            break
        else:
            print("\nInvalid Input\n")
    print("The moves you can make are:\n \nH = Hit. Take another card from the Dealer.\n    If you get 21 and the House doesn't, you win! \n    Careful! If your hand goes over 21 you lose!")
    print()
    print("S = Stand. Stop taking cards.\n    You are betting that your hand will be closer to 21 before the House's hand busts, (goes over 21) or stands.")
    print()
    print("D = Double Down. Double your bet and draw one more card before Standing.")
    print("______________________________________________________________________________________")
    print()
    
    chips -= bet
    dealer.hit()
    player1.hit()
    dealer.hit()
    player1.hit()
    while True:
        print()
        player_move = input("H = Hit, D = Double Down, S = Stand: ")
        if player_move == "H" or player_move == "h":
            print("You chose to Hit")
            print()
            player1.hit()
        elif player_move == "D" or player_move == "d":
            print("You chose to Double Down")
            print()
            player1.double_down()
        elif player_move == "S" or player_move == "s":
            print("You chose to Stand")
            print()
            player1.stand()
        else:
            print("Invalid Input.")
            print()

script()
