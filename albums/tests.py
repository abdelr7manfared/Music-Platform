from django.test import TestCase

# Create your tests here.
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5