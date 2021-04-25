import time
import sys

loader_width = 79

# setup toolbar
sys.stdout.write('%s' % (' ' * loader_width))
sys.stdout.flush()
sys.stdout.write('\b' * (loader_width)) # return to start of line, after '['

for i in range(loader_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write('\u25AE')
    sys.stdout.flush()

sys.stdout.write('\n') # this ends the progress bar