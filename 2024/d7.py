import sys
import os

def solution_p1(eqs: list[str]) -> int:
    correct: list[int] = []
    for eq in eqs:
        test_val: int = int(eq.split(':')[0])
        ops: list[int] = [int(op) for op in eq.split(':')[1].strip().split()]
        for i in range(2**len(ops)):
            idk: int = ops[0]
            for j in range(1, len(ops)):
                if i & (1 << (j-1)):
                    idk *= ops[j]
                else:
                    idk += ops[j]
            if idk == test_val:
                correct.append(test_val)
    return sum(set(correct))

def solution_p2():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(1)
    with open(sys.argv[1], 'r') as ifile:
        eqs: list[str] = ifile.readlines()
        sol1: int = solution_p1(eqs)
        print(sol1)
