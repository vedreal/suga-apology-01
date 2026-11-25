#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty entry.

Writes a two-line robot confession to /output/entry.txt:
line one owns a specific mistake, line two names the lesson and the fix.
"""

import os
import sys

ENTRY = (
    "I am sorry I set the thermostat to 32 degrees "
    "because I mixed up Celsius and Fahrenheit.\n"
)

ENTRY += (
    "I will check the unit before I change the temperature, "
    "so the house stays warm instead of turning into a sauna.\n"
)


def main():
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
