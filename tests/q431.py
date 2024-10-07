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
          >>> np.bool(type(population_magnitudes) == np.ndarray)
          np.True_
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You made an array, but it doesn't have the right numbers in it.
          >>> import numpy as np
          >>> np.bool(sum(abs(population_magnitudes - np.log10(population))) < 1e-6)
          np.True_
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
