# Challenge `Pickles in a serialous race` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Race condition (Time of check to time of use) / Remote code execution_
- Where: Where is the vulnerability present
  - _Option to read a note in `CLASSY` mode (executing `pickle.loads`) and mode checker `check_mode`_
- Impact: What results of exploiting this vulnerability
  - _Allows execute arbitrary commands in the target machine by sending data, previously serialized using pickle_

NOTE: The server provides 2 modes to manage notes, `CLASSY` and `FREE`. The `CLASSY` mode uses the Python `pickle` module to serialize and deserialize the notes, while the `FREE` mode uses raw content. The server has also a protection mechanism that prevents notes from being shared between modes (i.e. notes created in `CLASSY` mode cannot be read in `FREE` mode and vice-versa). To provide this separation the server deletes all user notes when the mode is changed. However, mode checking is only performed when selecting the desired mode, not when reading a note or writing it. Moreover, according to the module docs, the Python `pickle` module is vulnerable to remote code execution when deserializing untrusted data, which opens the possibility of performing arbitrary code execution in the target machine.

## Steps to reproduce

1. Establish 2 parallel socket connections with the server, one for each mode.

2. Select `CLASSY` mode in one of the connections and `FREE` mode in the other, to pass the mode checker verification and avoid future note deletions.

3. In the `FREE` mode session, write a tampered note, containing a malicious payload to be executed in the target machine. The malicious payload is a serialized Python object (instance of the `RCE` class, defined in the provided script and serialized using `pickle.dumps`) that will execute an arbitrary command in the target machine when deserialized using `pickle.loads`. Since the vulnerability allows arbitrary command execution, the payload can contain any command but after digging in the target machine, the flag was found in `/home/ctf/flag`. To perform the flag extraction the command to use is `cat /home/ctf/flag`.

4. In the `CLASSY` mode session, read the note created in step 3, which will deserialize the malicious payload and execute the arbitrary command in the target machine, returning the output of the command execution, and, consequently, the desired flag.

The script to reproduce the challenge is available at [pickles_in_a_serialous_race.py](pickles_in_a_serialous_race.py)
