from app.game import Game
from app.deck import Deck

class Card_Game( Game ):
  """This is a subclass of Game"""
  def __init__(
      self,
      name,
      description,
      card_game_rules,
      players,
      total_players=2,
      max_team_size=1 ):
    
    Game.__init__(self, name, description, players, total_players, max_team_size)
    self.decks = { 'main': None, }
    # this would be better if this was a list of Rule() objects or a Rules() object
    self.card_game_rules = self.set_card_game_rules( card_game_rules )
    self.pot = []
    self.set_decks()

  def set_card_game_rules(self, rules):
    if 'deck_rules' in rules:
      return rules
    else:
      rules['deck_rules']={}
      return rules

  def set_decks(self):
    """
      This methods job is to set the deck objects for the card_game's decks 
        attribute using the card games deck rules
    """
    # i have to check this because the rules require data structure.
    if 'main' in self.card_game_rules["deck_rules"]:
      for key in self.card_game_rules["deck_rules"]:
        self.decks[key] = self.build_deck(self.card_game_rules["deck_rules"][key])
    else:
      # print("No main deck in provided rules.  ... NEED TO FIX ...")
      pass
    
  def build_deck(self,deck_rules):
    a_deck = Deck(
      unique_cards=True,
      deck_rules=deck_rules )
    return a_deck

