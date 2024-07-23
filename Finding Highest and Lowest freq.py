arr = [10, 5, 10, 15, 10, 5]
v = []
f = {}

for i in range(len(arr)):
    count = 1
    if arr[i] in v:
        continue  # Skip this element as it is already processed
    else:
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        v.append(arr[i])
        f[arr[i]] = count
        print(arr[i], count)

# To see the final frequency dictionary
print(f)
print(min(f, key=lambda k: f[k]))
print(max(f, key=lambda k: f[k]))
