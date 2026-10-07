# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import nox

PYPROJECT = nox.project.load_toml('pyproject.toml')
PYTHONS = [
    *nox.project.python_versions(PYPROJECT),
    'pypy3',
]

nox.options.default_venv_backend = 'uv|virtualenv'

@nox.session(python=PYTHONS, tags=['test'])
def tests(session: nox.Session) -> None:
    session.install('.[test]', 'nox')
    session.run('pytest')
