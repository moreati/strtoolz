# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import nox

PYPROJECT = nox.project.load_toml('pyproject.toml')

# Also check/update .github/workflows, pyproject.toml
PYTHONS = [
    *nox.project.python_versions(PYPROJECT),
    'pypy3.11',  # TODO Upgrade to pypy3.12 once Hypothesis wheels available
]

nox.options.default_venv_backend = 'uv|virtualenv'

@nox.session(python=PYTHONS, tags=['test'])
def tests(session: nox.Session) -> None:
    session.install('.[test]', 'nox')
    session.run('pytest')
