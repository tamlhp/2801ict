import itertools

def cross_bridge(combination, arrived, solution):
    travel_time = 0
    travel_time += max(combination)
    arrived.extend(list(combination))
    flash_return = min(arrived)
    arrived.remove(flash_return)
    travel_time += flash_return
    remaining = [time for time in times if time not in arrived]
    solution += "\nBring {} and {} to the other side and bring {} back".format(times.index(combination[0])+1, times.index(combination[1])+1, times.index(flash_return)+1)
    return arrived, remaining, travel_time, solution

if __name__ == "__main__":
    # define the time each person takes to cross the bridge
    times = [1, 2, 5, 10]

    # define the total time allowed to cross the bridge
    time_limit = 17

    # generate all possible solutions of people crossing the bridge
    first_go = list(itertools.combinations(times, 2))
    solutions = []
    for comb_first in first_go:
        tmp_done = []
        tmp_solution = ""
        tmp_total_time = 0
        tmp_done, remaining, travel_time, tmp_solution = cross_bridge(comb_first, tmp_done, tmp_solution)
        tmp_total_time += travel_time
        second_go = list(itertools.combinations(remaining, 2))
        for comb_sec in second_go:
            solution = tmp_solution
            total_time = tmp_total_time
            _, remaining, travel_time, solution = cross_bridge(comb_sec, tmp_done.copy(), solution)
            total_time += travel_time
            total_time += max(remaining)
            if total_time <= time_limit:
                solution += "\nBring {} and {} to the other side".format(times.index(remaining[0]+1), times.index(remaining[1])+1)
                solution += "\nTotal time: {} minutes".format(total_time)
                solutions.append(solution)

    for sol in solutions:
        print(sol)