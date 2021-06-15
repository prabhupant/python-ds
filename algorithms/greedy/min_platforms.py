"""
Given the arrival and departure times of buses at a station
find the min number of platforms that must be there
"""


def find_platforms(arrival, departure):
    n = len(arrival)

    arrival.sort()
    departure.sort()

    i = 1
    j = 0

    ans = 1  # atleast one platform is required
    plat = 1

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            plat += 1
            i += 1

        elif arrival[i] > departure[j]:
            plat -= 1
            j += 1

        ans = max(ans, plat)


    return ans


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(find_platforms(arr, dep))
