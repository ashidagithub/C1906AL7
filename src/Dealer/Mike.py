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


def deal_to_a_player(aDeck, num, playerCards):
    'Desc: Deal some cards to a player from a deck'
    #playerCards = []
    for i in range(num):
        pickedCard = random.choice(aDeck)
        playerCards.append(pickedCard)
        aDeck.remove(pickedCard)
    # print('\# NOTE: ==debug1: %s' % (playerCards))
    playerCards.sort()
    #print('==debug2: %s' % (playerCards))
    return


def deal_to_multi_players(aDeck, *playersCards):
    'Desc: Deal to multiple players, deal remained cards into first player'
    playerNum = len(playersCards)
    cardsNum = len(aDeck)
    playerHoldCards = int(cardsNum / playerNum)
    #print('\n===debug1: %d' % (playerHoldCards))

    for pscs in playersCards:
        # fbb ----
        for i in range(playerHoldCards):
            # fbb ----
            pickedCard = random.choice(aDeck)
            pscs.append(pickedCard)
            aDeck.remove(pickedCard)
            # fbe ----
        # fbe ----
        pscs.sort()

    if len(aDeck) > 0:
        for card in aDeck:
            playersCards[0].append(card)
        aDeck = []

    return
