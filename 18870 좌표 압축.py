import collections

n = int(input())
cood_x = list(map(int, input().split()))

coord_counts = collections.Counter(cood_x)
sorted_unique_coords = sorted(coord_counts)

coord_to_index = {coord: i for i, coord in enumerate(sorted_unique_coords)}

for x in cood_x:
    index = coord_to_index[x]
    print(index, end=" ")
