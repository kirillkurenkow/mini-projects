from argparse import (
    ArgumentParser,
    ArgumentError,
)

from PascalTriangleGenerator import PascalTriangleGenerator

MAX_DEGREE = 100


class ScriptArgs:
    def __init__(self):
        self.__ArgParser = ArgumentParser()
        self.degree: int = ...
        self.no_color: bool = ...
        self.no_sub: bool = ...
        self.__parse_args()

    def __parse_args(self):
        # Add args
        self.__ArgParser.add_argument('degree', type=self.check_degree)
        self.__ArgParser.add_argument('--no-color', action='store_true')
        self.__ArgParser.add_argument('--no-sub', action='store_true')

        # Parse args
        args = self.__ArgParser.parse_args()
        self.degree = args.degree
        self.no_color = args.no_color
        self.no_sub = args.no_sub

    @staticmethod
    def check_degree(value) -> int:
        try:
            value = int(value)
        except ValueError as error:
            raise ArgumentError(None, f'Degree must be int: {value}') from error
        if value not in range(2, MAX_DEGREE):
            raise ArgumentError(None, f'Degree must be between 2 and {MAX_DEGREE}: {value}')
        return value


def main():
    args = ScriptArgs()
    generator = PascalTriangleGenerator(no_sub=args.no_sub)
    print(generator.get_formula_by_degree(args.degree, add_color=not args.no_color))


if __name__ == '__main__':
    main()