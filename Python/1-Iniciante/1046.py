# -*- coding:utf-8 -*-

a, b = map(int, input().split())

if a == b:
    print("O JOGO DUROU 24 HORA(S)")
elif a <= b:
    print("O JOGO DUROU %d HORA(S)" %(b - a))
else:
    print("O JOGO DUROU %d HORA(S)" %(24 - a + b))
