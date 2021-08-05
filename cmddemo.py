import argparse

def main():
    parser = argparse.ArgumentParser(prog="cmd test app")
    # positional 参数
    parser.add_argument('pos1', help='positional 1')
    parser.add_argument('pos2', nargs='+', help='positional 2')
    # 有名参数
    parser.add_argument('--arg1', dest='arg1', required=False, help='argument 1')
    parser.add_argument('--arg2', dest='arg2', nargs='*', help='argument 2')
    args = parser.parse_args()
    print('pos2: ', args.pos2)
    print('pos1: ', args.pos1)
    print('arg1: ', args.arg1)
    print('arg2: ', args.arg2)
if __name__ == "__main__":
    main()
