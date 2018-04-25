# -*- coding: utf-8 -*-

from myprint import myprint as _


'2.2 파이썬에서의 복소수'
_(3j)
_(1+3j)
_((1+3j) + (10+20j))
x = 1+3j
_((x-1)**2)
_(x.real)
_(x.imag)
_(type(1+2j))


'2.3 필드의 추상화'
def solve1(a, b, c): return (c-b)/a
_(solve1(10, 5, 30))
_(solve1(10+5j, 5, 20))


'2.4 복소수 필드 C 다루기'
from plotting import plot
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.75+1j, 3+1j, 3.25+1j}
def task_2_4_1():
    plot(S, 4)
'2.4.1 복소수의 절대값'
# abs(z)**2 == z.real**2 + z.imag**2
_(abs(3+4j))
_(abs(1+1j))
# Definition 2.4.2: 복소수 z의 공액 복소수 z.conjugate() == z.real - z.imag
_((3+4j).conjugate())
# abs(z)^2 == z * z.conjugate()
'2.4.2 복소수 덧셈하기'
def task_2_4_3():
    plot({1+2j+z for z in S}, 4)
def quiz_2_4_4():
    left_eye = 2+2j
    def f(z): return answer + z
    answer = -2-2j
    assert(f(left_eye) == 0)
'2.4.3 양의 실수로 복소수 곱하기'
def task_2_4_7():
    plot({z/2 for z in S}, 4)
'2.4.4 음수로 복소수 곱하기: 180도 회전'
'2.4.5 i를 곱하기: 90도 회전'
def task_2_4_8():
    plot({z*-1j/2 for z in S}, 4)
def task_2_4_9():
    plot({z*-1j/2 - 1j + 2 for z in S}, 4)
def task_2_4_10():
    from image import file2image
    data = file2image('img01.png')
    width = len(data[0])
    height = len(data)
    pts = {x + 1j*y for y, ps in enumerate(reversed(data))
                    for x, p in enumerate(ps)
                    if p[0] < 120}
    plot(pts, max(width, height), 1)
def f(s):
    reals = {z.real for z in s}
    imags = {z.imag for z in s}
    rc = (max(reals) - min(reals)) / 2
    ic = (max(imags) - min(imags)) / 2
    return {z -rc - 1j*ic for z in s}
def task_2_4_11():
    plot(f(S))
def task_2_4_12():
    from image import file2image
    data = file2image('gopher.png')
    width = len(data[0])
    height = len(data)
    pts = {x + 1j*y for y, ps in enumerate(reversed(data))
                    for x, p in enumerate(ps)
                    if p[0] < 120}
    plot(f(pts), max(width, height), 1)
task_2_4_12()