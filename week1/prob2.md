- After the first pass, every locker is open
- After the second pass, every second locker is toggled, so the even-numbered lockers are closed, and the odd-numbered lockers are open.
- This means that if i divides the locker number evenly (i.e., locker number j is a multiple of i), then locker j will be toggled on the ith pass. Therefore, after the n passes, the lockers that remain open are exactly the lockers that have an odd number of factors.

For example, locker #1 has only one factor (itself), so it will be toggled on every pass and end up closed. Locker #2 has two factors (1 and 2), so it will be toggled on the first and second passes and end up closed. Locker #3 has two factors (1 and 3), so it will be toggled on the first and third passes and end up open. Locker #4 has three factors (1, 2, and 4), so it will be toggled on the first, second, and fourth passes and end up open, and so on.

It is a well-known fact that a positive integer has an odd number of factors if and only if it is a perfect square. Therefore, after the n passes, the lockers that remain open are exactly the lockers that are perfect squares. There are exactly floor(sqrt(n)) perfect squares between 1 and n, so the answer is that floor(sqrt(n)) lockers are open.
