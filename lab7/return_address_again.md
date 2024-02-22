# Challenge `Return Address Again` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Format string vulnerability_
- Where: Where is the vulnerability present
  - _`printf` function call, printing the variable `buffer` without specifying a format string_
- Impact: What results of exploiting this vulnerability
  - _Allows to overwrite the return address of the `vuln` function, redirecting the execution flow to a function that prints the flag_

NOTE: By analyzing the source code of the vulnerable application, it is possible to notice that the `printf` function is called with the `buffer` variable as the first argument, without specifying a format string. This allows to overwrite the return address of the `vuln` function, redirecting the execution flow to the `win` function, which when called will print the flag. By analyzing the binary with `gdb`, it is also possible to notice that the return address of the `vuln` function is located at an offset of 144 bytes from the top of the stack at the moment of the `printf` function call. To get the address where the return address of the `vuln` function is located at the target machine, it is possible to leak it, by leaking the first address of the stack by using the format string vulnerability and afterward overwrite it with the address of the `win` function.

## Steps to reproduce

1. Run the vulnerable binary

2. Obtain the address of the `win` function

3. Send the payload `%08x` to leak the first address of the stack at the moment of the `printf` function call and obtain the address of the return address of the `vuln` function by adding 144 to the leaked address.

4. Rerun the vulnerable binary

5. Send the payload to overwrite the return address of the `vuln` function with the address of the `win` function. To do so, it is possible to use the same procedure as the one described in the [Write Big Numbers writeup](write_big_numbers.md), but using the address of the return address of the `vuln` function as target, and the address of the `win` function as the value to be written. This time, the payload must end with the format string `%37358x%7$hn%30222x%8$hn`. This will overwrite the return address of the `vuln` function with the address of the `win` function, redirecting the execution flow to the `win` function, which when called will print the flag.

The script to reproduce the challenge is available at [return_address_again.py](return_address_again.py)