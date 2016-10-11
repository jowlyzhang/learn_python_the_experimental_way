"""A study note for the hard learnt OR operator in re module.
Donts:
    1. No space before or after '|', which is gonna be taken as what's to be matched.

Do:
    1. Include multiple patterns in parenthesis.

Example:
    re.match(r'A03\.(CT[01]|MASTER), out)
matches:
    A03.CT0, A03.CT1, A03.MASTER
"""
