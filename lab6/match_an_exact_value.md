# Challenge `Match an exact value` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Buffer overflow_

- Where: Where is the vulnerability present
  - `buffer` variable in the `main` function

- Impact: What results of exploiting this vulnerability
    - _Allows to overwrite the value of the local variable `test`, which is used to check if the flag should be printed, ending up printing the flag_

NOTE: After analyzing both the source code and the binary using a debugger, it was found that the local variable `test` was allocated on the stack right after the variable `buffer`, so, by overflowing the buffer, we could overwrite the value of `test`, an integer, making it equal to the hex value `0x61626364`, which satisfies the condition of the if statement controlling the printing of the flag. More precisely, the variable `test` was allocated at `0xffffd13c` and the variable `buffer`, corresponding to a char array of size 64, was allocated at `0xffffd0fc`. This results in a difference of 64 bytes between the two variables.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload of 68 bytes where the last 4 bytes are equal to `0x61626364`, filling the buffer with garbage and overwriting the value of `test` to be equal to `0x61626364`, bypassing the check and printing the flag.

The script to reproduce the challenge is available at [match_an_exact_value.py](match_an_exact_value.py)