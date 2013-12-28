'''
Created on Dec 26, 2013

@author: Jafnee
'''

from random import choice


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
        print "%s has: %s"%(target['name'], str(target['cards']))
        
    def check_cards(target):
        tp = 0;
        for card in target['cards']:
            tp += card
        if tp == 21:
            print "BLACKJACK!!"
    
    while True:
        draw_card(player)
        draw_card(player)
        print_hand(player)
        check_cards(player)
        draw_card(computer)
        print_hand(computer)
        print "Hit or Stay (h/s)?"
        break
        
if __name__ == "__main__":
    main()