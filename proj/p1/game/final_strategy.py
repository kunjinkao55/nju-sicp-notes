"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = 'WDA'  # Change this line!

import random
def final_strategy(score, opponent_score):
    return max(score//opponent_score,opponent_score//score)