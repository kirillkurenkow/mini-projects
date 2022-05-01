from typing import List

import colorama

colorama.init(autoreset=True, convert=False)
FORE = colorama.Fore


class PascalTriangleGenerator:
    """
    Class for generating Pascal triangle and formulas
    """
    def __init__(self, no_superscript: bool = False):
        self.__triangle = [
            [1],
            [1, 1],
        ]
        self.__no_superscript = no_superscript
        self.__str_coefficients_mapping = '⁰¹²³⁴⁵⁶⁷⁸⁹'

    @property
    def __curr_level(self) -> int:
        """
        Current triangle level

        :return: Triangle len - 1
        """
        return len(self.__triangle) - 1

    @property
    def triangle(self) -> List[List[int]]:
        """
        Current triangle copy

        :return:
        [
            [1],
            [1, 1],
            ...
        ]
        """
        return self.__triangle.copy()

    def __get_degree(self, degree: int, empty_if_lt_1: bool = True) -> str:
        """
        Method for formula generating.

        :param degree: Degree
        :param empty_if_lt_1: Return empty string if degree less than 1

        :return: superscript degree or ^degree
        """
        result = f''
        if empty_if_lt_1 and (degree <= 1):
            return result
        if self.__no_superscript:
            return f'^{degree}'
        for i in str(degree):
            result += self.__str_coefficients_mapping[int(i)]
        return result

    def __add_triangle_level(self) -> None:
        """
        Adds 1 level to triangle

        :return: None
        """
        new_level = [1, ]
        for i in range(len(self.__triangle[-1]) - 1):
            new_level.append(self.__triangle[-1][i] + self.__triangle[-1][i + 1])
        new_level.append(1)
        self.__triangle.append(new_level)

    def get_formula_by_degree(self, degree: int, add_color: bool = False) -> str:
        """
        Returns formula for degree

        :param degree: Degree
        :param add_color: Use color highlight

        :return: Formula str
        """
        if self.__curr_level < degree:
            for _ in range(degree - self.__curr_level):
                self.__add_triangle_level()

        # Generate formula
        result = f'({FORE.GREEN if add_color else ""}a{FORE.RESET} - {FORE.BLUE if add_color else ""}b{FORE.RESET})' \
                 f'{self.__get_degree(degree, add_color)} = '
        a_degree = degree
        b_degree = 0
        curr_sign = '-'

        for index, coefficient in enumerate(self.__triangle[-1]):
            # Coefficient
            temp = f'{FORE.RED if add_color else ""}{coefficient}{FORE.RESET}' if coefficient != 1 else ''

            # a and b degrees
            if a_degree > 0:
                temp += f'{FORE.GREEN if add_color else ""}a{FORE.RESET}' + self.__get_degree(a_degree, add_color)
            if b_degree > 0:
                temp += f'{FORE.BLUE if add_color else ""}b{FORE.RESET}' + self.__get_degree(b_degree, add_color)
            a_degree -= 1
            b_degree += 1

            # Sign
            result += temp + f' {curr_sign} '
            curr_sign = '+' if curr_sign == '-' else '-'

        # Remove +- at the end of result
        result = result.rstrip('-+ ')

        return result
