"""
Artificial Immune System (AIS) - Negative Selection Algorithm
Classifies items as SELF (on the list) or NON-SELF (not on the list).
"""

import random

random.seed(42)

STRING_LENGTH = 8     # length of each binary pattern
R = 4                 # r-contiguous matching threshold
NUM_DETECTORS = 30    # number of detectors to generate


def matches(a, b, r=R):
    """True if a and b share r identical bits in a row at the same position."""
    for i in range(len(a) - r + 1):
        if a[i:i + r] == b[i:i + r]:
            return True
    return False


def random_pattern(length=STRING_LENGTH):
    return "".join(random.choice("01") for _ in range(length))


def generate_detectors(self_set, num_detectors=NUM_DETECTORS, max_tries=100000):
    """Keep a random pattern only if it matches NO item in the self set."""
    detectors = []
    tries = 0
    while len(detectors) < num_detectors and tries < max_tries:
        tries += 1
        candidate = random_pattern()
        if not any(matches(candidate, s) for s in self_set):
            detectors.append(candidate)
    return detectors


def classify(sample, detectors):
    """NON-SELF if any detector fires, else SELF."""
    if any(matches(sample, d) for d in detectors):
        return "NON-SELF (not on the list)"
    return "SELF (on the list)"


if __name__ == "__main__":
    # The "list" of allowed items
    self_set = [
        "00001111",
        "00011110",
        "00111100",
        "00001110",
        "00011111",
        "00111101",
    ]

    detectors = generate_detectors(self_set)
    print(f"Generated {len(detectors)} detectors.\n")

    tests = ["00001111", "00111100", "11110000", "10101010", "11001100"]
    for t in tests:
        print(f"{t} -> {classify(t, detectors)}")
