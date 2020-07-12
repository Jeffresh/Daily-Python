# You and Fredrick are good friends. Yesterday, Fredrick received N
# credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not.
# You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
# ► It must start with a 4, 5, or 6
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.

import re


def validate_credit_cards(credit_card):
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    if all(re.match(f, credit_card) for f in filters):
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':

    for _ in range(int(input())):
        validate_credit_cards(input())
