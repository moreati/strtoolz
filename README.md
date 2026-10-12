# strtoolz

Extra string search and manipulation functions for `str`, `bytes` & `bytearray`
objects in Python.

- `find_all()`
- `find_iter()`
- `find_nth()`
- `index_nth()`
- `replace_counted()`


## Usage

```python
>>> import strtoolz
>>> strtoolz.find_all("The rain in Spain falls mainly on the plain", 'ain')
[5, 14, 25, 40]
>>> strtoolz.find_nth("The rain in Spain falls mainly on the plain", 'ain', n=2)
25
>>> strtoolz.replace_counted('The rain in Spain falls mainly on the plain', 'ain', 'AIN')
('The rAIN in SpAIN falls mAINly on the plAIN', 4)
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
