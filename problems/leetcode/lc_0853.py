"""
PROBLEM   : Car Fleet
DIFFICULTY: medium
PATTERN   : stack, greedy
TRIGGER   : cars reaching target, speed, merge into fleets
INTUITION : Sort cars by starting position (closest to target first). Compute each car's time to
            reach the target. Iterate from closest to farthest: if a car behind arrives no sooner
            than the one ahead, it catches up and joins that fleet; otherwise it forms a new fleet.
            Count distinct fleet times on the stack.
"""

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pairs = sorted(zip(position, speed), reverse=True)
    stack = []

    for pos, spd in pairs:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)
