from app.utilities import clear_screen
import sys

class Game( object ):
  """a bit high level but i'm woriking on inheratance"""
  def __init__( self,
                name,
                description,
                players,
                total_players=2,
                max_team_size=1 ):
    
    self.name = name
    self.description = description
    self.players = self.set_players( players )
    self.players_out = []
    self.total_players = total_players
    self.max_team_size = max_team_size
    self.total_teams = None
    self.set_total_teams()

    # self.rules = { Rule(), Rule(), ... }

  def exit_game(self):
    """User selected to quit game"""
    sys.exit(1)

  def get_player_by_name( self, name ):
    """
      Returns a player object from the players list
      @name as a string
      returns Player object
    """
    for player in self.players:
      if name == player.name:
        return player

  def player_is_out( self, player ):
    """
      player is moved from Game.players to Game.players_out
        the state of players in a game, a hand, etc
    """
    self.players_out.append( self.players.pop( self.players.index( player ) ) )

  def set_players(self, players):
    """
      setter for the Game.players attribute
      @players as a list of Player objects
      returns list of people objects
    """
    assert type( players ) is list
    return players

  def set_total_teams(self):
    """Calculates the total teams and sets the class attribute total_teams """
    self.total_teams = int(self.total_players/self.max_team_size) + (self.total_players % self.max_team_size > 0)
