"""Contains helpers to elevate the user rights under Windows"""

from __future__ import unicode_literals
from __future__ import absolute_import
from builtins import str as text
import sys
import ctypes

__version__ = '0.0.0'

def elevate():
    """Tries to rerun the current script with admin rights"""

    if not is_admin():
        params = []

        for arg in sys.argv:
            if '"' in arg:
                arg = '"' + arg.replace('"', r'\"') + '"'
            elif ' ' in arg:
                arg = '"' + arg + '"'

            params.append(arg)

        res = ctypes.windll.shell32.ShellExecuteW(None, "runas".encode('utf_16'), text(sys.executable).encode('utf_16'), text(' '.join(params)).encode('utf_16'), None, 1)

        if res <= 32:
            raise WindowsError("ShellExecute returned error code %d" % res)

        return False

    return True

def is_admin():
    """Checks if the script is run with full admin rights"""

    return ctypes.windll.shell32.IsUserAnAdmin() == 1
