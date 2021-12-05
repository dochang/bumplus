# Change Log

## [Unreleased]

## [0.6.1] - 2021-12-05

### Changed

- Ensure that python3 is invoked

## [0.6.0] - 2021-12-05

### Added

- Python 3.10 support

### Changed

- Migrate MegaLinter to v5

## [0.5.1] - 2021-09-16

### Changed

- Run CI jobs/pipelines in parallel

## [0.5.0] - 2021-09-12

### Added

- Python 3.8 & 3.9 support for Tox

### Changed

- Install & run pipenv by pipx
- GitHub Actions workflow does not fail when the codecov step fails

### Removed

- Python 2.7 & 3.5 support

## [0.4.0] - 2021-09-12

### Added

- Lint project by Mega-Linter

## [0.3.2] - 2021-09-03

### Fixed

- Restore keys of Github Actions cache

## [0.3.1] - 2021-08-24

### Added

- Python 3.8 & 3.9 support in documentation and pypi classifiers

## [0.3.0] - 2021-08-24

### Added

- Test for Python 3.8 & 3.9
- Github Actions CI
- Github Actions badge

### Changed

- Pseudonym of the author

### Fixed

- Specify python version for pipenv
- Fix flake8-isort errors I003 & I001

### Removed

- Remove deprecated setuptools entrypoints
- Travis badge

## [0.2.0] - 2019-04-03

### Added

- Test with black
- Test with isort
- Test with bugbear

### Changed

- Migrate from Travis to Drone

### Removed

- Python 3.4 support

## [0.1.6] - 2018-11-28

### Fixed

- Add Python 3.7 support in README

## [0.1.5] - 2018-11-28

### Added

- Add Python 3.7 support

## [0.1.4] - 2018-11-28

### Changed

- Fix style error

## [0.1.3] - 2018-03-12

### Changed

- Cache pip files when testing on Travis CI

## [0.1.2] - 2018-02-27

### Added

- Add badges

## [0.1.1] - 2018-02-27

### Changed

- Build universal wheel

## [0.1.0] - 2018-02-27

### Added

- PyPI classifiers
- Use flake8 to check source code

### Changed

- Migrate from tox to pipenv
- Use tox for local testing only
- Integrate pytest and setup.py
- Replace `release.sh` with `python setup.py upload`

### Removed

- Python 2.6 support
- Python 3.3 support

## [0.0.9] - 2017-10-02

### Added

- Add compatibility code
- Python 3.6 support for Travis CI

## [0.0.8] - 2017-02-08

### Added

- Add saythanks.io badge

## [0.0.7] - 2016-12-07

### Added

- Python 3.5 support for Travis CI

## [0.0.6] - 2016-07-24

### Added

- Add code of conduct

## [0.0.5] - 2016-07-12

### Fixed

- Provide url meta-data for the setup script

## [0.0.4] - 2016-07-02

### Added

- Generate code coverage report
- Upload code coverage report to codecov.io

## [0.0.3] - 2016-06-01

### Added

- Add PyPI badge
- Add requires.io badge

## [0.0.2] - 2016-06-01

### Fixed

- Fix change log
- Fix README.rst for PyPI

## [0.0.1] - 2016-06-01

### Added

- Initial release

<!-- markdown-link-check-disable -->

<!-- Skip checking the links status because the CHANGELOG is always updated
before the tag is created -->

[Unreleased]: https://github.com/dochang/bumplus/compare/0.6.1...HEAD
[0.6.1]: https://github.com/dochang/bumplus/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/dochang/bumplus/compare/0.5.1...0.6.0
[0.5.1]: https://github.com/dochang/bumplus/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/dochang/bumplus/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/dochang/bumplus/compare/0.3.2...0.4.0
[0.3.2]: https://github.com/dochang/bumplus/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/dochang/bumplus/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/dochang/bumplus/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/dochang/bumplus/compare/0.1.6...0.2.0
[0.1.6]: https://github.com/dochang/bumplus/compare/0.1.5...0.1.6
[0.1.5]: https://github.com/dochang/bumplus/compare/0.1.4...0.1.5
[0.1.4]: https://github.com/dochang/bumplus/compare/0.1.3...0.1.4
[0.1.3]: https://github.com/dochang/bumplus/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/dochang/bumplus/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/dochang/bumplus/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/dochang/bumplus/compare/0.0.9...0.1.0
[0.0.9]: https://github.com/dochang/bumplus/compare/0.0.8...0.0.9
[0.0.8]: https://github.com/dochang/bumplus/compare/0.0.7...0.0.8
[0.0.7]: https://github.com/dochang/bumplus/compare/0.0.6...0.0.7
[0.0.6]: https://github.com/dochang/bumplus/compare/0.0.5...0.0.6
[0.0.5]: https://github.com/dochang/bumplus/compare/0.0.4...0.0.5
[0.0.4]: https://github.com/dochang/bumplus/compare/0.0.3...0.0.4
[0.0.3]: https://github.com/dochang/bumplus/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/dochang/bumplus/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/dochang/bumplus/commits/0.0.1

<!-- markdown-link-check-enable -->

<!-- markdownlint-configure-file
{
  "MD024": {
    "siblings_only": true
  }
}
-->
