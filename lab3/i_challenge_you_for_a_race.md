# Challenge `I challenge you for a race` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Race condition (Time of check to time of use)_

- Where: Where is the vulnerability present
  - `challenge/challenge` script, more specifically in the `access` and `fopen` calls

- Impact: What results of exploiting this vulnerability
  - _Allows to access the flag file without having the proper permissions_

NOTE: The script available at `challenge/challenge` runs `setuid` root and verifies the user permissions before opening the files provided as input. However, between the permission verification and the actual opening of the file, there is a time window that can be used to access files with root privileges.

## Steps to reproduce

1. Create an arbitrary file as a regular user
2. Create a symbolic link to the file created in step 1
3. Run the `challenge/challenge` script as a regular user and provide the symbolic link created in step 2 as input. In parallel, recreate the symbolic link created in step 2 to point to the flag file `/challenge/flag`
4. Repeat steps 2 and 3 until the symbolic link recreation hits the desired time window (i.e. between the permission verification and the actual opening of the file). Since the permission verification using `access` verifies the real UID and the file opening using `fopen` verifies the effective UID, this process will open the flag file `/challenge/flag` as root (effective UID).

The script to reproduce the challenge is available at [i_challenge_you_for_a_race.sh](i_challenge_you_for_a_race.sh)