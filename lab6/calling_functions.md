# Challenge `Calling functions` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Buffer overflow_

- Where: Where is the vulnerability present
  - `buffer` variable in `main` function

- Impact: What results of exploiting this vulnerability
    - _Allows to overwrite the value of the local variable `fp`, which can be used to `win` function, ending up printing the flag_

NOTE: After analyzing both the source code and the binary using a debugger, it was found that the local variable `fp` was allocated on the stack right after the variable `buffer`, so, by overflowing the buffer, we could overwrite the value of `fp`, a function pointer which is later called, and make it point to the `win` function, which will cause the flag to be printed. More precisely, the variable `fp` was allocated at `0xffffd12c` and the variable `buffer`, corresponding to a char array of size 32, was allocated at `0xffffd10c`. This results in a difference of 32 addresses between the two variables. Moreover, the `win` function was located at `0x080486f1`.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload of 36 bytes where the last 4 bytes are equal to `0x080486f1`, filling the buffer with garbage and overwriting the value of `fp` to be equal to `0x080486f1`, making it point to the `win` function, which will cause the flag to be printed later when the function pointer is called.

The script to reproduce the challenge is available at [calling_functions.py](calling_functions.py)

