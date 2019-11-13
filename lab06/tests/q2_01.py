test = {
  'name': 'Question2.0.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < prob_rolling_six < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(prob_rolling_six, 3) == round(1/6,3)
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

