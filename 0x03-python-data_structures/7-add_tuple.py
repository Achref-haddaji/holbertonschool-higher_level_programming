#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	tuple_c = ()
    i = len(tuple_a)
    j = len(tuple_b)

    if i < 2:
        tuple_a += (0, 0,)

    if j < 2:
        tuple_b += (0, 0,)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    tuple_c += (a, b, )
    return tuple_c
