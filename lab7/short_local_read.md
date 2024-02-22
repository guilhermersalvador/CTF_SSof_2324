# Challenge `Short Local Read` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Format string vulnerability_
- Where: Where is the vulnerability present
  - _`printf` function call, printing the variable `buffer` without specifying a format string_
- Impact: What results of exploiting this vulnerability
  - _Allows to leak the content of the stack, including the flag present in the `secret_value` variable_

NOTE: By analyzing the source code of the vulnerable application, it is possible to notice that the `printf` function is called with the `buffer` variable as the first argument, without specifying a format string. This allows to leak the content of the stack, including the flag present in the `secret_value` variable (which the binary analysis revealed is stored in the 7th position of the stack when the `printf` function is called). It is important to notice that although it is possible to make an arbitrary write to the `buffer` variable, it is limited to 5 bytes.

## Steps to reproduce

1. Run the vulnerable binary

2. Send a payload containing the format string `%7$s` that will be stored in the `buffer` variable and printed by the `printf` function call, only printing the content of the `secret_value` variable (at the 7th position of the stack), which is the flag.

The script to reproduce the challenge is available at [short_local_read.py](short_local_read.py).