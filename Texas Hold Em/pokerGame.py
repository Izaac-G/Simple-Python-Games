import random
# 11 = J, 12 = Q, 13 = K, 14 = A
card_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

face_cards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = Card(face_cards[value], suit)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards
cards = generate_cards()


# Now that we have a deck of cards stored in our 'cards' variable, we can move on to dealing

def deal_cards(cards):
    i = random.randint(0, len(cards)-1)
    card = cards[i]
    cards.pop(i)
    return card, cards

def deal(cards = cards, num_opp = 2):
    opp_hands = []
    for _ in range(num_opp):
        card1, cards = deal_cards(cards)
        card2, cards = deal_cards(cards)
        opp_hands.append([card1, card2])
    card1, cards = deal_cards(cards)
    card2, cards = deal_cards(cards)
    your_hand = [card1, card2]
    return your_hand, opp_hands
your_hand, opp_hands = deal()
print([(card.value, card.suit) for card in your_hand])

def flop(cards=cards):
    card1, cards = deal_cards(cards)
    card2, cards = deal_cards(cards)
    card3, cards = deal_cards(cards)
    return [card1, card2, card3]

def table_deal(cards=cards):
    card, cards = deal_cards(cards)
    return card

table = flop()
print(f"Cards on the table: {[(card.value, card.suit) for card in table]}")
table.append(table_deal())
print(f"Cards after turn: {[(card.value, card.suit) for card in table]}")
table.append(table_deal())
print(f"Cards after river: {[(card.value, card.suit) for card in table]}")

def evaluate(hand, table):
    total_hand = hand + table
    # count values and suits
    counts = {}
    suits = {}
    vals = set()
    # loop through all the card
    for card in total_hand:
        if card.value in face_cards:
            card_value = face_cards[card.value]
        else:
            card_value = card.value
        vals.add(card_value)
        if card_value in counts:
            counts[card_value] += 1
        else:
            counts[card_value] = 1
        if card.suit in suits:
            suits[card.suit] += 1
        else:
            suits[card.suit] = 1
    # sort counts and suits
    sorted_counts = sorted(counts.items(), key=lambda item:(item[1], item[0]), reverse=True)
    sorted_suits = sorted(suits.items(), key=lambda item:(item[1], item[0]), reverse=True)
    
    #Check if vals contains a straight
    run = [sorted(list(vals))[0]]
    lastval = sorted(list(vals))[0]
    is_straight = False
    for val in sorted(list(vals)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straight = True
            break

    #check if sorted_suits contains a flush
    is_flush = False
    if sorted_suits[0][1] == 5:
        is_flush = True

    #Check for straight flush
    if is_straight:
        if is_flush:
            return "Straight Flush!"

    #4 of a kind check
    if sorted_counts[0][1] == 4:
        return f"Quad {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s!"

    #full house check
    if sorted_counts[0][1] == 3:
        if sorted_counts[1][1] == 2:
            return f"Full house {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s over {face_cards.get(sorted_counts[1][0]) if sorted_counts[1][0] in face_cards else sorted_counts[1][0]}s!"
    
    #Flush check
    if is_flush:
        return f"Flush in {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
    #Straight check
    if is_straight:
        return f"Straight! {run}"

    #Check for groups
    if sorted_counts[0][1] == 3:
        return f"Triple {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s!"

    if sorted_counts[0][1] == 2:
        if sorted_counts[1][1] == 2:
            return f"Two pair {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]} and {face_cards.get(sorted_counts[1][0]) if sorted_counts[1][0] in face_cards else sorted_counts[1][0]}!"
        else:
            return f"Pair of {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
        return f"High Card {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"

def determine(hand, opp_hands, table):
    print(f"your highest poker hand: {evaluate(hand, table)}")
    for opp in opp_hands:
        print(f"Opponent hand: {opp[0].value} {opp[0].suit}, {opp[1].value} {opp[1].suit}")
        print(f"Your opponents highest poker hand: {evaluate(opp, table)}")

determine(your_hand, opp_hands, table)
