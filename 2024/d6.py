import sys
import os
import time
import copy

def rotate_guard(g: str) -> str:
    ret: list[str] = ['>', 'v', '<', '^']
    return ret[(ret.index(g) + 1) % 4]

def print_map(map: list[str]) -> None:
    os.system('cls' if os.name=='nt' else 'clear')
    print("-"*(len(map[0]) + 3))
    for row in map:
        print(f"| {row.strip()} |")
    print("-"*(len(map[-1]) + 3))

def solution_p1(map: list[str]) -> list[tuple[int,int]]:
    gx: int = -1
    gy: int = -1
    g: str = '.'
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in '^><v':
                gx = x
                gy = y
                g = map[y][x]
    positions: list[tuple[int,int]] = [(gy, gx)]
    while 0 <= gx <= len(map[gy]) and 0 <= gy <= len(map):
        map[gy] = map[gy][:gx] + '.' + map[gy][gx+1:]
        if g == '^':
            if gy - 1 < 0:
                break # Reached upper border
            elif map[gy - 1][gx] == '#':
                g = rotate_guard(g)
                continue
            else:
                gy -= 1
        elif g == 'v':
            if gy + 1 >= len(map):
                break # Reached bottom border
            elif map[gy + 1][gx] == '#':
                g = rotate_guard(g)
                continue
            else:
                gy += 1
        elif g == '<':
            if gx - 1 < 0:
                break # Reached left border
            elif map[gy][gx - 1] == '#':
                g = rotate_guard(g)
                continue
            else:
                gx -= 1
        elif g == '>':
            if gx + 1 >= len(map[gy]):
                break # Reached right border
            elif map[gy][gx + 1] == '#':
                g = rotate_guard(g)
                continue
            else:
                gx += 1
        else:
            raise Exception("FTW is with the Guard???")
        map[gy] = map[gy][:gx] + g + map[gy][gx+1:]
        if (gy, gx) not in positions:
            positions.append((gy, gx))
        #print_map(map)
        #time.sleep(0.01)
    #return len(set(positions))
    return positions

def has_loop(map: list[str]) -> bool:
    gx, gy, g = -1, -1, '.'
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in '^><v':
                gx, gy, g = x, y, map[y][x]
    if gx < 0 or gy < 0 or g not in '^><v':
        raise Exception("Couldn't find posiont of the guard")
    visited = set()
    while 0 <= gx <= len(map[gy]) and 0 <= gy <= len(map):
        if (gy, gx, g) in visited:
            return True
        visited.add((gy, gx, g))
        if g == '^':
            if gy - 1 < 0:
                break
            elif map[gy - 1][gx] in '#O':
                g = rotate_guard(g)
            else:
                gy -= 1
        elif g == 'v':
            if gy + 1 >= len(map):
                break
            elif map[gy + 1][gx] in '#O':
                g = rotate_guard(g)
            else:
                gy += 1
        elif g == '<':
            if gx - 1 < 0:
                break
            if map[gy][gx - 1] in '#O':
                g = rotate_guard(g)
            else:
                gx -= 1
        elif g == '>':
            if gx + 1 >= len(map[gy]):
                break
            if map[gy][gx + 1] in '#O':
                g = rotate_guard(g)
            else:
                gx += 1
        else:
            raise Exception("Invalid direction")
        #print_map(map)
        #time.sleep(0.05)
    return False

def solution_p2(map: list[str]) -> int:
    tmp_map = copy.deepcopy(map)
    to_try: list[tuple[int, int]] = solution_p1(tmp_map)[2:]
    loops: int = 0
    for pos in to_try:
        tmp_map = copy.deepcopy(map)
        tmp_map[pos[0]] = tmp_map[pos[0]][:pos[1]] + 'O' + tmp_map[pos[0]][pos[1]+1:]
        if has_loop(tmp_map):
            loops += 1
        #print_map(tmp_map)
        #time.sleep(0.3)
        print(f"Tried: {pos} | Loops: {loops}", end='\r')
    return loops


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(1)
    with open(sys.argv[1], 'r') as finput:
        map = finput.readlines()
        #sol1: int = solution_p1(map)
        #print(sol1)
        sol2: int = solution_p2(map)
        print(f"{sol2}" + " "*50)
