# -*- coding: utf-8 -*-
#!/usr/bin/env python

from nude import Nude


def run(argv):
    for index in range(1, len(argv)):
        filename = str(argv[index])
        n = Nude(filename)
        n.parse()
        print(filename, n.result, n.inspect())
    return 0


if __name__ == "__main__":
    import sys
    run(sys.argv)
