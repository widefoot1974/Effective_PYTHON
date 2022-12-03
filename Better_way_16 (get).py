counters = {}
key = 0

# case-1
if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1


# case-2
if key not in counters:
    counters[key] = 0

counters[key] += 1


# case-3
try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1


# case-4
count = counters.get(key, 0)
counters[key] = count + 1
