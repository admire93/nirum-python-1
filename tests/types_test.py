import collections

from pytest import raises

from nirum.types import ImmutableList


def test_immutable_list():
    immutable_list = ImmutableList([1, 2])
    with raises(AttributeError):
        immutable_list.append(1)

    with raises(TypeError):
        immutable_list + [3]

    assert isinstance(immutable_list, collections.Sequence)
    assert immutable_list[0] == 1
    assert len(immutable_list) == 2
    assert 2 in immutable_list
    assert next(iter(immutable_list)) == 1
    assert immutable_list.index(2) == 1
    assert immutable_list.count(1) == 1
    assert immutable_list.count(2) == 1
    assert immutable_list.count(3) == 0
