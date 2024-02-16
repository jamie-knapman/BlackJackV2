# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:45:47 2024
Version 2 - Refined
@author: jamie
"""
import random
class Blackjack:
    def __init__(self):
        self.balance = 10000
        self.quit_game = False
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = {
            "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "King": 10, "Queen": 10, "Jack": 10,
            "Ace": 11}
    
    def deal_card(self):
        suit = random.choice(self.suits)
        value = random.choice(list(self.values.keys()))
        return value, suit

    def calculate_total(self, hand):
        total = sum(self.values[card[0]] for card in hand)
        num_aces = sum(1 for card in hand if card[0] == 'Ace')
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1
        return total

    def display_hand(self, hand):
        return ', '.join(f"{value} of {suit}" for value, suit in hand)

    def play(self):
        bet = 0
        while bet <= 0 or bet > self.balance:
            try:
                bet = int(input("Enter your bet (balance: {}): ".format(self.balance)))
            except ValueError:
                print("Invalid input. Please enter a valid bet.")
                continue

        dealer_hand = [self.deal_card(), self.deal_card()]
        dealer_total = self.calculate_total(dealer_hand)
        player_hand = [self.deal_card(), self.deal_card()]
        player_total = self.calculate_total(player_hand)

        print("\nDealer's Hand:", self.display_hand([dealer_hand[0], ("Unknown", "Unknown")]))
        print("Your Hand:", self.display_hand(player_hand), "(Total:", player_total, ")\n")

        while player_total <= 21:
            action = input("Do you want to [H]it, [S]tand, or [D]ouble down? ").upper()
            if action == "H":
                player_hand.append(self.deal_card())
                player_total = self.calculate_total(player_hand)
                print("\nYour Hand:", self.display_hand(player_hand), "(Total:", player_total, ")")
                if player_total >= 21:
                    break
            elif action == "S":
                break
            elif action == "D":
                # Double down: double the bet, receive one more card, then stand
                bet *= 2
                player_hand.append(self.deal_card())
                player_total = self.calculate_total(player_hand)
                print("\nYour Hand:", self.display_hand(player_hand), "(Total:", player_total, ")")
                break
            else:
                print("Invalid action. Please enter 'H', 'S', or 'D'.")
                
        while dealer_total < 17:
            dealer_hand.append(self.deal_card())
            dealer_total = self.calculate_total(dealer_hand)
        print("\nDealer's Hand:", self.display_hand(dealer_hand), "(Total:", dealer_total, ")")

        if player_total > 21:
            print("You busted! Dealer wins.")
            self.balance -= bet
        elif player_total == 21:
            print("You have blackjack! You win!")
            self.balance += bet * 2 + (bet / 2)
        elif dealer_total > 21 or player_total > dealer_total:
            print("You win!")
            self.balance += bet
        elif player_total < dealer_total:
            print("Dealer wins!")
            self.balance -= bet
        else:
            print("It's a tie!")


    def start(self):
        print("Welcome to Blackjack!\n")
        while not self.quit_game:
            print("Main menu:")
            print("Chips to play with:", self.balance)
            print("A - Play")
            print("B - Quit")
            choice = input("Enter your choice: ").upper()
            if choice == "A":
                self.play()
            elif choice == "B":
                self.quit_game = True
                print("Thanks for playing!")
            else:
                print("Invalid choice. Please enter 'A' or 'B'.\n")


if __name__ == "__main__":
    game = Blackjack()
    game.start()