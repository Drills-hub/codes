import sys
input = sys.stdin.readline

a, b, c = map(int, (input()).split())
simsin, vip = map(int, (input()).split())
level = int(input())


def solution(a, b, c, simsin, vip, level):
    target_exp = (250 - level) * 100
    if target_exp <= 0:
        return 0

    total_time = 0
    vip_time_cap = vip * 30
    if target_exp > 0 and vip_time_cap > 0:
        vip_time = min(vip_time_cap, (target_exp + c - 1) // c)
        target_exp -= vip_time * c
        total_time += vip_time
    simsin_time_cap = simsin * 30

    if target_exp > 0 and simsin_time_cap > 0:
        simsin_time = min(simsin_time_cap, (target_exp + b - 1) // b)
        target_exp -= simsin_time * b
        total_time += simsin_time

    if target_exp > 0:
        event_time = (target_exp + a - 1) // a
        total_time += event_time
        target_exp -= event_time * a

    return total_time


print(solution(a, b, c, simsin, vip, level))