import argparse

import my_project.module


def main():
    # Basic example of how to get an arg parser up and running, after installing this package with `pip install .`
    # or `python setup.py install` run `my_cmd 2` to test this
    parser = argparse.ArgumentParser(description='Add two to an integer')
    parser.add_argument('int', metavar='N', type=int, nargs=1, help='Add two to this integer (default = 2)', default=2)

    args = parser.parse_args()

    # This shows how to import your own library functions in this project if the project has been installed
    # with `pip install .`
    print("Your number {0}, plus 2 is {1}".format(args.int[0], my_project.module.add_two(args.int[0])))


if __name__ == '__main__':
    main()
