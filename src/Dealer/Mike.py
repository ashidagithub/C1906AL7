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


def deal_to_a_player(aDeck, num, player_cards):
    'Desc: Deal some cards to a player from a deck'
    #player_cards = []
    for i in range(num):
        picked_card = random.choice(aDeck)
        player_cards.append(picked_card)
        aDeck.remove(picked_card)
    # print('\# NOTE: ==debug1: %s' % (player_cards))
    player_cards.sort()
    #print('==debug2: %s' % (player_cards))
    return


def deal_to_multi_players(aDeck, *players_cards):
    'Desc: Deal to multiple players, deal remained cards into first player'
    playerNum = len(players_cards)
    cardsNum = len(aDeck)
    playerHoldCards = int(cardsNum / playerNum)
    #print('\n===debug1: %d' % (playerHoldCards))

    for pscs in players_cards:
        # fbb ----
        for i in range(playerHoldCards):
            # fbb ----
            picked_card = random.choice(aDeck)
            pscs.append(picked_card)
            aDeck.remove(picked_card)
            # fbe ----
        # fbe ----
        pscs.sort()

    if len(aDeck) > 0:
        for card in aDeck:
            players_cards[0].append(card)
        aDeck = []
        players_cards[0].sort()

    return
