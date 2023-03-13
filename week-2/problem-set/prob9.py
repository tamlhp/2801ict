def order_queue_two(original_queue):
    q1 = []
    q2 = []
    current_min = original_queue.pop(0)

    while original_queue:
        next_element = original_queue.pop(0)
        if next_element < current_min:
            q1.append(current_min)
            current_min = next_element
        else:
            q1.append(next_element)

    q1.append(current_min)

    while q1:
        q2.append(q1.pop(0))
        while q1 and q2 and q2[-1] > q1[0]:
            q1.append(q2.pop(-1))

    while q2:
        original_queue.append(q2.pop(0))


def order_queue_one(original_queue):
    sorted_queue = []

    while original_queue:
        current_element = original_queue.pop(0)

        while sorted_queue and sorted_queue[-1] > current_element:
            original_queue.append(sorted_queue.pop())

        sorted_queue.append(current_element)

    while sorted_queue:
        original_queue.append(sorted_queue.pop(0))


my_queue = [4, 1, 3, 2, 5]
order_queue_two(my_queue)
print(my_queue)  # [1, 2, 3, 4, 5]

y_queue = [4, 1, 3, 2, 5]
order_queue_one(my_queue)
print(my_queue)  # [1, 2, 3, 4, 5]
