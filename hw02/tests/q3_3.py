test = {   'name': 'q3_3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> probability_of_faulty != '
                                               "0.03 # What's your failure "
                                               'rate?\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> probability_of_not_faulty '
                                               '== 1 - probability_of_faulty\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'probability_of_one_not_faulty '
                                               '== probability_of_not_faulty * '
                                               '(probability_of_faulty*4) # '
                                               'how do you compute the '
                                               'probability of four events in '
                                               'a row?\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(probability_of_one_not_faulty, '
                                               '6) == 1e-06\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
