test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're not making an array.  You shouldn't need to
          >>> # use .item anywhere in your solution.
          >>> import numpy as np
          >>> assert np.bool(type(total_charges) == np.ndarray)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You made an array, but it doesn't have the right numbers in it.
          >>> import numpy as np
          >>> assert np.bool(sum(abs(total_charges - np.array([24.144, 47.88, 37.212]))) < 1e-6)
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
