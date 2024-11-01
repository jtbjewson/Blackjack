import random
import time

name1 = input("Please enter your name. ")

cards_selected = []

class Players:
    def __init__(self, name, win_or_lose):
        self.name = name
        self.win_or_lose = win_or_lose
    def win(self):
        self.win_or_lose = "win"
        print("Congratulations {}. You win!".format(self.name))
    def lose(self):
        self.win_or_lose = "lose"
        print("Unlucky {}! You lost!.".format(self.name))

player1 = Players(name1, "lose")
    
class Cards:
    def __init__(self, name, value, id):
        self.name = name
        self.value = value
        self.id = id
    

cards_list = []
    
clubs_ace = Cards("an ace of clubs", 11, 1)
spades_ace = Cards("an ace of spades", 11, 14)
diamonds_ace = Cards("an ace of diamonds", 11, 27)
hearts_ace = Cards("an ace of hearts", 11, 40)
clubs_2 = Cards("a 2 of clubs", 2, 2)
spades_2 = Cards("a 2 of spades", 2, 15)
diamonds_2 = Cards("a 2 of diamonds", 2, 28)
hearts_2 = Cards("a 2 of hearts", 2, 41)
clubs_3 = Cards("a 3 of clubs", 3, 3)
spades_3 = Cards("a 3 of spades", 3, 16)
diamonds_3 = Cards("a 3 of diamonds", 3, 29)
hearts_3 = Cards("a 3 of hearts", 3, 42)
clubs_4 = Cards("a 4 of clubs", 4, 4)
spades_4 = Cards("a 4 of spades", 4, 17)
diamonds_4 = Cards("a 4 of diamonds", 4, 30)
hearts_4 = Cards("a 4 of hearts", 4, 43)
clubs_5 = Cards("a 5 of clubs", 5, 5)
spades_5 = Cards("a 5 of spades", 5, 18)
diamonds_5 = Cards("a 5 of diamonds", 5, 31)
hearts_5 = Cards("a 5 of hearts", 5, 44)
clubs_6 = Cards("a 6 of clubs", 6, 6)
spades_6 = Cards("a 6 of spades", 6, 19)
diamonds_6 = Cards("a 6 of diamonds", 6, 32)
hearts_6 = Cards("a 6 of hearts", 6, 45)
clubs_7 = Cards("a 7 of clubs", 7, 7)
spades_7 = Cards("a 7 of spades", 7, 20)
diamonds_7 = Cards("a 7 of diamonds", 4, 33)
hearts_7 = Cards("a 7 of hearts", 7, 46)
clubs_8 = Cards("an 8 of clubs", 8, 8)
spades_8 = Cards("an 8 of spades", 8, 21)
diamonds_8 = Cards("an 8 of diamonds", 8, 34)
hearts_8 = Cards("an 8 of hearts", 8, 47)
clubs_9 = Cards("a 9 of clubs", 9, 9)
spades_9 = Cards("a 9 of spades", 9, 22)
diamonds_9 = Cards("a 9 of diamonds", 9, 35)
hearts_9 = Cards("a 9 of hearts", 9, 48)
clubs_10 = Cards("a 10 of clubs", 10, 10)
spades_10 = Cards("a 10 of spades", 10, 23)
diamonds_10 = Cards("a 10 of diamonds", 10, 36)
hearts_10 = Cards("a 10 of hearts", 10, 49)
clubs_jack = Cards("a jack of clubs", 10, 11)
spades_jack = Cards("a jack of spades", 10, 24)
diamonds_jack = Cards("a jack of diamonds", 10, 37)
hearts_jack = Cards("a jack of hearts", 10, 50)
clubs_queen = Cards("a queen of clubs", 10, 12)
spades_queen = Cards("a queen of spades", 10, 25)
diamonds_queen = Cards("a queen of diamonds", 10, 38)
hearts_queen = Cards("a queen of hearts", 10, 51)
clubs_king = Cards("a king of clubs", 10, 13)
spades_king = Cards("a king of spades", 10, 26)
diamonds_king = Cards("a king of diamonds", 10, 39)
hearts_king = Cards("a king of hearts", 10, 52)

cards_list.append(clubs_ace)
cards_list.append(clubs_2)
cards_list.append(clubs_3)
cards_list.append(clubs_4)
cards_list.append(clubs_5)
cards_list.append(clubs_6)
cards_list.append(clubs_7)
cards_list.append(clubs_8)
cards_list.append(clubs_9)
cards_list.append(clubs_10)
cards_list.append(clubs_jack)
cards_list.append(clubs_queen)
cards_list.append(clubs_king)
cards_list.append(spades_ace)
cards_list.append(spades_2)
cards_list.append(spades_3)
cards_list.append(spades_4)
cards_list.append(spades_5)
cards_list.append(spades_6)
cards_list.append(spades_7)
cards_list.append(spades_8)
cards_list.append(spades_9)
cards_list.append(spades_10)
cards_list.append(spades_jack)
cards_list.append(spades_queen)
cards_list.append(spades_king)
cards_list.append(diamonds_ace)
cards_list.append(diamonds_2)
cards_list.append(diamonds_3)
cards_list.append(diamonds_4)
cards_list.append(diamonds_5)
cards_list.append(diamonds_6)
cards_list.append(diamonds_7)
cards_list.append(diamonds_8)
cards_list.append(diamonds_9)
cards_list.append(diamonds_10)
cards_list.append(diamonds_jack)
cards_list.append(diamonds_queen)
cards_list.append(diamonds_king)
cards_list.append(hearts_ace)
cards_list.append(hearts_2)
cards_list.append(hearts_3)
cards_list.append(hearts_4)
cards_list.append(hearts_5)
cards_list.append(hearts_6)
cards_list.append(hearts_7)
cards_list.append(hearts_8)
cards_list.append(hearts_9)
cards_list.append(hearts_10)
cards_list.append(hearts_jack)
cards_list.append(hearts_queen)
cards_list.append(hearts_king)



#game starts
index = 0
five_card_trick = "no"
ids = []
playerid1 = random.randint(1,52) 
ids.append(playerid1)
playerid2 = random.randint(1,52)
while playerid2 in ids:
    playerid2 = random.randint(1,52)
ids.append(playerid2)

for card in cards_list:
    if card.id == playerid1:
        playercard1 = card.name
        playercardvalue1 = card.value
for card in cards_list:
    if card.id == playerid2:
        playercard2 = card.name
        playercardvalue2 = card.value

dealerid1 = random.randint(1,52)
while dealerid1 in ids:
    dealerid1 = random.randint(1,52)
ids.append(dealerid1)

dealerid2 = random.randint(1,52)
while dealerid2 in ids:
    dealerid2 = random.randint(1,52)
ids.append(dealerid2)

for card in cards_list:
    if card.id == dealerid1:
        dealercard1 = card.name
        dealercardvalue1 = card.value
for card in cards_list:
    if card.id == dealerid2:
        dealercard2 = card.name
        dealercardvalue2 = card.value


#hit or stick
readiness = "no"
value_list = []
value_list.append(playercardvalue1)
value_list.append(playercardvalue2)
print("Welcome to the blackjack table {}!".format(name1))
while readiness.lower() == "no":
    readiness = input("Are you ready to play a game? ")

if readiness.lower() == "yes":
    player_total = playercardvalue1 + playercardvalue2
    dealer_total = dealercardvalue1
    print("Great! You have {} and {} in your hand.".format(playercard1, playercard2))
    print("Your dealer has " + dealercard1)
    hit_or_stick = input("Would you like to hit or stick? ")
# make function that converts ace value to 1 if 21 is exceeded by player_total and ace in hand
    if hit_or_stick.lower() == "hit":
        playerid3 = random.randint(1,52)
        while playerid3 in ids:
            playerid3 = random.randint(1,52)
        ids.append(playerid3)
        for card in cards_list:
            if card.id == playerid3:
                playercard3 = card.name
                playercardvalue3 = card.value
        player_total += playercardvalue3
        value_list.append(playercardvalue3)
        if player_total > 21 and 11 in value_list:
            index = 0
            for i in value_list:
                if i == 11:
                    value_list[index] = 1
                    player_total -= 10
                index += 1
        if player_total <= 21:
            print("You have {}, {} and {}".format(playercard1, playercard2, playercard3))
            print("Your dealer has " + dealercard1)
            hit_or_stick = input("Would you like to hit or stick? ")

        else: 
            print("You have {}, {} and {}".format(playercard1, playercard2, playercard3))
            print("You went bust.")
            hit_or_stick = "lose"
    
        
        if hit_or_stick.lower() == "hit":
            playerid4 = random.randint(1,52)
            while playerid4 in ids:
                playerid4 = random.randint(1,52)
            ids.append(playerid4)
            for card in cards_list:
                if card.id == playerid4:
                    playercard4 = card.name
                    playercardvalue4 = card.value
            player_total += playercardvalue4
            value_list.append(playercardvalue4)
        
            if player_total > 21 and 11 in value_list:
                index = 0
                for i in value_list:
                    if i == 11:
                        value_list[index] = 1
                        player_total -= 10
                    index += 1
            if player_total <= 21:
                print("You have {}, {}, {} and {}".format(playercard1, playercard2, playercard3, playercard4))
                print("Your dealer has " + dealercard1)
                hit_or_stick = input("Would you like to hit or stick? ")
            else:
                print("You have {}, {}, {} and {}".format(playercard1, playercard2, playercard3, playercard4))
                print("You went bust.")
                hit_or_stick = "lose"
        
                
            if hit_or_stick.lower() == "hit":
                playerid5 = random.randint(1,52)
                while playerid5 in ids:
                    playerid5 = random.randint(1,52)
                ids.append(playerid5)
                for card in cards_list:
                    if card.id == playerid5:
                        playercard5 = card.name
                        playercardvalue5 = card.value
                player_total += playercardvalue5
                value_list.append(playercardvalue5)
                if player_total > 21 and 11 in value_list:
                    index = 0
                    for i in value_list:
                        if i == 11:
                            value_list[index] = 1
                            player_total -= 10
                        index += 1
                if player_total <= 21:
                    print("You have {}, {}, {}, {} and {}.".format(playercard1, playercard2, playercard3, playercard4, playercard5))
                    print("You have a five card trick!")   
                    hit_or_stick = "stick" 
                    five_card_trick = "yes"         
                else:
                    print("You have {}, {}, {}, {} and {}.".format(playercard1, playercard2, playercard3, playercard4, playercard5))
                    print("You went bust.")
                    hit_or_stick = "lose"
        
    if hit_or_stick == "stick":
        print("Your dealer has {} and {}.".format(dealercard1, dealercard2))
#dealer card process.
        time.sleep(3)
        dealer_value_list = []
        dealer_total = dealercardvalue1 + dealercardvalue2
        if dealer_total < player_total or five_card_trick == "yes":
            dealerid3 = random.randint(1,52)
            while dealerid3 in ids:
                dealerid3 = random.randint(1,52)
            ids.append(dealerid3)
            for card in cards_list:
                if card.id == dealerid3:
                    dealercard3 = card.name
                    dealercardvalue3 = card.value
            dealer_total += dealercardvalue3
            dealer_value_list.append(dealercardvalue3)
            if dealer_total >  21 and 11 in dealer_value_list:
                index = 0
                for i in dealer_value_list:
                    if i == 11:
                        value_list[index] = 1
                        player_total -= 10
                    index += 1
            if dealer_total <= 21:
                time.sleep(5)
                print("your dealer gets {}. He now has {}, {} and {}.".format(dealercard3, dealercard1, dealercard2, dealercard3))
                if dealer_total < player_total or five_card_trick == "yes":
                    dealerid4 = random.randint(1,52)
                    while dealerid4 in ids:
                        dealerid4 = random.randint(1,52)
                    ids.append(dealerid4)
                    for card in cards_list:
                        if card.id == dealerid4:
                            dealercard4 = card.name
                            dealercardvalue4 = card.value
                    dealer_total += dealercardvalue4
                    dealer_value_list.append(dealercardvalue4)
                    if dealer_total >  21 and 11 in dealer_value_list:
                        index = 0
                        for i in dealer_value_list:
                            if i == 11:
                                value_list[index] = 1
                                player_total -= 10
                            index += 1
                    if dealer_total <= 21:
                        time.sleep(5)
                        print("Your dealer gets {}. He now has {}, {}, {} and {}.".format(dealercard4, dealercard1, dealercard2, dealercard3, dealercard4))
                        time.sleep(5)
                        if dealer_total < player_total or five_card_trick == "yes":
                            dealerid5 = random.randint(1,52)
                            while dealerid5 in ids:
                                dealerid5 = random.randint(1,52)
                            ids.append(dealerid5)
                            for card in cards_list:
                                if card.id == dealerid5:
                                    dealercard5 = card.name
                                    dealercardvalue5 = card.value
                            dealer_total += dealercardvalue5
                            dealer_value_list.append(dealercardvalue5)
                            if dealer_total > 21 and 11 in dealer_value_list:
                                index = 0
                                for i in dealer_value_list:
                                    if i == 11:
                                        value_list[index] = 1 
                                        player_total -= 10
                                    index += 1
                            if dealer_total <= 21:
                                time.sleep(6)
                                print("The dealer gets {}. Now he has {}, {}, {}, {} and {}.".format(dealercard5, dealercard1, dealercard2, dealercard3, dealercard4, dealercard5)) 
                                print("The dealer has a five card trick.")
                                time.sleep(5)
                                player1.lose()

                            if dealer_total > 21:
                                time.sleep(3)
                                print("The dealer gets {}. Now he has {}, {}, {}, {} and {}.".format(dealercard5, dealercard1, dealercard2, dealercard3, dealercard4, dealercard5))
                                print("The dealer has gone bust.")
                                time.sleep(5)
                                player1.win()
                        else: 
                            time.sleep(5)
                            player1.lose()
                    if dealer_total > 21 and player1.win_or_lose != "win":
                        time.sleep(3)
                        print("Your dealer gets {}. He now has {}, {}, {} and {}.".format(dealercard4, dealercard1, dealercard2, dealercard3, dealercard4))
                        print("The dealer has gone bust.")
                        time.sleep(5)
                        player1.win()
                else:
                    time.sleep(5) 
                    player1.lose()
            if dealer_total > 21 and player1.win_or_lose != "win":
                time.sleep(3)
                print("your dealer gets {}. He now has {}, {} and {}.".format(dealercard3, dealercard1, dealercard2, dealercard3))
                print("The dealer has gone bust.")
                time.sleep(5)
                player1.win()
        else: 
            time.sleep(5)
            player1.lose()

            
        
            
                