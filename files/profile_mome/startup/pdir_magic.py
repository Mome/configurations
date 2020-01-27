from IPython.core.magic import register_line_magic

import pdir as _pdir


@register_line_magic
def pdir(line):
    #line = ' '.join(*line)
    if line:
        obj = eval(line)
        return _pdir(obj).public

@register_line_magic
def apdir(line):
    #line = ' '.join(*line)
    if line:
        obj = eval(line)
        return _pdir(obj)


# We delete these to avoid name conflicts for automagic to work
del pdir, apdir

