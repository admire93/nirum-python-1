from pytest import raises

from nirum.func import import_string


def test_import_string():
    assert import_string('builtins:int') == int
    assert import_string('builtins:int(1)') == 1
    with raises(ValueError):
        # malformed
        import_string('world')
    with raises(ValueError):
        # coudn't import
        import_string('builtins:world')
    with raises(ValueError):
        # coudn't import
        import_string('os.hello:world')
