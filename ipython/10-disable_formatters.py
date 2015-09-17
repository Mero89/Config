# coding=utf-8
import IPython
import os

_types_to_remove = ['image/png']
_here = os.path.abspath(__file__)
_msg = " >>>> *{typ} removed from this session"
_final = "Change the startup scripts at {here}"

_ip = IPython.get_ipython()
_formatters = _ip.display_formatter.formatters
for typ in _types_to_remove:
    _formatters.pop(typ)
    print(_msg.format(typ=typ))
# else:
#     print(_final.format(here=_here))
