# Challenge `Super Secure System` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Buffer overflow_

- Where: Where is the vulnerability present
  - _`buffer` variable in `check_password` function_

- Impact: What results of exploiting this vulnerability
    - _Allows to overwrite the return address of the function `check_password` with the address of the instruction that prints the flag, bypassing the check and printing the flag_

NOTES: 
- After analyzing both the source code and the binary using a debugger, we could see that, in function `main`, although the user input was limited to 63 characters since it was received using the `read` function, it was later passed to the function `check_password`, being copied to a buffer of size 32, `buffer`, using the `strcpy` function, which does not perform any bounds checking. This allows us to overflow the buffer and overwrite the return address of the function `check_password` with the address of the instruction that prints the flag. During the 
execution of the function `check_password`, its return address was located at `0xffffd0dc` and the variable `buffer`, was allocated at `0xffffd0b0`. This results in a difference of 44 addresses between the two variables. Moreover, the instruction that prints the flag at function `main` was located at `0x080487e9`.

 - Simply overflowing the buffer with 44 bytes of garbage and 4 bytes equal to `0x080487e9` will overwrite the return address of the function `check_password`, but will also cause the program to crash since the register `ebx`, at address `0xffffd0d4`, will be overwritten with garbage. This behavior occurs since after returning from the function `check_password`, the program uses the value of `ebx` to call the function `printf`, so it must not be overwritten with garbage.

- To avoid void the corruption of the register `ebx`, we could simply place its normal value as part of the payload, which is `0x804a000`. However, this content contains the null byte, which will cause the `strcpy` function to stop copying the content of the payload to the buffer. To avoid this we can simply add a minimal offset to the address of `ebx`, which will not affect the printing of the flag since the content of the register `ebx` is used as a pointer to the string containing the flag and the concrete flag does not appear right at the beginning of the string. In this case, we can simply add an offset of 1 byte to the content of `ebx`, which will result in the value `0x804a001`.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload of 48 bytes where the last 4 bytes are equal to `0x080487e9` and the bytes at offset 36 to 39 are equal to `0x804a001`. The payload follows the following format:
  - 36 bytes of garbage - fill the buffer and the offset to the address of `ebx` with garbage
  - 4 bytes equal to `0x804a001` - avoid the corruption of the register `ebx`
  - 4 bytes of garbage - fill the offset to the return address of the function (this interval corresponds to the addresses of the register `ebp` and can be filled with the uncorrupted value of `ebp`, `0xffffd148`, as well)
  - 4 bytes equal to `0x080487e9` - overwrite the return address of the function `check_password` with the address of the instruction that prints the flag

The script to reproduce the challenge is available at [super_secure_system.py](super_secure_system.py)
