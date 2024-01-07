# Challenge `Simple Overflow` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Buffer overflow_

- Where: Where is the vulnerability present
  - `buffer` variable in the `main` function

- Impact: What results of exploiting this vulnerability
    - _Allows to overwrite the value of the local variable `test`, which is used to check if the flag should be printed, ending up printing the flag_

NOTE: After analyzing both the source code and the binary using a debugger, it was found that the local variable `test` was allocated on the stack right after the variable `buffer`, so, by overflowing the buffer, we could overwrite the value of `test`, an integer, and make it non-zero, which will cause the flag to be printed. More precisely, the variable `test` was allocated at `0xffffd12c` and the variable `buffer`, corresponding to a char array of size 128, was allocated at `0xffffd0ac`. This results in a difference of 128 addresses between the two variables.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload of 129 bytes where the last byte is non-zero, filling the buffer with garbage and overwriting the value of `test` to be non-zero, bypassing the check and printing the flag.

The script to reproduce the challenge is available at [simple_overflow.py](simple_overflow.py)