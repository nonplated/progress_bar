progress_bar
============
simple and customizable progress bar for python 3 console output


example 1
=========
```python
print_progress_bar(47, 100, length=30, title='In loop')
```
will print:
```console
[██████████████................]  47% In loop
```

example 2
=========
```python
custom_mode = {
    'length': 6,
    'char_begin': '<',
    'char_end': '>',
    'char_full': '#',
    'char_empty': ' ',
    'title': 'my custom mode',
}
print_progress_bar(47, 80, **custom_mode)
```
will print:
```console
<###   >  59% my custom mode
```

example 3
=========
```python
print_progress_bar(12, 20, length=8, char_empty='#', char_full='-')
```
will print:
```console
[----####]  60%
```

example 4
=========

```python
print_progress_bar(1, 10, length=4)
```
will print:
```console
[....]  10%
```

example 5
=========
```python
my_theme = {
    'length': 12,
    'char_begin': '>',
    'char_end': '',
    'char_full': '|',
    'char_empty': '.',
    'title': 'done',
}
print_progress_bar(0, 100, **my_theme)
print()
print_progress_bar(1, 100, **my_theme)
print()
print_progress_bar(99, 100, **my_theme)
print()
print_progress_bar(100, 100, **my_theme)
print()
print_progress_bar(120, 100, **my_theme)
print()
print_progress_bar(999, 100, **my_theme)
print()
```
will print:
```console
>............   0% done
>............   1% done
>|||||||||||.  99% done
>|||||||||||| 100% done
>|||||||||||| 120% done
>|||||||||||| 999% done
```
