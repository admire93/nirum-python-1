import enum
import typing
import decimal

from nirum.serialize import serialize_record_type, serialize_boxed_type
from nirum.deserialize import deserialize_record_type, deserialize_boxed_type
from nirum.validate import (validate_boxed_type, validate_record_type,
                            validate_union_type)
from nirum.constructs import NameDict, name_dict_type


class Offset:

    __nirum_boxed_type__ = float

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return (isinstance(other, Offset) and self.value == other.value)

    def __hash__(self):
        return hash(self.value)

    def __nirum_serialize__(self):
        return serialize_boxed_type(self)

    @classmethod
    def __nirum_deserialize__(cls, value):
        return deserialize_boxed_type(cls, value)

    def __hash__(self): # noqa
        return hash((self.__class__, self.value))


class Point:

    __slots__ = (
        'left',
        'top'
    )
    __nirum_record_behind_name__ = 'point'
    __nirum_field_types__ = {
        'left': Offset,
        'top': Offset
    }
    __nirum_field_names__ = NameDict([
        ('left', 'x')
    ])

    def __init__(self, left, top):
        self.left = left
        self.top = top
        validate_record_type(self)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1})'.format(
            type(self),
            ', '.join('{}={}'.format(attr, getattr(self, attr))
                      for attr in self.__slots__)
        )

    def __eq__(self, other):
        return isinstance(other, Point) and all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )

    def __nirum_serialize__(self):
        return serialize_record_type(self)

    @classmethod
    def __nirum_deserialize__(cls, values):
        return deserialize_record_type(cls, values)

    def __hash__(self):
        return hash((self.__class__, self.left, self.top))


class Shape(object):

    __nirum_union_behind_name__ = 'shape'
    __nirum_field_names__ = NameDict([
    ])

    class Tag(enum.Enum):
        rectangle = 'rectangle'
        circle = 'circle'

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "{0.__module__}.{0.__qualname__} cannot be instantiated "
            "since it is an abstract class.  Instantiate a concrete subtype "
            "of it instead.".format(
                type(self)
            )
        )

    def __nirum_serialize__(self):
        pass

    @classmethod
    def __nirum_deserialize__(cls, value):
        pass


class Rectangle(Shape):

    __slots__ = (
        'upper_left',
        'lower_right'
    )
    __nirum_tag__ = Shape.Tag.rectangle
    __nirum_tag_types__ = {
        'upper_left': Point,
        'lower_right': Point
    }
    __nirum_tag_names__ = NameDict([])

    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right
        validate_union_type(self)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1})'.format(
            type(self),
            ', '.join('{}={}'.format(attr, getattr(self, attr))
                      for attr in self.__slots__)
        )

    def __eq__(self, other):
        return isinstance(other, Rectangle) and all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )


class Circle(Shape):

    __slots__ = (
        'origin',
        'radius'
    )
    __nirum_tag__ = Shape.Tag.circle
    __nirum_tag_types__ = {
        'origin': Point,
        'radius': Offset
    }
    __nirum_tag_names__ = NameDict([])

    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius
        validate_union_type(self)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1})'.format(
            type(self),
            ', '.join('{}={}'.format(attr, getattr(self, attr))
                      for attr in self.__slots__)
        )

    def __eq__(self, other):
        return isinstance(other, Circle) and all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )


class Location:
    # TODO: docstring

    __slots__ = (
        'name',
        'lat',
        'lng',
    )
    __nirum_record_behind_name__ = 'location'
    __nirum_field_types__ = {
        'name': typing.Optional[unicode],
        'lat': decimal.Decimal,
        'lng': decimal.Decimal
    }
    __nirum_field_names__ = name_dict_type([
        ('name', 'name'),
        ('lat', 'lat'),
        ('lng', 'lng')
    ])

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng
        validate_record_type(self)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1})'.format(
            type(self),
            ', '.join('{}={}'.format(attr, getattr(self, attr))
                      for attr in self.__slots__)
        )

    def __eq__(self, other):
        return isinstance(other, Location) and all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )

    def __nirum_serialize__(self):
        return serialize_record_type(self)

    @classmethod
    def __nirum_deserialize__(cls, value):
        return deserialize_record_type(cls, value)


class A:

    __nirum_boxed_type__ = unicode

    def __init__(self, value):
        validate_boxed_type(value, unicode)
        self.value = value  # type: Text

    def __eq__(self, other):
        return (isinstance(other, A) and
                self.value == other.value)

    def __hash__(self):
        return hash(self.value)

    def __nirum_serialize__(self):
        return serialize_boxed_type(self)

    @classmethod
    def __nirum_deserialize__(cls, value):
        return deserialize_boxed_type(cls, value)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1!r})'.format(
            type(self), self.value
        )


class B:

    __nirum_boxed_type__ = A

    def __init__(self, value):
        validate_boxed_type(value, A)
        self.value = value  # type: A

    def __eq__(self, other):
        return (isinstance(other, B) and
                self.value == other.value)

    def __hash__(self):
        return hash(self.value)

    def __nirum_serialize__(self):
        return serialize_boxed_type(self)

    @classmethod
    def __nirum_deserialize__(cls, value):
        return deserialize_boxed_type(cls, value)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1!r})'.format(
            type(self), self.value
        )


class C:

    __nirum_boxed_type__ = B

    def __init__(self, value):
        validate_boxed_type(value, B)
        self.value = value  # type: B

    def __eq__(self, other):
        return (isinstance(other, C) and
                self.value == other.value)

    def __hash__(self):
        return hash(self.value)

    def __nirum_serialize__(self):
        return serialize_boxed_type(self)

    @classmethod
    def __nirum_deserialize__(cls, value):
        return deserialize_boxed_type(cls, value)

    def __repr__(self):
        return '{0.__module__}.{0.__qualname__}({1!r})'.format(
            type(self), self.value
        )

