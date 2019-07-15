# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 发牌员 Mike, 他可以
#   1) 从某副牌中给某人发指定数量的牌
#   2) 按指定人数平均发牌，多余的牌放在一边
# ------------------------(max to 80 columns)-----------------------------------
import random


def deal_to_a_player(a_deck, deal_num, player_cards):
    'Desc: Deal some cards to a player from a deck'
    #player_cards = []
    for i in range(deal_num):
        picked_card = random.choice(a_deck)
        player_cards.append(picked_card)
        a_deck.remove(picked_card)
    # print('\# NOTE: ==debug1: %s' % (player_cards))
    player_cards.sort()
    #print('==debug2: %s' % (player_cards))
    return


def deal_to_multi_players(a_deck, *players_cards):
    'Desc: Deal to multiple players, deal remained cards into first player'
    player_num = len(players_cards)
    total_cards = len(a_deck)
    deal_num = int(total_cards / player_num)
    #print('\n===debug1: %d' % (deal_num))

    for pscs in players_cards:
        deal_to_a_player(a_deck, deal_num, pscs)
        '''
        # fbb ----
        for i in range(deal_num):
            # fbb ----
            picked_card = random.choice(a_deck)
            pscs.append(picked_card)
            a_deck.remove(picked_card)
            # fbe ----
        # fbe ----
        pscs.sort()
        '''

    if len(a_deck) > 0:
        for card in a_deck:
            players_cards[0].append(card)
        a_deck = []
        players_cards[0].sort()

    return
