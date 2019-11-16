test = {
  'name': 'Question42',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> my_dice = []
          >>> my_test = np.arange(7,9)
          >>> reroll(my_test)
          >>> reroll(my_test)
          >>> len(my_test) == 2 and min(my_test) >= 1 and max(my_test) <= 6 
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
