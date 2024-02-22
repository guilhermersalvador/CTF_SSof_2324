# Challenge `Write Big Numbers` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Format string vulnerability_

- Where: Where is the vulnerability present
  - _`printf` function call, printing the variable `buffer` without specifying a format string_

- Impact: What results of exploiting this vulnerability
  - _Allows to overwrite the content of the stack, bypassing the check that prevents the user from obtaining the flag_

NOTE: By analyzing the source code of the vulnerable application, it is possible to notice that the `printf` function is called with the `buffer` variable as the first argument, without specifying a format string. This allows to overwrite the content of the variable `target` which is used to check if the user should be allowed to obtain the flag. Since the check is performed by checking if the `target` variable is equal to `0xdeadbeef`, it is possible to overwrite it with the exact value, bypassing the check and obtaining the flag.

## Steps to reproduce

1. Run the vulnerable binary

2. Obtain the address of the `target` variable

3. Send the payload to overwrite the `target` variable that should be composed by the address of the `target` variable followed by the address of the 3rd less significant byte of the `target` variable and by the format string `%48871x%7$hn%8126x%8$hn`. This will overwrite both the less significant half of the `target` variable with the value of `0xbeef` and the most significant half of the `target` variable with the value of `0xdead`, allowing to obtain the flag. Note that the padding values were calculated taking into account the number of characters printed by the `printf` function at each point of the format string, in order to overwrite the correct bytes of the `target` variable.

The script to reproduce the challenge is available at [write_big_numbers.py](write_big_numbers.py).