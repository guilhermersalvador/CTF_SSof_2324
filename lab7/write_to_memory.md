# Challenge `Write to Memory` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Format string vulnerability_

- Where: Where is the vulnerability present
  - _`printf` function call, printing the variable `buffer` without specifying a format string_

- Impact: What results of exploiting this vulnerability
  - _Allows to overwrite variables, bypassing the check that prevents the user from obtaining the flag_

NOTE: By analyzing the source code of the vulnerable application, it is possible to notice that the `printf` function is called with the `buffer` variable as the first argument, without specifying a format string. This allows to overwrite the content of the variable `target` which is used to check if the user should be allowed to obtain the flag. Since the check is performed by checking if the `target` variable is 0, it is possible to overwrite it with any value different from 0, bypassing the check and obtaining the flag.

## Steps to reproduce

1. Run the vulnerable binary

2. Obtain the address of the `target` variable

3. Send the payload to overwrite the `target` variable that should be composed by the address of the `target` variable followed by `%08x%08x%08x%08x%08x%08x%n`. This will overwrite the `target` variable with the number of characters printed by the `printf`, which is different from 0, allowing to obtain the flag.

The script to reproduce the challenge is available at [write_to_memory.py](write_to_memory.py).