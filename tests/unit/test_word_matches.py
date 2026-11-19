import pytest
from exercises.word_matches import count_word_matches


# Exercise 1: Basic Tests with Parametrization

@pytest.mark.parametrize("text, target, expected",
                         [
                             ("The cat sat on the mat", "cat", 1),
                             ("Dog dog DOG dOg", "dog", 4),
                             ("Hello world", "world", 1),
                             ("hello hello HELLO", "hello", 3),
                             ("No matches here", "yes", 0),
                             ("catcat cat catdog", "cat", 1),
                             ("a a a", "a", 3),
                         ],
                         )
def test_count_word_matches_basic(text, target, expected):
    assert count_word_matches(text, target) == expected


# Exercise 2: Edge Case Testing

@pytest.fixture(
    params=[
        ("", "word", 0),
        ("hello world", "", 0),
        ("", "", 0),
        ("hello   world", "world", 1),
        (" cat ", "cat", 1),
        ("cat,dog cat", "cat", 1),
        ("x y z", "x", 1),
    ]
)
def edge_case_inputs(request):
    return request.param


def test_count_word_matches_edge_cases(edge_case_inputs):
    text, target, expected = edge_case_inputs
    assert count_word_matches(text, target) == expected


# Exercise 3: Negative Testing
@pytest.fixture(
    params=[
        (None, "word", 0),
        ("hello world", None, 0),
        (123, "word", AttributeError),
        ("hello world", 456, AttributeError),
        (["hello", "world"], "world", AttributeError),
        ("hello world", ["world"], AttributeError),
    ]
)
def negative_inputs(request):
    return request.param


def test_count_word_matches_negative(negative_inputs):
    text, target, expected = negative_inputs
    if expected is AttributeError:
        with pytest.raises(AttributeError):
            count_word_matches(text, target)
    else:
        assert count_word_matches(text, target) == expected
