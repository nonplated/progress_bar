from progress_bar import print_progress_bar

##############################################################
print_progress_bar(47, 100, length=30, title='In loop')
print()  # new line after finish

##############################################################
custom_mode = {
    'length': 6,
    'char_begin': '<',
    'char_end': '>',
    'char_full': '#',
    'char_empty': ' ',
    'title': 'my custom mode',
}
print_progress_bar(47, 80, **custom_mode)
print()  # new line after finish

##############################################################
print_progress_bar(12, 20, length=8, char_empty='#', char_full='-')
print()

##############################################################
print_progress_bar(1, 10, length=4)
print()
