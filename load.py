"""
loading on screen animation
"""


import sys
import time



def loading(delay, sleep, loadmsg):
    """
    animates loading
    """
    t_end = time.time() + sleep
    while time.time() < t_end:
        sys.stdout.write(f'\r{loadmsg} |')
        time.sleep(delay)
        sys.stdout.write(f'\r{loadmsg} /')
        time.sleep(delay)
        sys.stdout.write(f'\r{loadmsg} -')
        time.sleep(delay)
        sys.stdout.write(f'\r{loadmsg} \\')
        time.sleep(delay)
