# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 完成一个荷官洗牌发牌给n个玩家的模拟程序
# ------------------------(max to 80 columns)-----------------------------------

import Machine.StandardMachine
import Dealer.Mike

# main
# 从机器取一副新牌并写入一个文件
deck = []
Machine.StandardMachine.create_deck(deck)
print('\n-----------cutting line(1)---------------')
print('--debug: I got a new deck of playing cards, total %d cards, detail is :\n%s' %
      (len(deck), deck))

fname = 'poker01.txt'
Machine.StandardMachine.record_deck(deck, fname)

# 重新从机器拿一副牌，并重新洗牌并将结果写入另一个文件
deck = []
Machine.StandardMachine.create_deck(deck)
Machine.StandardMachine.shuffle_deck(deck)

fname = 'poker02.txt'
Machine.StandardMachine.record_deck(deck, fname)

# 给某个玩家发几张牌
card_num = 5
player1Cards = []
Dealer.Mike.deal_to_a_player(deck, card_num, player1Cards)
print('\n-----------cutting line(2)---------------')
print('--debug: Mike dealed %d cards to first player, detail is :\n%s' %
      (card_num, player1Cards))
print('--debug: Remained %d cards, detail is :\n%s' %
      (len(deck), deck))


# 给多个玩家发牌
# method 1:
print('\n-----------cutting line(3)---------------')
# 重新从机器拿一副牌，并重新洗牌
deck = []
Machine.StandardMachine.create_deck(deck)
Machine.StandardMachine.shuffle_deck(deck)

numOfPlayers = 3
cardsOfPlayer = int(len(deck) / numOfPlayers)
print('--debug: %d players, every one has %d cards.'
      % (numOfPlayers, cardsOfPlayer))

player1Cards = []
Dealer.Mike.deal_to_a_player(deck, cardsOfPlayer, player1Cards)
Machine.StandardMachine.record_deck(player1Cards, 'Player1Cards.txt')

player2Cards = []
Dealer.Mike.deal_to_a_player(deck, cardsOfPlayer, player2Cards)
Machine.StandardMachine.record_deck(player2Cards, 'Player2Cards.txt')

player3Cards = []
Dealer.Mike.deal_to_a_player(deck, cardsOfPlayer, player3Cards)
Machine.StandardMachine.record_deck(player3Cards, 'Player3Cards.txt')


# 给多个玩家发牌
# method 2:
deck = []
Machine.StandardMachine.create_deck(deck)
Machine.StandardMachine.shuffle_deck(deck)

player1Cards = []
player2Cards = []
player3Cards = []
player4Cards = []
Dealer.Mike.deal_to_multi_players(
    deck, player1Cards, player2Cards, player3Cards, player4Cards)

Machine.StandardMachine.record_deck(player1Cards, 'P1.txt')
Machine.StandardMachine.record_deck(player2Cards, 'P2.txt')
Machine.StandardMachine.record_deck(player3Cards, 'P3.txt')
Machine.StandardMachine.record_deck(player4Cards, 'P4.txt')
