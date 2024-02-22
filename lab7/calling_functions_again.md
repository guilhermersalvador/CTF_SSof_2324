# Challenge `Calling Functions Again` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Format string vulnerability_

- Where: Where is the vulnerability present
  - _`printf` function call, printing the variable `buffer` without specifying a format string_

- Impact: What results of exploiting this vulnerability
  - _Allows to overwrite the address of the `puts` function in the GOT, which when called will execute a function that prints the flag_

NOTE: By analyzing the source code of the vulnerable application, it is possible to notice that the `printf` function is called with the `buffer` variable as the first argument, without specifying a format string. This allows to overwrite the address of the `puts` function in the GOT, with the address of the `win` function, which when called will print the flag.

## Steps to reproduce

1. Run the vulnerable binary

2. Obtain the address of the `puts` function in the GOT and the address of the `win` function

3. Send the payload to overwrite the address of the `puts` function, essentially following the same procedure as the one described in the [Write Big Numbers writeup](write_big_numbers.md), but instead uses the address of the `win` function as the value to be written and ends with the format string `%37390x%7$hn%30190x%8$hn`. This will overwrite the address of the `puts` function in the GOT with the address of the `win` function, which when called will print the flag.

The script to reproduce the challenge is available at [calling_functions_again.py](calling_functions_again.py)