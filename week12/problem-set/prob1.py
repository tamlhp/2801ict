import math
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def merge_sort(points, key):
    if len(points) <= 1:
        return points
    middle = len(points) // 2
    left = merge_sort(points[:middle], key)
    right = merge_sort(points[middle:], key)

    return merge(left, right, key)


def merge(left, right, key):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def closest_pair(points, sorted_y):
    if len(points) <= 3:
        min_distance = float('inf')
        min_pair = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = euclidean_distance(points[i], points[j])
                if distance < min_distance:
                    min_distance = distance
                    min_pair = (points[i], points[j])
        return min_pair, min_distance

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    left_sorted_y = [p for p in sorted_y if p in left_points]
    right_sorted_y = [p for p in sorted_y if p in right_points]

    left_pair, left_distance = closest_pair(left_points, left_sorted_y)
    right_pair, right_distance = closest_pair(right_points, right_sorted_y)
    min_pair = left_pair if left_distance < right_distance else right_pair
    min_distance = min(left_distance, right_distance)

    strip_points = [p for p in sorted_y if abs(p[0] - points[mid][0]) < min_distance]

    for i in range(len(strip_points)):
        for j in range(i + 1, len(strip_points)):
            if strip_points[j][1] - strip_points[i][1] >= min_distance:
                break
            distance = euclidean_distance(strip_points[i], strip_points[j])
            if distance < min_distance:
                min_distance = distance
                min_pair = (strip_points[i], strip_points[j])

    return min_pair, min_distance


def main():
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (30, 25)]
    sorted_points = merge_sort(points, 0)
    sorted_y = merge_sort(points, 1)
    min_pair, min_distance = closest_pair(sorted_points, sorted_y)
    print(f"Closest pair: {min_pair}")
    print(f"Minimum distance: {min_distance}")

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    x_res = [point[0] for point in min_pair]
    y_res = [point[1] for point in min_pair]
    col = ['red' if point in min_pair else 'blue' for point in points ]
    plt.plot(x_res,y_res)
    plt.scatter(x,y,c = col)
    plt.show()


if __name__ == "__main__":
    main()
