import pytest


def max_alternating_subsequence(X: list[int]) -> int:
    # Initialize variables to track the longest subsequence ending with 0 or 1
    end_with_0 = 0  # Length of the longest subsequence ending with 0
    end_with_1 = 0  # Length of the longest subsequence ending with 1

    # Iterate through the array
    for num in X:
        if num == 0:
            # If the current element is 0, it can extend subsequences ending with 1
            end_with_0 = end_with_1 + 1
        else:
            # If the current element is 1, it can extend subsequences ending with 0
            end_with_1 = end_with_0 + 1

    # The result is the maximum of the two
    return max(end_with_0, end_with_1)


@pytest.mark.parametrize(
    ("X", "expected"),
    (
        ([0, 1, 0, 1, 0], 5),
        ([0], 1),
        ([0, 1, 0, 1, 0, 1, 0, 1, 0], 9),
        ([0, 1, 0, 1, 1, 0, 1, 0, 0], 7),
    ),
)
def test_max_alternating_subsequence(
    X: list[int],
    expected: int,
) -> None:
    assert expected == max_alternating_subsequence(X)
