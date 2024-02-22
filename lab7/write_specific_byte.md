# Challenge `Write Specific Byte` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Format string vulnerability_

- Where: Where is the vulnerability present
  - _`printf` function call, printing the variable `buffer` without specifying a format string_

- Impact: What results of exploiting this vulnerability
  - _Allows to overwrite variables, bypassing the check that prevents the user from obtaining the flag_

NOTE: By analyzing the source code of the vulnerable application, it is possible to notice that the `printf` function is called with the `buffer` variable as the first argument, without specifying a format string. This allows to overwrite the content of the variable `target` which is used to check if the user should be allowed to obtain the flag. Since the check is performed by checking if the most significant byte of the `target` variable is 2, it is possible to overwrite it with the byte that is needed to fit the condition.

## Steps to reproduce

1. Run the vulnerable binary

2. Obtain the address of the `target` variable

3. Send the payload to overwrite the `target` variable that should be composed by the address of the most significant byte of the `target` variable followed by `%254x%7$hhn`. Since the `printf` call will print 258 characters and one single byte can store a value up to 255, this will overwrite the most significant byte of the `target` variable with the value of 2 (258%256), allowing to obtain the flag.

The script to reproduce the challenge is available at [write_specific_byte.py](write_specific_byte.py).