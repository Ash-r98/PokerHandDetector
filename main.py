cardvalues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
suits = ['spade', 'heart', 'club', 'diamond']
handtypes = ['high card', 'pair', 'two pair' ,'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush', 'royal flush']
cardexample = ['a', 'spade']

def sorthand(hand): # Sorts hand by card value, lowest to highest
    sortedhand = []
    for i in range(len(hand)):
        smallestindex = 12 # Ace index
        foundindex = 0
        for j in range(len(hand)):
            index = cardvalues.index(hand[j][0])
            if index < smallestindex:
                smallestindex = index
                foundindex = j
        sortedhand.append(hand.pop(foundindex))
    return sortedhand

def subtractlists(biglist, smalllist): # Remove all elements in small list from big list
    finallist = []
    for i in range(len(biglist)):
        indexflag = True
        for j in range(len(smalllist)):
            if biglist[i] == smalllist[j]:
                indexflag = False
                smalllist[j] = None
        if indexflag:
            finallist.append(biglist[i])
    return finallist

def detectpokerhand(hand): # Parameter of 7 cards list
    handtype = 'high card'
    tophand = []
    remainingcards = []
    spadelist = []
    heartlist = []
    clublist = []
    diamondlist = []

    for i in range(len(hand)):
        match hand[i][1]:
            case 'spade':
                spadelist.append(hand[i])
            case 'heart':
                heartlist.append(hand[i])
            case 'club':
                clublist.append(hand[i])
            case 'diamond':
                diamondlist.append(hand[i])
            case _:
                print("Invalid card")

    suitlists = [sorthand(spadelist), sorthand(heartlist), sorthand(clublist), sorthand(diamondlist)]
    sortedcardlist = sorthand(suitlists[0] + suitlists[1] + suitlists[2] + suitlists[3])

    # Flush detection
    for i in range(len(suitlists)):
        if len(suitlists[i]) >= 5:
            tophand = suitlists[i][-5:]
            straightflushflag = True
            for j in range(1, len(tophand)):
                if cardvalues.index(tophand[j][0]) - cardvalues.index(tophand[j-1][0]) != 1:
                    straightflushflag = False
            if not straightflushflag:
                handtype = 'flush'
            else:
                if tophand[-1][0] == 'a':
                    handtype = 'royal flush'
                else:
                    handtype = 'straight flush'
            remainingcards = subtractlists(sortedcardlist, tophand)
            return handtype, tophand, remainingcards

    # Non-flush hands
    for i in range(sortedcardlist):
        pass




testhand = [['a', 'spade'], ['3', 'spade'], ['7', 'spade'], ['2', 'spade'], ['7', 'spade'], ['7', 'spade']]
print(testhand)
print(detectpokerhand(testhand))