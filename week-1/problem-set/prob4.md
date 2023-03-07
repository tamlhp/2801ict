The standard algorithm for finding the binary representation of a positive decimal integer involves the following steps:

Divide the decimal number by 2 and keep track of the remainder (either 0 or 1).
Divide the quotient (result of step 1) by 2 and keep track of the remainder.
Repeat step 2 until the quotient is zero.
Write down the remainders in reverse order to get the binary representation of the original decimal number.
For example, let's say we want to find the binary representation of the decimal number 13. We would follow these steps:

13 divided by 2 is 6 with a remainder of 1.
6 divided by 2 is 3 with a remainder of 0.
3 divided by 2 is 1 with a remainder of 1.
1 divided by 2 is 0 with a remainder of 1.
The remainders in reverse order are 1101, so the binary representation of the decimal number 13 is 1101.

Note that the binary representation of a decimal number can also be found using built-in functions in programming languages such as Python, but the standard algorithm described above provides a general approach that can be implemented manually or with basic programming constructs.

```
binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2
```
