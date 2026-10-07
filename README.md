# strtoolz

Extra string search and manipulation functions for Python.

- `find_all()`
- `find_iter()`
- `find_nth()`
- `index_nth()`


## Usage

```python
>>> import strtoolz
>>> strtoolz.find_all("The rain in Spain falls mainly on the plain", 'ain')
[5, 14, 25, 40]
>>> strtoolz.find_nth("The rain in Spain falls mainly on the plain", 'ain', n=2)
25
```


## Installtion

```sh
uv pip install strtoolz
```

or

```sh
pip install strtoolz
```


## Licence

MIT
