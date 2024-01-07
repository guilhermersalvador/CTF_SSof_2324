# Challenge `Return address` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Buffer overflow_

- Where: Where is the vulnerability present
  - _`buffer` variable in `challenge` function_

- Impact: What results of exploiting this vulnerability
    - _Allows to overwrite the return address of the `challenge` function, making it point to the `win` function, ending up printing the flag, instead of returning to the caller function_

NOTE: After analyzing both the source code and the binary using a debugger, it was found that, during the execution of the `challenge` function, the saved `eip` containing the return address was located at `0xffffd13c` and the variable `buffer`, corresponding to a char array of size 10, was allocated at `0xffffd126`. This results in a difference of 22 addresses between the two variables. Moreover, the `win` function was located at `0x080486f1`.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload of 26 bytes where the last 4 bytes are equal to `0x080486f1`. This way, the first 10 bytes will fill the buffer with garbage, the following 12 bytes will fill the offset between the end of the buffer and the saved `eip` and the last 4 bytes will overwrite the return address of the `challenge` function, making it point to the `win` function, which will cause the flag to be printed later when the `challenge` function returns.

The script to reproduce the challenge is available at [return_address.py](return_address.py)