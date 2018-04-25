# -*- coding: utf-8 -*-

from myprint import myprint as __


'2.2 파이썬에서의 복소수'
__(3j)
__(1+3j)
__((1+3j) + (10+20j))
x = 1+3j
__((x-1)**2)
__(x.real)
__(x.imag)
__(type(1+2j))


'2.3 필드의 추상화'
def solve1(a, b, c): return (c-b)/a
__(solve1(10, 5, 30))
__(solve1(10+5j, 5, 20))


'2.4 복소수 필드 C 다루기'
from plotting import plot
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.75+1j, 3+1j, 3.25+1j}
def task_2_4_1():
    plot(S, 4)
'2.4.1 복소수의 절대값'
# abs(z)**2 == z.real**2 + z.imag**2
__(abs(3+4j))
__(abs(1+1j))
# Definition 2.4.2: 복소수 z의 공액 복소수 z.conjugate() == z.real - z.imag
__((3+4j).conjugate())
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
    from image import file2image, color2gray
    data = color2gray(file2image('gopher.png'))
    pts = {x + 1j*y for y, ps in enumerate(reversed(data))
                    for x, p in enumerate(ps)
                    if p[0] < 150}
    width = max(abs(z.real) for z in pts)
    height = max(abs(z.imag) for z in pts)
    plot(pts, max(width, height), 1)
def f(s):
    reals = {z.real for z in s}
    imags = {z.imag for z in s}
    rc = (max(reals) - min(reals)) / 2
    ic = (max(imags) - min(imags)) / 2
    return {z - rc - 1j*ic for z in s}
def task_2_4_11():
    plot(f(S))
def task_2_4_12():
    from image import file2image, color2gray
    data = color2gray(file2image('gopher.png'))
    pts = {x + 1j*y for y, ps in enumerate(reversed(data))
                    for x, p in enumerate(ps)
                    if p < 150}
    width = max(abs(z.real) for z in pts)
    height = max(abs(z.imag) for z in pts)
    pts2 = f(pts)
    plot(pts2, max(width, height), 1)
'2.4.6 복소 평면의 단위원: 편각과 각도'
'2.4.7 오일러 공식'
def task_2_4_17():
    from math import e, pi
    n = 20
    w = e ** (2j * pi / n)
    plot([w ** x for x in range(n)])
'2.4.8 복소수에 대한 극좌표 표현'
# z = r*e**(1j*θ)
'2.4.9 첫 번째 지수 법칙'
# e**u * e**v == e**(u+v)
'2.4.10 τ 라디안 회전'
# f(z) = z*e**(1j*τ)
def task_2_4_18():
    from math import e, pi
    plot({z * e**(pi/4 * 1j) for z in S})
def task_2_4_19():
    from math import e, pi
    from image import file2image, color2gray
    data = color2gray(file2image('gopher.png'))
    pts = {x + 1j*y for y, ps in enumerate(reversed(data))
                    for x, p in enumerate(ps)
                    if p < 150}
    width = max(abs(z.real) for z in pts)
    height = max(abs(z.imag) for z in pts)
    pts2 = {z * e**(pi/4 * 1j) for z in pts}
    plot(pts2, max(width, height), 1)
'2.4.11 연산 결합하기'
def task_2_4_20():
    from math import e, pi
    from image import file2image, color2gray
    data = color2gray(file2image('gopher.png'))
    pts = {x + 1j*y for y, ps in enumerate(reversed(data))
                    for x, p in enumerate(ps)
                    if p < 150}
    width = max(abs(z.real) for z in pts)
    height = max(abs(z.imag) for z in pts)
    pts2 = f(pts)
    pts3 = {z * e**(pi/4 * 1j) / 2 for z in pts2}
    plot(pts3, max(width, height), 1)
'2.4.12 3차원 이상의 경우'


'2.5 GF(2)에 대해 알아보기'
# GF(2): Galois Field 2
#
# *|0 1
# 0|0 0
# 1|0 1
#
# +|0 1
# 0|0 1
# 0|1 0
from GF2 import one
__(one*one)
__(one*0)
__(one + 0)
__(one+one)
__(-one)
'2.5.1 완벽한 비밀 유지 - 다시 방문'
# p k|c
# 0 ♣|0
# 0 ♡|1
# 1 ♣|1
# 1 ♥|0
#
# k -> k + p는 가역적(단사, 전사)
#
# p k|c
# 0 0|0
# 0 1|1
# 1 0|1
# 1 1|0
#
# 키 비트열 k1 ... kn
# 평문 p1 ... pn
# 암호문 c1 ... cn
# c1 = k1 + p1
# c2 = k2 + p2
# ...
# cn = kn + pn
# c는 p에 대해 주는 정보가 아무것도 없다. 그러므로 완벽한 비밀 유지가 가능하다.
# 이러한 암호체계를 one-time pad라고 부른다.
'2.5.1 네트워크 코딩(Network coding)'


'2.6 Review questions'


'2.7 Problems'
