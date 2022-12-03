names = ['Cecilia', 'Austin', 'Chistopher', 'Herry']
counts = [len(n) for n in names]
print(counts)

#  Case-1
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(f'longest_name  = {longest_name}')


#  Case-2
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(f'longest_name  = {longest_name}')


#  Case-3 (clean code)
for name, count in zip(name, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(f'longest_name  = {longest_name}')
