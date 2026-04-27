import math

def generate_row(x):
    n = 0
    xmult = x
    while True:
        yield (n, 2 * (1 / ((2 * n + 1) * xmult)))
        xmult *= x**2
        n += 1

NANO_EPS = 1e-9

def emit_full_row(x_val, eps_val, f_val):
    """
    Generator of rows for table displaying approximation computation

    Args:
        x_val (float): argument of approximated function
        eps_val (float): required precision
        f_val (float): value of approximated function
    """

    sum_val = 0
    for n, row_val in generate_row(x_val):
        sum_val += row_val
        eps_cur = abs(f_val - sum_val)
        yield (x_val, n, f_val, sum_val, eps_cur)
        if eps_cur < eps_val:
            break
