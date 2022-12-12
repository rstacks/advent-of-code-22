# CHALLENGE INTRO:
# Each line of the file day2_input.txt represents a round of rock,
# paper, scissors. We need to calculate our total score after all
# rounds are played. The total score is the sum of all points earned
# in each individual round. Round scores are based on the weapon
# we chose according to the input file and the outcome of the round
# for us (win, draw, or loss):
#       Chose rock: +1 points
#       Chose paper: +2 points
#       Chose scissors: +3 points
#       Win: +6 points
#       Draw: +3 points
#       Loss: +0 points
#
# PART 1:
# The first letter in a given line from the input file represents
# the opponent's weapon of choice:
#       A: rock
#       B: paper
#       C: scissors
# The second letter in the line represents our weapon of choice:
#       X: rock
#       Y: paper
#       Z: scissors
# Determine the total score using this information.
#
# PART 2:
# The first letter still represents the opponent's weapon, but the
# second letter now represents the outcome of the round for us:
#       X: loss
#       Y: draw
#       Z: win
# Points are assigned in the same way as PART 1. Determine the total
# score using this information.


class GametypeA:
    """
    Contains methods for running RPS rounds according to the
    description of PART 1 of this challenge.

    Methods
    -------
    get_weapons(user_char, opponent_char)
        Returns tuple of weapons from chars as (user_wep, opponent_wep).
    get_outcome(user_wep, opponent_wep)
        Determine outcome of an RPS round given contenders' weapons.
    get_round_score(user_wep, opponent_wep)
        Return RPS round score given contenders' weapons.
    get_total_score(round_scores)
        Return total score given list of all individual round scores.
    """
    
    def get_weapons(self, user_char, opponent_char):
        """
        Returns tuple of weapons from chars as (user_wep, opponent_wep).
        
        Args
        ----
        user_char: single-character string for the player's weapon
        opponent_char: single-character string for opponent's weapon
        
        Returns
        -------
        corresponding weapons as strings
        
        Raises
        ------
        KeyError: provided char(s) has no corresponding weapon
        """
        weapon_dict = {
            "A":"rock", "B":"paper", "C":"scissors", 
            "X":"rock", "Y":"paper", "Z":"scissors"
        }
        return (weapon_dict[user_char], weapon_dict[opponent_char])

    def get_outcome(self, user_wep, opponent_wep):
        """
        Determine outcome of an RPS round given contenders' weapons.

        Args
        ----
        user_wep: string with player's chosen weapon
        opponent_wep: string with opponent's chosen weapon
        
        Returns
        -------
        "win", "draw", or "loss" depending on outcome for player
        
        Raises
        ------
        KeyError: provided user_wep param is not an available weapon
        """
        win_combo_dict = {
            "rock":"scissors", "paper":"rock", "scissors":"paper"
        }
        if win_combo_dict[user_wep] == opponent_wep:
            return "win"
        if user_wep == opponent_wep:
            return "draw"
        return "loss"

    def get_round_score(self, user_wep, opponent_wep):
        """
        Return RPS round score given contenders' weapons.

        Args
        ----
        user_wep: string with player's chosen weapon
        opponent_wep: string with opponent's chosen weapon
        
        Returns
        -------
        int score for player based on their chosen weapon and
        outcome of round for them
        
        Raises
        ------
        KeyError: provided user_wep param is not an available weapon
        """
        score_dict = {
            "rock":1, "paper":2, "scissors":3,
            "loss":0, "draw":3, "win":6
        }
        outcome = self.get_outcome(user_wep, opponent_wep)
        return score_dict[user_wep] + score_dict[outcome]

    def get_total_score(self, round_scores):
        """
        Return total score given list of all individual round scores.
        
        Args
        ----
        round_scores: iterable containing numeric values
        representing RPS round scores
        
        Returns
        -------
        numeric sum of all values in round_scores iterable
        
        Raises
        ------
        TypeError: provided param contains non-numeric data
        """
        return sum(round_scores)


class GametypeB(GametypeA):
    """
    Extends GametypeA. Overrides get_weapons(user_char, opponent_char)
    method to reflect the new description of RPS rounds in PART 2 of
    this challenge.

    Methods
    -------
    get_weapons(user_char, opponent_char)
        Returns tuple of weapons from chars as (user_wep, opponent_wep).
    """

    def get_weapons(self, user_char, opponent_char):
        """
        Returns tuple of weapons from chars as (user_wep, opponent_wep).
        
        Args
        ----
        user_char: single-character string for round outcome
        opponent_char: single-character string for opponent's weapon
        
        Returns
        -------
        corresponding weapons as strings
        
        Raises
        ------
        KeyError: provided char(s) has no matching weapon or outcome
        """
        # Determine correct round outcome given user_char
        outcome_dict = {"X":"loss", "Y":"draw", "Z":"win"}
        correct_outcome = outcome_dict[user_char]
        # Assign opponent weapon using superclass method
        opponent_wep = super().get_weapons(user_char, opponent_char)[1]
        # Select user_wep that yields the correct round outcome
        wep_list = ["rock", "paper", "scissors"]
        user_wep = wep_list[0]
        trial_outcome = self.get_outcome(user_wep, opponent_wep)
        while trial_outcome != correct_outcome:
            wep_list = wep_list[1:]
            user_wep = wep_list[0]
            trial_outcome = self.get_outcome(user_wep, opponent_wep)
        return (user_wep, opponent_wep)


def play_game(game):
    """
    Prints total score after running all rounds for provided gametype.

    Args
    ----
    game: GametypeA or GametypeB object to calculate score for
    
    Returns
    -------
    None
    
    Raises
    ------
    AttributeError: param is not an object of GametypeA
    """
    round_scores = []
    with open("./day2/day2_input.txt") as rounds:
        round = rounds.readline().strip()
        while round != "":
            my_wep, elf_wep = game.get_weapons(round[-1], round[0])
            round_scores.append(game.get_round_score(my_wep, elf_wep))
            round = rounds.readline().strip()
    print(f"{game.get_total_score(round_scores)} is my total score")


# PART 1 Solution
# Iterate through all lines in input file and compile round scores
game1 = GametypeA()
print("Part 1:", end=" ")
play_game(game1)

# PART 2 Solution
game2 = GametypeB()
print("Part 2:", end=" ")
play_game(game2)
