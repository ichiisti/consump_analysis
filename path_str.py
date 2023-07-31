"""
PATH:
----------
Define path for local package and module. Do not modify it !!!!!!
"""


from sys import path
from constants import __PATH_CONN_STR, __PATH_STR_PKG


def add_path(p_path: str) -> None:
    path.append(p_path)


add_path(__PATH_STR_PKG)
add_path(__PATH_CONN_STR)


# for i in path:
#     print(i)
