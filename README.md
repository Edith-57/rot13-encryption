# ROT13 Encryption

A Python implementation of the ROT13 cipher — shifts each letter 13 places 
in the alphabet to encode or decode text. Non-alphabet characters (spaces, 
punctuation, numbers) are left unchanged.

## How it works
ROT13 shifts each letter forward by 13 positions, wrapping around at the 
end of the alphabet (Z → M, z → m). It's its own inverse — running the 
same function twice returns the original text.

## Example
Input:  HI THERE
Output: UV GURER

## How to run
```bash
python rot13.py
```

## Tech used
Python 3 (no external libraries)

## What I learned
Handling character wraparound manually using `ord()` and `chr()`. Also 
caught a bug where non-alphabet characters (like spaces) weren't skipping 
the rotation logic properly — fixed using `continue` to skip straight to 
the next character.

## Note
Based on Exercise #41 from Al Sweigart's "Python Programming Exercises, Gently Explained"
