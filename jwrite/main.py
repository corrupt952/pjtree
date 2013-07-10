# -*- utf-8 -*-


def main():
    u""" Main method

    main method.
    """
    import sys
    import jwrite

    argc = len(sys.argv)
    if(argc < 4):
        print('Usage: jwrite json encode path')
        sys.exit(1)
    data = jwrite.load_json(sys.argv[1], sys.argv[2])
    jwrite.trace(data, sys.argv[3])


if __name__ == '__main__':
    main()
