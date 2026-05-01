"""
PROBLEM   : Capacity to Ship Packages Within D Days
DIFFICULTY: medium
PATTERN   : binary search
TRIGGER   : minimum capacity, ship within d days, feasibility check
INTUITION : Binary search on ship capacity from max(weights) to sum(weights). For each
            candidate capacity, simulate how many days are needed; shrink or expand the
            range until the minimum valid capacity is found.
"""

# Search space = ship capacity
# Condition = days it will take
    

def main():
    weights = [3,2,2,4,1,4]
    days = 3
    l = max(weights)
    r = sum(weights)

    while l < r:
        mid_cap = (l + r) // 2

        days_elapsed = days_it_will_take(weights, mid_cap)

        if days_elapsed == days:
            print(mid_cap)
            exit()
        elif days_elapsed > days:
            l = mid_cap + 1
        else:
            # works, but we can try a smaller capacity
            r = mid_cap

def days_it_will_take(weights, ship_capacity): # ship capacity that we will test
    current_weights = 0
    days = 1

    for w in weights:
        if current_weights + w > ship_capacity:
            current_weights = 0
            days += 1
        current_weights += w        

    return days 

main()