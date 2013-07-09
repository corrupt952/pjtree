# -*- utf-8 -*-


def main():
    u""" Main method

    main method.
    """
    import sys
    import jread

    argc = len(sys.argv)
    if argc < 2:
        print('Usage: jread path')
        sys.exit(1)
    data = jread.scan({}, sys.argv[1])
    jread.show(data)


if __name__ == '__main__':
    main()
