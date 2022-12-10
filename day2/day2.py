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


class GametypeA:
    """
    Contains methods for running RPS rounds according to the
    description of PART 1 of this challenge.

    Methods
    -------
    get_weapon(char)
        Return weapon associated with provided character.
    get_outcome(user_wep, opponent_wep)
        Determine outcome of an RPS round given contenders' weapons.
    get_round_score(user_wep, opponent_wep)
        Return RPS round score given contenders' weapons.
    get_total_score(round_scores)
        Return total score given list of all individual round scores.
    """
    
    def get_weapon(self, char):
        """
        Return weapon associated with provided character.
        
        Args
        ----
        char: single-character string representing a weapon
        
        Returns
        -------
        corresponding weapon as string
        
        Raises
        ------
        KeyError: provided char has no corresponding weapon
        """
        weapon_dict = {
            "A":"rock", "B":"paper", "C":"scissors", 
            "X":"rock", "Y":"paper", "Z":"scissors"
        }
        return weapon_dict[char]

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


# PART 1 Solution
# Iterate through all lines in input file and compile round scores
game1 = GametypeA()
round_scores = []
with open("./day2/day2_input.txt") as rounds:
    round = rounds.readline().strip()
    while round != "":
        my_wep = game1.get_weapon(round[-1])
        elf_wep = game1.get_weapon(round[0])
        round_scores.append(game1.get_round_score(my_wep, elf_wep))
        round = rounds.readline().strip()

# PART 1 Output
print(f"{game1.get_total_score(round_scores)} is my total score")
