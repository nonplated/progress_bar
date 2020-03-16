
def get_progress_bar(current, maximum=100, **kwargs) -> str:
    '''
        Return progress bar (as string).
    '''
    length = kwargs.get('length', 20)
    char_full = kwargs.get('char_full', u"\u2588")
    char_empty = kwargs.get('char_empty', '.')
    char_begin = kwargs.get('char_begin', '[')
    char_end = kwargs.get('char_end', ']')
    title = kwargs.get('title', '')

    if maximum == 0:
        return 'Set "maximum" to non zero number.'

    percent = (current * 100) / maximum
    cur_pos = int(percent * length // 100)
    cur_pos = length if cur_pos>length else cur_pos #dont draw more than 100%
    progress_bar = (char_full*cur_pos + char_empty*(length-cur_pos))

    return "{}{}{} {:3d}% {}".format(
        char_begin, progress_bar, char_end, round(percent), title)


def print_progress_bar(current, maximum=100, **kwargs):
    '''
        Display progress bar inline in console.
    '''
    print("\r{}".format(get_progress_bar(current, maximum, **kwargs)), end='')
