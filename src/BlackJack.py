'''
Created on Dec 26, 2013

@author: Jafnee
'''

from random import choice
from time import sleep
player_point = 0
computer_point = 0

def main():
    print "Welcome to BLACKJACK!\n\n"
    
    
    
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    player = {'name':"player",
              'cards':[],
              'total_points':0,
              'money':1000
              }
    
    computer = {'name':"computer",
              'cards':[],
              'total_points':0
              }

    def draw_card(target):
        target['cards'].append(choice(cards))
        
    def print_hand(target):
        print "%s has: %s and a hand value of: %d"%(target['name'], str(target['cards']), get_cardval(target))
        
    def print_score():
        print "Scores are:\nPlayer: "+str(player['total_points'])+"\nComputer: "+str(computer['total_points'])

    def play_again():
        if player['money'] > 0:
            again = (raw_input("Play Again? y/n\n")).lower()
        else:
            print "You have no money!"
            again = "n"
        if again == "y":
            start_game()
            print_score()
            sleep(0.5)
            play_again()
        elif again == "n":
            print_score()
            print "Thank you for playing"
        else:
            print "invalid input"
            sleep(0.5)
            play_again()
        
    def get_cardval(target):
        tp = 0;
        for card in target['cards']:
            tp += card
        return tp
    
    def compare_money(bet):
        if bet > player['money']:
            return False
        else:
            return True
    
    def get_money():
        m = player['money']
        return m
    
    def place_bet():
        legal = False
        while legal == False:
            wager = raw_input("Place your bet: \n")
            if wager.isdigit():
                if compare_money(int(wager)):
                    legal = True
                    return int(wager)
                else:
                    print "Enter a valid wager."
            else:
                print "Enter a valid wager."
        
    
    def print_money():
        print "You have $%d"%(player['money'])
        
    def check_player():
        if get_cardval(player) == 21:
            print "BLACKJACK!!"
            sleep(0.5)
            return "playerwin"
        elif get_cardval(player) >21:
            if 11 in player['cards']:
                player['cards'][player['cards'].index(11)] = 1
                print "Changed 11(Ace) to 1"
                print_hand(player)
                sleep(0.5)
            else:
                print "BUST!"
                sleep(0.5)
                return "playerlose"
        else:
            return "continue"
        
        
    def initial_draw():
        draw_card(player)
        draw_card(player)
        draw_card(computer)
        
    #GAME START
    def start_game():
        can_continue = True
        stay = False
        
        player['cards'] = []
        computer['cards'] = []
        print_money()
        if player['money'] > 0:
            player_wager = place_bet()
        else:
            print "You have no money!"
            can_continue = False
        initial_draw()
        while can_continue:
            if player['money'] <= 0:
                print "You have no money!"
                break
            
            sleep(0.5)
            print_hand(player)
            if check_player() == "playerwin":
                print "you win\n"
                sleep(0.5)
                player['total_points'] += 1
                player['money'] += int(player_wager)
                break
            elif check_player() =="playerlose":
                print "you lose\n"
                sleep(0.5)
                computer['total_points'] += 1
                player['money'] -= int(player_wager)
                break
            print_hand(computer)
            if stay == False:
                user_input=raw_input ("Hit or Stay (h/s)?\n").lower()
                if user_input == "h":
                    draw_card(player)
                elif user_input =="s":
                    stay = True
                    draw_card(computer)
                    print_hand(player)
                    sleep(0.5)
                    print_hand(computer)
                    sleep(0.5)
                    while True:
                        if get_cardval(computer) > 21:
                            if 11 in computer['cards']:
                                computer['cards'][computer['cards'].index(11)] = 1
                                print "Changed 11(Ace) to 1"
                            else:
                                print "BUST!"
                                print "you win\n"
                                player['total_points'] += 1
                                player['money'] += int(player_wager)
                                can_continue = False
                                break
                        if get_cardval(computer) > get_cardval(player):
                            print "you lose\n"
                            computer['total_points'] += 1
                            player['money'] -= int(player_wager)
                            can_continue = False
                            break
                        elif get_cardval(computer) <= get_cardval(player):
                            draw_card(computer)
                            print_hand(computer)
                            sleep(0.5)


        
    start_game()
    print_score()
    sleep(0.5)
    play_again()
    
        
if __name__ == "__main__":
    main()