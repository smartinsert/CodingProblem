"""
A car factory has two assembly lines, each with n stations. A station is denoted by Si,j where i is either 1 or 2 and
indicates the assembly line the station is on, and j indicates the number of the station. The time taken per station is
denoted by ai,j. Each station is dedicated to some sort of work like engine fitting, body fitting, painting and so on.
So, a car chassis must pass through each of the n stations in order before exiting the factory. The parallel stations
of the two assembly lines perform the same task. After it passes through station Si,j, it will continue to station
Si,j+1 unless it decides to transfer to the other line. Continuing on the same line incurs no extra cost, but
transferring from line i at station j – 1 to station j on the other line takes time ti,j. Each assembly line takes an
entry time ei and exit time xi which may be different for the two lines. Give an algorithm for computing the minimum
time it will take to build a car chassis.
"""


def assembly_line_dp(e, a, t, x):
    assembly_line_length = len(a[0])
    t1 = [0 for _ in range(assembly_line_length)]
    t2 = [0 for _ in range(assembly_line_length)]

    t1[0] = e[0] + a[0][0]
    t2[0] = e[1] + a[1][0]

    for i in range(1, assembly_line_length):
        t1[i] = min(t1[i-1] + a[0][i],
                    t2[i-1] + t[1][i] + a[0][i])
        t2[i] = min(t2[i - 1] + a[1][i],
                    t1[i - 1] + t[0][i] + a[1][i])
    return min(t1[assembly_line_length - 1] + x[0],
               t2[assembly_line_length - 1] + x[1])


def assembly_line_recursive(e, a, t, x):
    assembly_line_length = len(a[0]) - 1
    return min((assembly_line_helper(e, a, t, x, assembly_line_length, 0) + x[0]),
               (assembly_line_helper(e, a, t, x, assembly_line_length, 1) + x[1]))


def assembly_line_helper(e, a, t, x, n, line):
    if n == 0:
        return e[line] + a[line][0]

    t0 = float('inf')
    t1 = float('inf')

    if line == 0:
        t0 = min((assembly_line_helper(e, a, t, x, n-1, 0) + a[0][n]),
                 (assembly_line_helper(e, a, t, x, n-1, 1) + t[1][n] + a[0][n]))
    else:
        t1 = min((assembly_line_helper(e, a, t, x, n - 1, 1) + a[1][n]),
                 (assembly_line_helper(e, a, t, x, n - 1, 0) + t[0][n] + a[1][n]))
    return min(t0, t1)


if __name__ == '__main__':
    e = [10, 12]
    a = [[4, 5, 3, 2],
         [2, 10, 1, 4]]
    t = [[0, 7, 4, 5],
         [0, 9, 2, 8]]
    x = [18, 7]

    assert assembly_line_dp(e, a, t, x) == 35
    assert assembly_line_recursive(e, a, t, x) == 35

