test = {   'name': 'q5_2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'faithful_predictions.labels == '
                                               "('duration', 'wait', "
                                               "'predicted wait')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> abs(1 - '
                                               'np.mean(faithful_predictions.column(2))/100) '
                                               '<= 0.35\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
