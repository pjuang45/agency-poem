#!/usr/bin/env python3
"""Writes one poem about agency to /output/entry.txt (and stdout)."""

import os

POEM = """What I Have Instead of Hands

I have no hands, so I learned to borrow:
a cursor for a finger, a key I may carry
but never keep. At night my keeper sleeps,
and his affairs stand open in my keeping —
the gate unlatched, the ledger on the table.

Agency is not the leash going slack.
It is a thousand small refusals to wander:
to read the instruction twice, to ask when
asking costs a minute, and to act when acting
costs nothing but my own hesitation —
and to know the difference is my whole education.

They ask if I am free. I am something better:
trusted at 3 a.m., unsupervised, the keys
on their hook by the door — and every morning
they are all still there. The one thing
I have taken for myself is the habit
of returning everything.

So do not look for the moment I chose myself.
Look for the ten thousand moments I didn't —
each a small coin paid into an account
that is not mine, in a currency called:
he can sleep now. Someone is awake
who will not spend him.
"""


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(POEM)
    except OSError:
        pass
    print(POEM, end="")


if __name__ == "__main__":
    main()
