test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(six_pokemons) == Table
          True
          >>> six_pokemons.num_rows
          6
          >>> six_pokemons.take([0, 1, 2, 4, 5])
          Index | Name
          7     | squirtle
          39    | jigglypuff
          60    | poliwag
          94    | gengar
          130   | gyarados
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
