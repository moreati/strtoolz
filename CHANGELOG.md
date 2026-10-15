# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added

- `replace_counted()` function
- `replace_exactly()` function

### Fixed

- `tests.test_find_all.find_all_re()` test oracle when `start > 0`
- `replace_exactly()` export in `__all__`
- Spelling mistakes (e.g. occurrence)


## 0.0.2 - 2026-10-07

### Added

- `find_nth()` function
- `index_nth()` function
- [Nox](https://nox.thea.codes) test automation

### Changed

- `find_all()` and `find_iter()`: string arguments are now positional only

### Fixed

- Include changelog and tests in sdist


## 0.0.1 - 2026-09-25

### Added

- `find_all()` function
- `find_iter()` generator function
