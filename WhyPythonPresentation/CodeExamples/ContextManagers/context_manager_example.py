#!/usr/bin/env python

# __future__ module helps with Python 2 to 3 conversions

# division uses Python 3's division operator which always does float division
# therefore 5 / 2 = 2.5 instead of 2
# for integer division use //, 5 // 2 = 2
from __future__ import division

# print_function uses Python 3's print function which allows us to control
# what is printed at the end using end:
#          print('hello world', end='!@#') => hello world!@#
from __future__ import print_function


class ControlledExecution(object):  # className(parentClass) always put object for new style class objects
    def __enter__(self):
        # Set things up
        return None

    def __exit__(self, type, value, traceback):
        # Tear things down
        pass  # Since Python is space delimited, when we have an empty block
              # we need to indicate that it wasn't a mistake, use pass when
              # nothing is supposed to be done


with ControlledExecution() as thing:
    # Do stuff
    pass
