from random import choice

cards = [face+suit for face in 'AKQJT98765432' for suit in 'cdhs']
print(choice(cards))
