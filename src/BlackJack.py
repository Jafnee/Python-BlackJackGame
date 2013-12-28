'''
Created on Dec 26, 2013

@author: Jafnee
'''

from random import choice
player_point = 0
computer_point = 0

def main():
    print "Welcome to BLACKJACK!"
    
    
    
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    player = {'name':"player",
              'cards':[],
              'total_points':0
              }
    
    computer = {'name':"computer",
              'cards':[],
              'total_points':0
              }

    def draw_card(target):
        target['cards'].append(choice(cards))
        
    def print_hand(target):
        print "%s has: %s and a hand value of: %d"%(target['name'], str(target['cards']), get_cardval(target))
        
        
    def get_cardval(target):
        tp = 0;
        for card in target['cards']:
            tp += card
        return tp
        
    def check_player():
        tp = get_cardval(player)
       
        if tp == 21:
            print "BLACKJACK!!"
            return "playerwin"
        elif tp >21:
            if 11 in player['cards']:
                player['cards'][player['cards'].index(11)] = 1
            else:
                print "BUST!"
                return "playerlose"
        else:
            return "continue"
    
    def initial_draw():
        draw_card(player)
        draw_card(player)
        draw_card(computer)
        
    #GAME START
    def start_game():
        global player_point
        global computer_point
        can_continue = True
        initial_draw()
        stay = False
        
        while can_continue:
            print_hand(player)
            if check_player() == "playerwin":
                print "you win"
                player_point = player_point + 1
                break
            elif check_player() =="playerlose":
                print "you lose"
                computer_point = computer_point + 1
                break
            print_hand(computer)
            if stay == False:
                user_input=raw_input ("Hit or Stay (h/s)?").lower()
            if user_input == "h":
                draw_card(player)
            elif user_input =="s":
                stay = True
                draw_card(computer)

    
    start_game()
    print "Scores are:\nPlayer: "+str(player_point)+"\nComputer: "+str(computer_point)
    
        
if __name__ == "__main__":
    main()