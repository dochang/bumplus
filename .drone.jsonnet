local base_step(py_ver) = {
  image: 'python:%s' % py_ver,
  volumes: [
    {
      name: 'pip-cache',
      path: '/root/.cache/pip',
    },
  ],
  environment: {
    PIPENV_VENV_IN_PROJECT: 1,
  },
};

local test_in_py(py_ver) = {
  kind: 'pipeline',
  name: 'python%s' % py_ver,

  steps: [
    base_step(py_ver) + {
      name: 'test',
      commands: [
        'pip install --upgrade pipenv',
        'pipenv --python %s' % py_ver,
        'pipenv install --dev --skip-lock',
        // It seems that `pipenv lock` does not understand markers.  We have to
        // `--skip-lock`.
        'pipenv run flake8',
        'pipenv run pytest',
      ],
    },
    base_step(py_ver) + {
      name: 'codecov',
      commands: [
        'pip install --upgrade pipenv',
        'pipenv run codecov',
      ],
      failure: 'ignore',
      // https://discourse.drone.io/t/how-to-allow-failure-of-an-individual-step/3499
      // https://github.com/drone/drone/issues/1920#issuecomment-436837486
      environment: {
        PIPENV_VENV_IN_PROJECT: 1,
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
  ],
};

std.map(test_in_py, ['2.7', '3.5', '3.6', '3.7', '3.8', '3.9']) + [
  {
    kind: 'secret',
    name: 'codecov-upload-token',
    data: '9ooebQakEh6XD6G3L3yvCTKKQ9pxdI8cpPMfGweOOmThfG1EEygi8uZSaAmxTGKxRgrT8qgqkSFyv7edrRAkIw==',
  },
]
