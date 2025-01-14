test = {
  'name': 'Question 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '1b26ada5a58db30444f6f64d80a11c53',
          'choices': [
            r"""
            A commentary function that prints information about the
            biggest point increase for the current player.
            """,
            r"""
            A string containing the largest point increase for the
            current player.
            """,
            r"""
            The current largest point increase between both
            players.
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does announce_highest return?'
        },
        {
          'answer': '7d886fd7ff35daff80023a8393a95a32',
          'choices': [
            r"""
            When the current player, given by the parameter `who`,
            earns their biggest point increase yet in the game.
            """,
            'After each turn.',
            r"""
            When the current player, given by the parameter `who`,
            earns the biggest point increase yet between both
            players in the game.
            """
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          When does the commentary function returned by announce_highest
          print something out?
          """
        },
        {
          'answer': '5751efd31d23f9934e774e6a8315975e',
          'choices': [
            'The previous highest gain for the current player.',
            "The current player's score before this turn.",
            "The opponent's score before this turn."
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the parameter previous_score represent?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> f0 = announce_highest(1) # Only announce Player 1 score gains
          >>> f1 = f0(11, 0)
          >>> f2 = f1(11, 9)
          9 point(s)! That's the biggest gain yet for Player 1
          >>> f3 = f2(20, 9)
          >>> f4 = f3(12, 20) # Player 1 gets 3 points, then Swine Swap applies
          11 point(s)! That's the biggest gain yet for Player 1
          >>> f5 = f4(20, 32) # Player 0 gets 20 points, then Swine Swap applies
          12 point(s)! That's the biggest gain yet for Player 1
          >>> f6 = f5(20, 43) # Player 1 gets 11 points; not enough for a new high
          >>> f7 = f6(21, 43)
          >>> f8 = f7(21, 75)
          32 point(s)! That's the biggest gain yet for Player 1
          >>> f9 = f8(75, 27) # Swap!
          >>> f10 = f9(37, 75) # Swap!
          48 point(s)! That's the biggest gain yet for Player 1
          >>> # The following function call checks if the behavior of f1 changes,
          >>> # perhaps due to a side effect other than printing. The only side
          >>> # effect of a commentary function should be to print.
          >>> f2_again = f1(11, 9)
          9 point(s)! That's the biggest gain yet for Player 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> announce_both = both(announce_highest(0), announce_highest(1))
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5, 3, 5), goal=10, say=announce_both)
          5 point(s)! That's the biggest gain yet for Player 0
          3 point(s)! That's the biggest gain yet for Player 1
          7 point(s)! That's the biggest gain yet for Player 1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, announce_highest, both
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
