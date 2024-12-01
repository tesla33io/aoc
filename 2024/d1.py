import sys

import rich
from rich.panel import Panel


def read_input(filename: str) -> list[list[int]]:
    a: list[int] = []
    b: list[int] = []
    with open(filename, "r") as input:
        for line in input.readlines():
            x1, x2 = line.split("   ")
            a.append(int(x1))
            b.append(int(x2))
    return [a, b]


def solution_p1(a: list[int], b: list[int]) -> int:
    a = sorted(a)
    b = sorted(b)
    dist: int = 0
    for i in range(len(a)):
        dist += abs(a[i] - b[i])
    return dist


def solution_p2(a: list[int], b: list[int]) -> int:
    sim_score: int = 0
    for x in a:
        sim_score += x * b.count(x)
    return sim_score


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    input = read_input(sys.argv[1])
    sol1: int = solution_p1(input[0].copy(), input[1].copy())
    sol2: int = solution_p2(input[0], input[1])
    rich.print(
        Panel(
            f"[green]Main solution:  {sol1}\n[yellow]Bonus solution: {sol2}",
            title="AoC-2024 Day 1",
            style="magenta",
            expand=False,
        )
    )
