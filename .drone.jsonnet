local base_step(py_ver) = {
  image: 'python:%s' % py_ver,
  volumes: [
    {
      name: 'pip-cache',
      path: '/root/.cache/pip',
    },
    {
      name: 'pipenv-cache',
      path: '/root/.local/share/virtualenvs',
    },
  ],
};

local test_in_py(py_ver) = {
  kind: 'pipeline',
  name: 'python%s' % py_ver,

  steps: [
    base_step(py_ver) + {
      name: 'test',
      commands: [
        'python3 -m pip install --upgrade pip',
        'python3 -m pip install --upgrade pipx',
        'python3 -m pipx ensurepath',
        'python3 -m pipx run pipenv --python %s' % py_ver,
        'python3 -m pipx run pipenv install --dev --skip-lock',
        // It seems that `pipenv lock` does not understand markers.  We have to
        // `--skip-lock`.
        'python3 -m pipx run pipenv run lint',
        'python3 -m pipx run pipenv run test',
      ],
    },
    base_step(py_ver) + {
      name: 'codecov',
      commands: [
        'python3 -m pip install --upgrade pip',
        'python3 -m pip install --upgrade pipx',
        'python3 -m pipx ensurepath',
        'python3 -m pipx run pipenv run codecov',
      ],
      failure: 'ignore',
      // https://discourse.drone.io/t/how-to-allow-failure-of-an-individual-step/3499
      // https://github.com/drone/drone/issues/1920#issuecomment-436837486
      environment: {
        CODECOV_TOKEN: {
          from_secret: 'codecov-upload-token',
        },
      },
    },
  ],

  volumes: [
    {
      name: 'pip-cache',
      temp: {},
    },
    {
      name: 'pipenv-cache',
      temp: {},
    },
  ],
};

[
  {
    kind: 'pipeline',
    name: 'Mega-Linter',
    workspace: {
      path: '/drone/src',
    },
    steps: [
      {
        name: 'Lint',
        image: 'megalinter/megalinter-python:v5',
      },
    ],
    environment: {
      DEFAULT_WORKSPACE: '/drone/src',
    },
  },
] + std.map(test_in_py, ['3.7', '3.8', '3.9', '3.10']) + [
  {
    kind: 'pipeline',
    name: 'Package',

    steps: [
      {
        name: 'Package',
        image: 'python:3',
        commands: [
          'python3 -m pip install --upgrade pip',
          'python3 -m pip install --upgrade pipx',
          'python3 -m pipx ensurepath',
          'python3 -m pipx run pipenv --three',
          'python3 -m pipx run pipenv install --dev --skip-lock',
          // It seems that `pipenv lock` does not understand markers.  We have
          // to `--skip-lock`.
          'python3 -m pipx run pipenv run clean',
          'python3 -m pipx run pipenv run package',
          'python3 -m pipx run pipenv run check-package',
        ],
        volumes: [
          {
            name: 'pip-cache',
            path: '/root/.cache/pip',
          },
          {
            name: 'pipenv-cache',
            path: '/root/.local/share/virtualenvs',
          },
        ],
      },
    ],

    volumes: [
      {
        name: 'pip-cache',
        temp: {},
      },
      {
        name: 'pipenv-cache',
        temp: {},
      },
    ],

    depends_on: [
      'Mega-Linter',
    ] + ['python3.%s' % v for v in std.range(7, 10)],
  },

  {
    kind: 'secret',
    name: 'codecov-upload-token',
    data: '9ooebQakEh6XD6G3L3yvCTKKQ9pxdI8cpPMfGweOOmThfG1EEygi8uZSaAmxTGKxRgrT8qgqkSFyv7edrRAkIw==',
  },
]
