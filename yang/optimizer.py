from card import Card
from cost import Cost

def getDeck():
    deck = [];
    deck.append(Card("Striking Sliver", Cost(1,0,0,0,0,0), 0));
    deck.append(Card("Striking Sliver", Cost(1,1,1,3,4,3), 0));
    deck.append(Card("Striking Sliver", Cost(1,0,0,0,0,0), 0));
    deck.append(Card("Striking Sliver", Cost(1,0,0,0,0,0), 0));
    deck.append(Card("Striking Sliver", Cost(1,0,0,0,0,0), 0));
    deck.append(Card("Striking Sliver", Cost(1,0,0,0,0,0), 0));
    deck.append(Card("Striking Sliver", Cost(1,0,0,0,0,0), 0));
    return deck;

def main():
    deck = getDeck();
    for card in deck:
        card.printCard();


if  __name__ =='__main__':main()
