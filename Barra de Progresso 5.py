import sys
import time


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" %
                   (prefix, "#" * x, "." * (size - x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()


users = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


for user in progressbar(users, "Processing: "):
    time.sleep(0.01)
    # Do something.


for i in progressbar(range(42), "Processing: "):
    time.sleep(0.01)
    # Do something.