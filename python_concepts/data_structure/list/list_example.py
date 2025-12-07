numbers = [10, 20,30]
numbers.append(40) #add
numbers[1] = 25 #modiy
numbers.remove(30) #remove
print(numbers) #output: [10,25,40]

# reverse the list without using reverse()

arr = [1,2,3,4,5]
rev = arr[::-1] #using slicing
print(rev)

#manual method

rev = []
for i in range(len(arr) -1, -1, -1):
    rev.append(arr[i])
print(rev)

#find the second larget number

arr = [10,20,4,45,99]
unique = list(set(arr))
unique.sort()

print(unique[-2])

#remove the duplicate number

arr = [1,2,3,4,4,5,2]

arr = list(set(arr))
print(arr)

#if order must be prserved

arr = [1,2,2,3,4,4,5]
result = []

for x in arr:
    if x not in result:
        result.append(x)

print(result)

#check if a list is a palindrome

arr = [1,2,3,2,1]
print(arr == arr[:: -1])

#find the frequency of each element

arr = [1,2,2,3,3,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)

#find common elements between two lists

a = [1,2,3,4]
b = [3,4,5,6]

common = list(set(a) & set(b))
print(common)

#find pair of numbers that sum to a target
#example target = 9

arr = [2,7,11,15,3,6]
target = 9
seen = set()
pairs = []

for num in arr:
    diff = target - num
    if diff in seen:
        pairs.append((num, diff))
    seen.add(num)
print(pairs)

#find the missing number in a list from 1 to n

arr = [1,2,4,5]

n = 5
missing = n*(n+1)//2 - sum(arr)
print(missing)

#flatten a nested list

nested = [[1,2], [3,4], [5]]
flat = [item for sub in nested for item in sub]
print(flat)

#find the longest increasing sub-list

arr = [1,2,2,3,4]

longest = []
current = []

for i in range(len(arr)):
    if i == 0 or arr[i] > arr[i-1]:
        current.append(arr[i])
    else:
        longest = max(longest, current, key=len)
        current = [arr[i]]
longest = max(longest, current, key=len)
print(longest)

"""Easy Level"""

#find the larget element in list

arr = [10,25,3,99]
print(max(arr))

#Count even and odd numbers

arr = [1,2,3,4,5,6]
even = len([x for x in arr if x % 2 == 0])
odd = len(arr) - even

print(even, odd)

#find all indexes of a given element

arr = [1,2,3,2,2,4]
target = 2

indexes = [i for i, v in enumerate(arr) if v == target]
print(indexes)

#remove all occurrences of an element

arr = [1,2,2,3,4]
arr = [x for x in arr if x != 2]
print(arr)

#split a list into chunks of size n

arr = [1,2,3,4,5]
n = 2
chunks = [arr[i: i + n] for i in range(0, len(arr), n)]
print(chunks)

#find the difference between two lists

a = [1,2,3]
b = [2,3,4]

diff = list(set(a) - set(b))
print(diff)

#find the elements that appear only once
arr = [1,2,3,2,1,4]
unique = [x for x in arr if arr.count(x) == 1]
print(unique)

#Rotate a list ( right rotation )

arr = [1,2,3,4,5]
k = 2

k %= len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)

#find all pairs whose sum is even

arr = [1,2,3,4]
pairs = []

for i in range(len(arr)) :
    for j in range(i+1, len(arr)):
        if (arr[i] + arr[j]) % 2 == 0:
            pairs.append((arr[i], arr[j]))
print(pairs)

#find duplicates in a list

arr = [1,2,3,2,3,4,5,5]

seen = set()
dup = set()

for x in arr:
    if x in seen:
        dup.add(x)
    seen.add(x)
print(list(dup))

#merge two sorted lists

a = [1,3,5]
b = [2,4,6]

i = j = 0
merged = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i]); i +=1
    else:
        merged.append(b[j]); j += 1
merged.extend(a[i:])
merged.extend(b[j:])

print(merged)

#Find the majority element(> n/2 times)

arr = [2,2,1,2,3,2]

for x in set(arr):
    if arr.count(x) > len(arr)//2:
        print(x)
        break


#move all zeros to the end

arr = [0,1,0,3,12]

result = [x for x in arr if x != 0] + [0] * arr.count(0)
print(result)

#Get interaction of two sorted lists

a = [1,2,3,5]
b = [2,3,4,5]

i = j = 0
res = []

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        res.append(a[j]); i +=1; j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(res)

""" Hard level """

arr = [1,2,3,1,1,1]
k = 3
sum_map = {0: -1}
s = 0
longest = 0

for i, x in enumerate(arr):
    s += x
    if s - k in sum_map:
        longest = max(longest, i - sum_map[s - k])
    if s not in sum_map:
        sum_map[s] = i
print(longest)

#Longest consecutive sequence

arr  = [100, 4, 200, 1, 3, 2]
s = set(arr)

longest = 0

for x in arr:
    if x - 1 not in s:
        y = x
        length = 1
        while y + 1 in s:
            y += 1
            length += 1
        length = max(longest, length)
print(longest)

#Find three numbers whose sum is zero(3-sum)

arr = [-1,0,1,2,-1,-4]
arr.sort()

res = []

for i in range(len(arr) - 2):
    if i > 0 and arr[i] == arr[i-1]:
        continue
l, r = i + 1, len(arr) - 1

while l < r:
    s = arr[i] + arr[l] + arr[r]
    if s == 0:
        res.append([arr[i], arr[l], arr[r]])
        l +=1; r -=1
        while l < r and arr[l] == arr[l - 1]: l += 1
        while l < r and arr[r] == arr[r + 1]: r -=1

    elif s < 0:
        l += 1
    else:
        r -= 1
print(res)

#maximum sum subarray(Kadane's alogrithm)

arr = [-2,1,-3, 4, -1,2,1,-5,4]

max_sum = curr = arr[0]
for x in arr[1:]:
    curr = max(x, curr + x)
    max_sum = max(max_sum, curr)
print(max_sum)
