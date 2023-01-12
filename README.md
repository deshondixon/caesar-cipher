# LAB 18 - Class 401d20

## Caesar Cipher

### Author: DeShon Dixon

---

## Overview

- Method encrypts a message that can then be decrypted when supplied with the corresponding key.

- Method created to decipher the encrypted message event when you do NOT have the key.

---

- Created an encrypt function that takes in a plain text phrase and a numeric shift.
the phrase is then shifted that many letters.
   - E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
shifts that exceed 26 should wrap around.
   - E.g. encrypt(‘abc’,27) would return ‘bcd’.
shifts that push a letter out or range should wrap around.
   - E.g. encrypt(‘zzz’,1) would return ‘aaa’.

- Created a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

- Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
Devise a method for the computer to determine if code was broken with minimal human guidance.

---

## Setup

- Create repo on desktop

- Create virtual environment: python3.11 -m venv .venv

- Activate environment: source .venv/bin/activate

- Install ntlk: pip install nltk

## Tests

- Encrypt a string with a given shift

- Decrypt a previously encrypted string with the same shift.

- Encryption should handle upper and lower case letters.

- Encryption should allow non-alpha characters but ignore them, including white space.

- Decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.

## Sources

- https://cryptii.com/

- https://www.nltk.org/
