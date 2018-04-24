# -*- coding: utf-8 -*-

from myprint import myprint as m


'2.2 파이썬에서의 복소수'
m(3j)
m(1+3j)
m((1+3j) + (10+20j))
x = 1+3j
m((x-1)**2)
m(x.real)
m(x.imag)
m(type(1+2j))


'2.3 필드의 추상화'
def solve1(a, b, c): return (c-b)/a
m(solve1(10, 5, 30))
m(solve1(10+5j, 5, 20))


'2.4 복소수 필드 C 다루기'
def task_2_4_1():
    from plotting import plot
    S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.75+1j, 3+1j, 3.25+1j}
    plot(S, 4)
'2.4.1 복소수의 절대값'
# abs(z)**2 == z.real**2 + z.imag**2
m(abs(3+4j))
m(abs(1+1j))
# Definition 2.4.2: 복소수 z의 공액 복소수 z.conjugate() == z.real - z.imag
m((3.4j).conjugate())
# abs(z)^2 == z  z.conjugate()
m((3.4j) * (3.4j).conjugate())