test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(new_pokemon) == list
          True
          >>> type(new_pokemon[0]) == int
          True
          >>> type(new_pokemon[1]) == str and new_pokemon[1] != ''
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
