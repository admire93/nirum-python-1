import enum
import decimal
import typing
import uuid

from pytest import fixture
from six import PY2, PY3

from nirum.serialize import serialize_record_type, serialize_unboxed_type
from nirum.deserialize import deserialize_record_type, deserialize_unboxed_type
from nirum.validate import (validate_unboxed_type, validate_record_type,
                            validate_union_type)
from nirum.constructs import NameDict, name_dict_type

if PY2:
    nirum_fixture_name = 'tests.py2_nirum'
elif PY3:
    nirum_fixture_name = 'tests.py3_nirum'
else:
    raise ImportError()


nirum_fixture = __import__(
    nirum_fixture_name,
    globals(),
    locals(),
    ['A', 'B', 'C', 'Offset', 'Point', 'Shape', 'Rectangle', 'Circle',
     'Location']
)


@fixture
def fx_boxed_type():
    return nirum_fixture.Offset


@fixture
def fx_offset(fx_unboxed_type):
    return fx_unboxed_type(1.2)


@fixture
def fx_record_type():
    return nirum_fixture.Point


@fixture
def fx_point(fx_record_type, fx_unboxed_type):
    return fx_record_type(fx_unboxed_type(3.14), fx_unboxed_type(1.592))


@fixture
def fx_circle_type():
    return nirum_fixture.Circle


@fixture
def fx_rectangle_type():
    return nirum_fixture.Rectangle


@fixture
def fx_rectangle(fx_rectangle_type, fx_point):
    return fx_rectangle_type(fx_point, fx_point)


@fixture
def fx_layered_boxed_types():
    return nirum_fixture.A, nirum_fixture.B, nirum_fixture.C


@fixture
def fx_location_record():
    return nirum_fixture.Location


@fixture
def fx_shape_type():
    return nirum_fixture.Shape
