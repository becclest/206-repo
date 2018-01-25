class Hand(object):
	"""docstring for Hand."""

	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards):
		self.init_cards = []


	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		for card in self.init_cards:
			if card.__str__() not in card_strs:
				total.insert(card.random())
			else:
				return None

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand

	def remove_card(self, card):
		self.init_cards.remove(card)


	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def draw(self, deck):
		for card in deck:
			deck.append(c.__str__())
