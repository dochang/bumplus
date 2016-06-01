import pytest

from textwrap import dedent

import bumplus

class TestCLI:

    def test_not_bumplus_dir(self, tmpdir):
        tmpdir.chdir()
        with pytest.raises(bumplus.NotBumplusDir):
            bumplus.main(['1.2.4'])

    def test_version_not_defined(self, tmpdir):
        tmpdir.chdir()
        tmpdir.join('.bumplus.toml').ensure()
        with pytest.raises(bumplus.VersionNotDefined):
            bumplus.main(['1.2.4'])

    def test_bump_version(self, tmpdir):
        tmpdir.chdir()
        tmpdir.join('.bumplus.toml').write(dedent('''
        version = '1.2.3'
        [[files.foo]]
        search = '{{old_version}}'
        replace = '{{new_version}}'
        '''))
        tmpdir.join('foo').write('1.2.3')
        bumplus.main(['1.2.4'])
        assert tmpdir.join('foo').read() == '1.2.4'
        assert tmpdir.join('.bumplus.toml').read() == dedent('''
        version = '1.2.4'
        [[files.foo]]
        search = '{{old_version}}'
        replace = '{{new_version}}'
        ''')

    def test_bump_version_multi_line(self, tmpdir):

        tmpdir.chdir()
        tmpdir.join('.bumplus.toml').write(dedent("""
        version = '1.2.3'
        [[files.foo]]
        search = '{{old_version}}'
        replace = '''{{new_version}}
        {{old_version}}'''
        """))
        tmpdir.join('foo').write(dedent('''
        1.2.3
        '''))

        bumplus.main(['1.2.4'])

        assert tmpdir.join('foo').read() == dedent('''
        1.2.4
        1.2.3
        ''')

    def test_bump_version_multi_pattern(self, tmpdir):

        tmpdir.chdir()
        tmpdir.join('.bumplus.toml').write(dedent("""
        version = '1.2.3'

        [[files.foo]]
        search = '''
        Unreleased
        ----------
        '''
        replace = '''
        Unreleased
        ----------

        {{new_version}}
        {{'-' * (new_version | length)}}
        '''

        [[files.foo]]
        search = '''
        [Unreleased]: <change log url HEAD>
        '''
        replace = '''
        [Unreleased]: <change log url HEAD>
        [{{new_version}}]: <change log url {{new_version}}>
        '''
        """))
        tmpdir.join('foo').write(dedent('''
        CHANGELOG
        =========

        Unreleased
        ----------

          - fix #3
          - fix #4

        1.2.3
        -----

          - fix #1
          - fix #2

        [Unreleased]: <change log url HEAD>
        [1.2.3]: <change log url 1.2.3>
        '''))

        bumplus.main(['1.2.4'])

        assert tmpdir.join('foo').read() == dedent('''
        CHANGELOG
        =========

        Unreleased
        ----------

        1.2.4
        -----

          - fix #3
          - fix #4

        1.2.3
        -----

          - fix #1
          - fix #2

        [Unreleased]: <change log url HEAD>
        [1.2.4]: <change log url 1.2.4>
        [1.2.3]: <change log url 1.2.3>
        ''')

    def test_bump_version_multi_file(self, tmpdir):

        tmpdir.chdir()
        tmpdir.join('.bumplus.toml').write(dedent('''
        version = '1.2.3'
        [[files.foo]]
        search = '{{old_version}}'
        replace = '{{new_version}}'
        [[files.bar]]
        search = '{{old_version}}'
        replace = '{{new_version}}'
        '''))
        tmpdir.join('foo').write(dedent('1.2.3'))
        tmpdir.join('bar').write(dedent('1.2.3'))

        bumplus.main(['1.2.4'])

        assert tmpdir.join('foo').read() == '1.2.4'
        assert tmpdir.join('bar').read() == '1.2.4'
