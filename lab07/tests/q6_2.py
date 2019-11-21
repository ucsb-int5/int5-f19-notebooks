test = {   'name': 'q6_2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> true_predictions != []\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Try looking at the other '
                                               'statements, see if that can '
                                               'help you figure out;\n'
                                               '>>> # why this prediction '
                                               "isn't reliable.;\n"
                                               '>>> 1 in true_predictions\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Try looking at the other '
                                               'statements, see if that can '
                                               'help you figure out;\n'
                                               '>>> # why this prediction '
                                               "isn't reliable.;\n"
                                               '>>> 3 in true_predictions\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Are you sure? Try '
                                               'checking if the table has rows '
                                               'for duration 0, 2.5, and 60.;\n'
                                               '>>> 4 in true_predictions\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Are you sure? Do we have '
                                               'data for durations less than '
                                               '0? Greater than 60?;\n'
                                               '>>> 5 in true_predictions\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> set(true_predictions) == '
                                               '{2}\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
