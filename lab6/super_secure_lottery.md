# Challenge `Super Secure Lottery` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Buffer overflow_

- Where: Where is the vulnerability present
  - _`guess` variable in `run_lottery` function_

- Impact: What results of exploiting this vulnerability
    - _Allows, in function `run_lottery`, to overwrite the values of both `guess` local buffer and `prize` function argument, which are compared to check if the flag should be printed, ending up printing the flag_

NOTE: After analyzing both the source code and the binary using a debugger, it was found that even though the program checks the length of the input by using the function `read`, it allows to read up to 64 bytes into the buffer `guess`, which is only 8 bytes long. This results in a buffer overflow vulnerability. During the execution of the function `run_lottery`, the local variable `guess` is allocated at `0xffffd104` and the function argument `prize` is allocated at `0xffffd0fc`. The argument `prize` contains the reference to the address of the `lottery` buffer allocated in the `main` function, `0xffffd134`, which was previously pushed into the stack. This results in a difference of 48 bytes between the variables which are compared in the function compared to check if the flag should be printed.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload of 56 equal bytes, filling both the buffer `guess` and the buffer referenced by the argument `prize` with the same content, overwriting the value of both variables to be equal, bypassing the check and printing the flag. Note that the first 8 bytes fill the buffer `guess`, the following 40 fill the offset between the two buffers and the last 8 bytes fill the buffer referenced by the argument `prize`.

The script to reproduce the challenge is available at [super_secure_lottery.py](super_secure_lottery.py)
