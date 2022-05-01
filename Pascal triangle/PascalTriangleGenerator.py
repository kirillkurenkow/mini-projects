from typing import List

import colorama

colorama.init(autoreset=True, convert=False)
FORE = colorama.Fore


class PascalTriangleGenerator:
    def __init__(self, no_sub: bool = False):
        self.__triangle = [
            [1],
            [1, 1],
        ]
        self.__no_sub = no_sub
        self.__str_coefficients_mapping = '⁰¹²³⁴⁵⁶⁷⁸⁹'

    @property
    def __curr_level(self) -> int:
        return len(self.__triangle) - 1

    @property
    def triangle(self) -> List[List[int]]:
        return self.__triangle.copy()

    def __get_sub_degree(self, degree: int, empty_if_lt_1: bool = True) -> str:
        result = f''
        if empty_if_lt_1 and (degree <= 1):
            return result
        if self.__no_sub:
            return f'^{degree}'
        for i in str(degree):
            result += self.__str_coefficients_mapping[int(i)]
        return result

    def __add_triangle_level(self) -> None:
        new_level = [1, ]
        for i in range(len(self.__triangle[-1]) - 1):
            new_level.append(self.__triangle[-1][i] + self.__triangle[-1][i + 1])
        new_level.append(1)
        self.__triangle.append(new_level)

    def get_formula_by_degree(self, degree: int, add_color: bool = False) -> str:
        if self.__curr_level < degree:
            for _ in range(degree - self.__curr_level):
                self.__add_triangle_level()

        # Generate formula
        result = f'({FORE.GREEN if add_color else ""}a{FORE.RESET} - {FORE.BLUE if add_color else ""}b{FORE.RESET})' \
                 f'{self.__get_sub_degree(degree, add_color)} = '
        a_degree = degree
        b_degree = 0
        curr_sign = '-'

        for index, coefficient in enumerate(self.__triangle[-1]):
            # Coefficient
            temp = f'{FORE.RED if add_color else ""}{coefficient}{FORE.RESET}' if coefficient != 1 else ''

            # a and b degrees
            if a_degree > 0:
                temp += f'{FORE.GREEN if add_color else ""}a{FORE.RESET}' + self.__get_sub_degree(a_degree, add_color)
            if b_degree > 0:
                temp += f'{FORE.BLUE if add_color else ""}b{FORE.RESET}' + self.__get_sub_degree(b_degree, add_color)
            a_degree -= 1
            b_degree += 1

            # Sign
            result += temp + f' {curr_sign} '
            curr_sign = '+' if curr_sign == '-' else '-'

        # Remove +- at the end of result
        result = result.rstrip('-+ ')

        return result
