# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 完成一个荷官洗牌发牌给n个玩家的模拟程序
# ------------------------(max to 80 columns)-----------------------------------

from my_mods import *
from machine.standard_machine import *
from dealer.Mike import *

# Phase 1 -------------------------------------------------------
# 从机器取一副新牌并写入一个文件
deck = []
create_deck(deck)
fname = 'poker01.txt'
record_deck(deck, fname)

# 完成动作后显示信息
pnt_cut_line(1)
msg = '1st time I got a new deck , total %d cards, detail is :\n%s' % (
    len(deck), deck)
pnt_box(msg)


# Phase 2 -------------------------------------------------------
# 重新从机器拿一副牌，并重新洗牌并将结果写入另一个文件
deck = []
create_deck(deck)
shuffle_deck(deck)
fname = 'poker02.txt'
record_deck(deck, fname)

# 完成动作后显示信息
pnt_cut_line(2)
msg = '2nd I got another new-shuffled deck , total %d cards, detail is :\n%s' % (
    len(deck), deck)
pnt_box(msg)


# Phase 3 -------------------------------------------------------
# 给某个玩家发几张牌
card_num = 5
player1Cards = []
deal_to_a_player(deck, card_num, player1Cards)
fname = 'Player1-Cards.txt'
record_deck(player1Cards, fname)
fname = 'Remained-Deck.txt'
record_deck(deck, fname)

pnt_cut_line(3)
msg = 'Mike dealed %d cards to first player, detail is :\n%s' % (
    card_num, player1Cards)
pnt_box(msg)
msg = 'Remained %d cards, detail is :\n%s' % (len(deck), deck)
pnt_box(msg)

# Phase 3 -------------------------------------------------------
# 给多个玩家发牌
# method 1:
# 重新从机器拿一副牌，并重新洗牌
deck = []
create_deck(deck)
shuffle_deck(deck)

numOfPlayers = 3
cardsOfPlayer = int(len(deck) / numOfPlayers)
msg = '--debug: %d players, every one has %d cards.' % (
    numOfPlayers, cardsOfPlayer)
pnt_box(msg)

player1Cards = []
deal_to_a_player(deck, cardsOfPlayer, player1Cards)
record_deck(player1Cards, 'Player1Cards.txt')

player2Cards = []
deal_to_a_player(deck, cardsOfPlayer, player2Cards)
record_deck(player2Cards, 'Player2Cards.txt')

player3Cards = []
deal_to_a_player(deck, cardsOfPlayer, player3Cards)
record_deck(player3Cards, 'Player3Cards.txt')

# Phase 4 -------------------------------------------------------
# 给多个玩家发牌
# method 2:
deck = []
create_deck(deck)
shuffle_deck(deck)

player1Cards = []
player2Cards = []
player3Cards = []
player4Cards = []
player5Cards = []
deal_to_multi_players(
    deck, player1Cards, player2Cards, player3Cards, player4Cards, player5Cards)

record_deck(player1Cards, 'P1.txt')
record_deck(player2Cards, 'P2.txt')
record_deck(player3Cards, 'P3.txt')
record_deck(player4Cards, 'P4.txt')
record_deck(player5Cards, 'P5.txt')
