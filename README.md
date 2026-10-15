# strtoolz

Extra string search and manipulation functions for `str`, `bytes` & `bytearray`
objects in Python.

- `find_all()`
- `find_iter()`
- `find_nth()`
- `index_nth()`
- `replace_counted()`
- `replace_exactly()`
- `replace_nth()`


## Usage

### Finding

```python
>>> import strtoolz
>>> strtoolz.find_all("The rain in Spain falls mainly on the plain", 'ain')
[5, 14, 25, 40]
>>> strtoolz.find_nth("The rain in Spain falls mainly on the plain", 'ain', n=2)
25
```

### Replacing

```python
>>> strtoolz.replace_counted('The rain in Spain falls mainly on the plain', 'ain', 'AIN')
('The rAIN in SpAIN falls mAINly on the plAIN', 4)
>>> strtoolz.replace_exactly('The rain in Spain falls mainly on the plain', 'ain', 'AIN', 10)
Traceback (most recent call last):
...
ValueError: Only 4 occurences could be replaced, required 10
>>> strtoolz.replace_nth('The rain in Spain falls mainly on the plain', 'ain', 'AIN', n=3)
'The rain in Spain falls mainly on the plAIN'
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


## See also

### stdlib

`re` was inspiration for some of the functions in `strtoolz`, including
`strtoolz.find_all()`/`strtoolz.find_iter()`.

To find static strings with `re` your must escape any metachars

```py
>>> pattern = re.compile(re.escape('an.'))
>>> [m.start() for m in pattern.finditer('A man. A plan. A canal. Panama!')]
[3, 11]
```

Combine `re` with `itertools` to recreate `strtoolz.find_nth()`

```py
>>> pattern = re.compile(re.escape('an.'))
>>> matches = pattern.finditer('A man. A plan. A canal. Panama!')
>>> next(itertools.islice(matches, 1, None), -1).start()
11
```
