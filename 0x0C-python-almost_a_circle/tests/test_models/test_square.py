#!/usr/bin/python3
# test_square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
	"""Unittests for testing instantiation of the Square class."""

	def test_is_base(self):
		self.assertIsInstance(Square(10), Base)

	def test_is_rectangle(self):
		self.assertIsInstance(Square(10), Square)

	def test_no_args(self):
		with self.assertRaises(TypeError):
			Square()

	def test_one_arg(self):
		s1 = Square(10)
		s2 = Square(11)
		self.assertEqual(s1.id, s2.id - 1)

	def test_two_args(self):
		s1 = Square(10, 2)
		s2 = Square(2, 10)
		self.assertEqual(s1.id, s2.id - 1)

	def test_three_args(self):
		s1 = Square(10, 2, 2)
		s2 = Square(2, 2, 10)
		self.assertEqual(s1.id, s2.id - 1)

	def test_four_args(self):
		self.assertEqual(7, Square(10, 2, 2, 7).id)

	def test_more_than_four_args(self):
		with self.assertRaises(TypeError):
			Square(1, 2, 3, 4, 5)

	def test_size_private(self):
		with self.assertRaises(AttributeError):
			print(Square(10, 2, 3, 4).__size)

	def test_size_getter(self):
		self.assertEqual(5, Square(5, 2, 3, 9).size)

	def test_size_setter(self):
		s = Square(4, 1, 9, 2)
		s.size = 8
		self.assertEqual(8, s.size)

	def test_width_getter(self):
		s = Square(4, 1, 9, 2)
		s.size = 8
		self.assertEqual(8, s.width)

	def test_height_getter(self):
		s = Square(4, 1, 9, 2)
		s.size = 8
		self.assertEqual(8, s.height)

	def test_x_getter(self):
		self.assertEqual(0, Square(10).x)

	def test_y_getter(self):
		self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
	"""Unittests for testing size initialization of the Square class."""

	def test_None_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(None)

	def test_str_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square("invalid")

	def test_float_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(5.5)

	def test_complex_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(complex(5))

	def test_dict_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square({"a": 1, "b": 2}, 2)

	def test_bool_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(True, 2, 3)

	def test_list_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square([1, 2, 3])

	def test_set_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square({1, 2, 3}, 2)

	def test_tuple_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square((1, 2, 3), 2, 3)

	def test_frozenset_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(frozenset({1, 2, 3, 1}))

	def test_range_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(range(5))

	def test_bytes_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(b'Python')

	def test_bytearray_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(bytearray(b'abcdefg'))

	def test_memoryview_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square

(memoryview(b'abcdefg'))

	def test_inf_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(float('inf'))

	def test_nan_size(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square(float('nan'))

	# Test size values
	def test_negative_size(self):
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			Square(-1, 2)

	def test_zero_size(self):
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			Square(0, 2)


class TestSquare_x(unittest.TestCase):
	"""Unittests for testing initialization of Square x attribute."""

	def test_None_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, None)

	def test_str_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, "invalid")

	def test_float_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, 5.5)

	def test_complex_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, complex(5))

	def test_dict_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, {"a": 1, "b": 2}, 2)

	def test_bool_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, True)

	def test_list_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, [1, 2, 3])

	def test_set_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, {1, 2, 3})

	def test_tuple_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, (1, 2, 3))

	def test_frozenset_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, frozenset({1, 2, 3, 1}))

	def test_range_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, range(5))

	def test_bytes_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, b'Python')

	def test_bytearray_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, bytearray(b'abcdefg'))

	def test_memoryview_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, memoryview(b'abcedfg'))

	def test_inf_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, float('inf'), 2)

	def test_nan_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, float('nan'), 2)

	def test_negative_x(self):
		with self.assertRaisesRegex(ValueError, "x must be >= 0"):
			Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
	"""Unittests for testing initialization of Square y attribute."""

	def test_None_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, None)

	def test_str_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, "invalid")

	def test_float_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, 5.5)

	def test_complex_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, complex(5))

	def test_dict_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, {"a": 1, "b": 2})

	def test_list_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, [1, 2, 3])

	def test_set_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, {1, 2, 3})

	def test_tuple_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, (1, 2, 3))

	def test_frozenset_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, frozenset({1, 2, 3, 1}))

	def test_range_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, range(5))

	def test_bytes_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, b'Python')

	def test_bytearray_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 3, bytearray(b'abcdefg'))

	def test_memoryview_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			S

quare(1, 3, memoryview(b'abcedfg'))

	def test_inf_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, float('inf'))

	def test_nan_y(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Square(1, 1, float('nan'))

	def test_negative_y(self):
		with self.assertRaisesRegex(ValueError, "y must be >= 0"):
			Square(3, 0, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
	"""Unittests for testing order of Square attribute initialization."""

	def test_size_before_x(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square("invalid size", "invalid x")

	def test_size_before_y(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Square("invalid size", 1, "invalid y")

	def test_x_before_y(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
	"""Unittests for testing the area method of the Square class."""

	def test_area_small(self):
		self.assertEqual(100, Square(10, 0, 0, 1).area())

	def test_area_large(self):
		s = Square(999999999999999999, 0, 0, 1)
		self.assertEqual(999999999999999998000000000000000001, s.area())

	def test_area_changed_attributes(self):
		s = Square(2, 0, 0, 1)
		s.size = 7
		self.assertEqual(49, s.area())

	def test_area_one_arg(self):
		s = Square(2, 10, 1, 1)
		with self.assertRaises(TypeError):
			s.area(1)


class TestSquare_stdout(unittest.TestCase):
	"""Unittests for testing __str__ and display methods of Square class."""

	@staticmethod
	def capture_stdout(sq, method):
		"""Captures and returns text printed to stdout.

		Args:
			sq (Square): The Square ot print to stdout.
			method (str): The method to run on sq.
		Returns:
			The text printed to stdout by calling method on sq.
		"""
		capture = io.StringIO()
		sys.stdout = capture
		if method == "print":
			print(sq)
		else:
			sq.display()
		sys.stdout = sys.__stdout__
		return capture

	def test_str_method_print_size(self):
		s = Square(4)
		capture = TestSquare_stdout.capture_stdout(s, "print")
		correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
		self.assertEqual(correct, capture.getvalue())

	def test_str_method_size_x(self):
		s = Square(5, 5)
		correct = "[Square] ({}) 5/0 - 5".format(s.id)
		self.assertEqual(correct, s.__str__())

	def test_str_method_size_x_y(self):
		s = Square(7, 4, 22)
		correct = "[Square] ({}) 4/22 - 7".format(s.id)
		self.assertEqual(correct, str(s))

	def test_str_method_size_x_y_id(self):
		s = Square(2, 88, 4, 19)
		self.assertEqual("[Square] (19) 88/4 - 2", str(s))

	def test_str_method_changed_attributes(self):
		s = Square(7, 0, 0, [4])
		s.size = 15
		s.x = 8
		s.y = 10
		self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

	def test_str_method_one_arg(self):
		s = Square(1, 2, 3, 4)
		with self.assertRaises(TypeError):
			s.__str__(1)

	# Test display method
	def test_display_size(self):
		s = Square(2, 0, 0, 9)
		capture = TestSquare_stdout.capture_stdout(s, "display")
		self.assertEqual("##\n##\n", capture.getvalue())

	def test_display_size_x(self):
		s = Square(3, 1, 0, 18)
		capture = TestSquare_stdout.capture_stdout(s, "display")
		self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

	def test_display_size_y(self):
		s = Square(4, 0, 1, 9)
		capture = TestSquare_stdout.capture_stdout(s, "display")
		display = "\n####\n####\n####\n####\n"
		self.assertEqual(display, capture.getvalue())

	def test_display_size_x_y(self):
		s = Square(2, 3, 2, 1)
		capture = TestSquare_stdout.capture_stdout(s, "display")
		display = "\n\n   ##\n   ##\n"
		self.assertEqual(display, capture.getvalue())

	def test_display_one_arg(self):
		s = Square(3

, 1, 0, 1)
		with self.assertRaises(TypeError):
			s.display(1)


class TestSquare_update_args(unittest.TestCase):
	"""Unittests for testing the update method with *args in Square class."""

	# Test changing size attribute
	def test_size_args(self):
		s = Square(4, 0, 0, 1)
		s.update(5)
		self.assertEqual(5, s.size)

	def test_size_args_and_x(self):
		s = Square(4, 0, 0, 1)
		s.update(7, 10)
		self.assertEqual(7, s.size)
		self.assertEqual(10, s.x)

	def test_size_args_x_and_y(self):
		s = Square(3, 2, 1, 3)
		s.update(8, 10, 2)
		self.assertEqual(8, s.size)
		self.assertEqual(10, s.x)
		self.assertEqual(2, s.y)

	def test_size_args_x_y_and_id(self):
		s = Square(4, 2, 3, 9)
		s.update(2, 4, 1, 6)
		self.assertEqual(2, s.size)
		self.assertEqual(4, s.x)
		self.assertEqual(1, s.y)
		self.assertEqual(6, s.id)

	def test_size_args_x_y_id_and_other_arg(self):
		s = Square(1, 0, 5, 4)
		s.update(9, 4, 8, 12, [4])
		self.assertEqual(9, s.size)
		self.assertEqual(4, s.x)
		self.assertEqual(8, s.y)
		self.assertEqual(12, s.id)
		self.assertEqual([4], s.__str__())

	def test_size_args_with_None(self):
		s = Square(3, 2, 1, 7)
		s.update(8, None)
		self.assertEqual(8, s.size)
		self.assertEqual(2, s.x)

	def test_size_args_with_str(self):
		s = Square(4, 0, 0, 7)
		s.update("invalid")
		self.assertEqual(4, s.size)

	def test_size_args_with_float(self):
		s = Square(5, 1, 2, 3)
		s.update(10.5)
		self.assertEqual(5, s.size)

	def test_size_args_with_complex(self):
		s = Square(2, 0, 0, 1)
		s.update(complex(5))
		self.assertEqual(2, s.size)

	def test_size_args_with_dict(self):
		s = Square(1, 1, 2, 3)
		s.update({"a": 1, "b": 2})
		self.assertEqual(1, s.size)

	def test_size_args_with_bool(self):
		s = Square(2, 2, 1, 4)
		s.update(True)
		self.assertEqual(2, s.size)

	def test_size_args_with_list(self):
		s = Square(3, 0, 2, 9)
		s.update([1, 2, 3])
		self.assertEqual(3, s.size)

	def test_size_args_with_set(self):
		s = Square(5, 3, 0, 8)
		s.update({1, 2, 3})
		self.assertEqual(5, s.size)

	def test_size_args_with_tuple(self):
		s = Square(4, 0, 0, 2)
		s.update((1, 2, 3))
		self.assertEqual(4, s.size)

	def test_size_args_with_frozenset(self):
		s = Square(5, 1, 3, 2)
		s.update(frozenset({1, 2, 3, 1}))
		self.assertEqual(5, s.size)

	def test_size_args_with_range(self):
		s = Square(4, 0, 2, 5)
		s.update(range(5))
		self.assertEqual(4, s.size)

	def test_size_args_with_bytes(self):
		s = Square(2, 0, 0, 3)
		s.update(b'Python')
		self.assertEqual(2, s.size)

	def test_size_args_with_bytearray(self):
		s = Square(3, 2, 1, 7)
		s.update(bytearray(b'abcdefg'))
		self.assertEqual(3, s.size)

	def test_size_args_with_memoryview(self):
		s = Square(4, 3, 2, 5)
		s.update(memoryview(b'abcdefg'))
		self.assertEqual(4, s.size)

	def test_size_args_with_inf(self):
		s = Square(5, 0, 0, 6)
		s.update(float('inf'))
		self.assertEqual(5, s.size)

	def test_size_args_with_nan(self):
		s = Square(2, 0, 2, 9)
		s.update(float('nan'))
		self.assertEqual(2, s.size)

	def test_size_args_negative(self):
		s = Square(4, 0, 0, 7)
		s.update(-1)
		self.assertEqual(4, s.size)

	def test_size_args_zero(self):
		s = Square(3, 0, 0, 8)
		s.update(0)
		self.assertEqual(3, s.size)


class TestSquare_update_kwargs(unittest.TestCase):
	"""Unittests for testing the update method with **kwargs in Square class."""

	def test_size_kwargs(self):
		s = Square(4, 0, 0, 1)
		s.update(size=5)
		self.assertEqual(5, s.size)

	def test_size_kwargs_and_x(self):
		s = Square(4, 0, 0, 1)
		s.update(size=7, x=10)
		self.assertEqual(7, s.size)
		self.assertEqual(10, s.x)

	def test_size_kwargs_x_and_y(self):
		s = Square(3, 2, 1, 3)
		s.update(size=8, x=10, y=2)
		self.assertEqual(8, s.size)
		self.assertEqual(10, s.x)
		self.assertEqual(2, s.y)

	def test_size_kwargs_x_y_and_id(self):
		s = Square(4, 2, 3, 9)
		s.update(size=2, x=4, y=1, id=6)
		self.assertEqual(2, s.size)
		self.assertEqual(4, s.x)
		self.assertEqual(1, s.y)
		self.assertEqual(6, s.id)

	def test_size_kwargs_x_y_id_and_other_arg(self):
		s = Square(1, 0, 5, 4)
		s.update(size=9, x=4, y=8, id=12, other_arg=[4])
		self.assertEqual(9, s.size)
		self.assertEqual(4, s.x)
		self.assertEqual(8, s.y)
		self.assertEqual(12, s.id)
		self.assertEqual([4], s.__str__())

	def test_size_kwargs_with_None(self):
		s = Square(3, 2, 1, 7)
		s

.update(size=8, x=None)
		self.assertEqual(8, s.size)
		self.assertEqual(2, s.x)

	def test_size_kwargs_with_str(self):
		s = Square(4, 0, 0, 7)
		s.update(size="invalid")
		self.assertEqual(4, s.size)

	def test_size_kwargs_with_float(self):
		s = Square(5, 1, 2, 3)
		s.update(size=10.5)
		self.assertEqual(5, s.size)

	def test_size_kwargs_with_complex(self):
		s = Square(2, 0, 0, 1)
		s.update(size=complex(5))
		self.assertEqual(2, s.size)

	def test_size_kwargs_with_dict(self):
		s = Square(1, 1, 2, 3)
		s.update(size={"a": 1, "b": 2})
		self.assertEqual(1, s.size)

	def test_size_kwargs_with_bool(self):
		s = Square(2, 2, 1, 4)
		s.update(size=True)
		self.assertEqual(2, s.size)

	def test_size_kwargs_with_list(self):
		s = Square(3, 0, 2, 9)
		s.update(size=[1, 2, 3])
		self.assertEqual(3, s.size)

	def test_size_kwargs_with_set(self):
		s = Square(5, 3, 0, 8)
		s.update(size={1, 2, 3})
		self.assertEqual(5, s.size)

	def test_size_kwargs_with_tuple(self):
		s = Square(4, 0, 0, 2)
		s.update(size=(1, 2, 3))
		self.assertEqual(4, s.size)

	def test_size_kwargs_with_frozenset(self):
		s = Square(5, 1, 3, 2)
		s.update(size=frozenset({1, 2, 3, 1}))
		self.assertEqual(5, s.size)

	def test_size_kwargs_with_range(self):
		s = Square(4, 0, 2, 5)
		s.update(size=range(5))
		self.assertEqual(4, s.size)

	def test_size_kwargs_with_bytes(self):
		s = Square(2, 0, 0, 3)
		s.update(size=b'Python')
		self.assertEqual(2, s.size)

	def test_size_kwargs_with_bytearray(self):
		s = Square(3, 2, 1, 7)
		s.update(size=bytearray(b'abcdefg'))
		self.assertEqual(3, s.size)

	def test_size_kwargs_with_memoryview(self):
		s = Square(4, 3, 2, 5)
		s.update(size=memoryview(b'abcdefg'))
		self.assertEqual(4, s.size)

	def test_size_kwargs_with_inf(self):
		s = Square(5, 0, 0, 6)
		s.update(size=float('inf'))
		self.assertEqual(5, s.size)

	def test_size_kwargs_with_nan(self):
		s = Square(2, 0, 2, 9)
		s.update(size=float('nan'))
		self.assertEqual(2, s.size)

	def test_size_kwargs_negative(self):
		s = Square(4, 0, 0, 7)
		s.update(size=-1)
		self.assertEqual(4, s.size)

	def test_size_kwargs_zero(self):
		s = Square(3, 0, 0, 8)
		s.update(size=0)
		self.assertEqual(3, s.size)


class TestSquare_update_no_args_kwargs(unittest.TestCase):
	"""Unittests for testing the update method with no *args and **kwargs in Square class."""

	def test_no_args_kwargs(self):
		s = Square(4, 0, 0, 1)
		s.update()
		self.assertEqual(4, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(1, s.id)

	def test_no_args_with_size_kwargs(self):
		s = Square(4, 0, 0, 1)
		s.update(size=8)
		self.assertEqual(8, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(1, s.id)

	def test_no_args_with_x_and_id_kwargs(self):
		s = Square(4, 0, 0, 1)
		s.update(x=5, id=10)
		self.assertEqual(4, s.size)
		self.assertEqual(5, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(10, s.id)

	def test_no_args_with_y_kwargs(self):
		s = Square(3, 2, 1, 9)
		s.update(y=5)
		self.assertEqual(3, s.size)
		self.assertEqual(2, s.x)
		self.assertEqual(5, s.y)
		self.assertEqual(9, s.id)

	def test_no_args_with_invalid_kwargs(self):
		s = Square(2, 0, 0, 4)
		s.update(invalid_arg=10)
		self.assertEqual(2, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(4, s.id)

	def test_no_args_with_None_kwargs(self):
		s = Square(3, 2, 1, 7)
		s.update(x=None, y=None)
		self.assertEqual(3, s.size)
		self.assertEqual(2, s.x)
		self.assertEqual(1, s.y)
		self.assertEqual(7, s.id)

	def test_no_args_with_str_kwargs(self):
		s = Square(4, 0, 0, 7)
		s.update(size="invalid", x="string", y="another")
		self.assertEqual(4, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(7, s.id)

	def test_no_args_with_float_kwargs(self):
		s = Square(5, 1, 2, 3)
		s.update(size=10.5, x=1.5, y=2.5, id=3.5)
		self.assertEqual(5, s.size)
		self.assertEqual(1, s.x)
		self.assertEqual(2, s.y)
		self.assertEqual(3, s.id)

	def test_no_args_with_complex_kwargs(self):
		s = Square(2, 0, 0, 1)
		s.update(size=complex(5), x=complex(2), y=complex(3), id=complex(1))
		self.assertEqual(2, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(1, s.id)

	def test_no_args_with_dict_kwargs(self):
		s = Square(1, 1, 2, 3)
		s.update(size={"a": 1, "b": 2}, x={"c": 3}, y={"d": 4}, id={"e": 5})
		self.assertEqual(1, s.size)
		self

.assertEqual(1, s.x)
		self.assertEqual(2, s.y)
		self.assertEqual(3, s.id)

	def test_no_args_with_bool_kwargs(self):
		s = Square(2, 2, 1, 4)
		s.update(size=True, x=False, y=True, id=False)
		self.assertEqual(2, s.size)
		self.assertEqual(2, s.x)
		self.assertEqual(1, s.y)
		self.assertEqual(4, s.id)

	def test_no_args_with_list_kwargs(self):
		s = Square(3, 0, 2, 9)
		s.update(size=[1, 2, 3], x=[4, 5], y=[6, 7, 8], id=[9, 10, 11, 12])
		self.assertEqual(3, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(2, s.y)
		self.assertEqual(9, s.id)

	def test_no_args_with_set_kwargs(self):
		s = Square(5, 3, 0, 8)
		s.update(size={1, 2, 3}, x={4, 5}, y={6, 7, 8}, id={9, 10, 11, 12})
		self.assertEqual(5, s.size)
		self.assertEqual(3, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(8, s.id)

	def test_no_args_with_tuple_kwargs(self):
		s = Square(4, 0, 0, 2)
		s.update(size=(1, 2, 3), x=(4, 5), y=(6, 7, 8), id=(9, 10, 11, 12))
		self.assertEqual(4, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(2, s.id)

	def test_no_args_with_frozenset_kwargs(self):
		s = Square(5, 1, 3, 2)
		s.update(size=frozenset({1, 2, 3, 1}), x=frozenset({4, 5}),
				 y=frozenset({6, 7, 8}), id=frozenset({9, 10, 11, 12}))
		self.assertEqual(5, s.size)
		self.assertEqual(1, s.x)
		self.assertEqual(3, s.y)
		self.assertEqual(2, s.id)

	def test_no_args_with_range_kwargs(self):
		s = Square(4, 0, 2, 5)
		s.update(size=range(5), x=range(10), y=range(3), id=range(8))
		self.assertEqual(4, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(2, s.y)
		self.assertEqual(5, s.id)

	def test_no_args_with_bytes_kwargs(self):
		s = Square(2, 0, 0, 3)
		s.update(size=b'Python', x=b'Programming', y=b'Language', id=b'2022')
		self.assertEqual(2, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(3, s.id)

	def test_no_args_with_bytearray_kwargs(self):
		s = Square(3, 2, 1, 7)
		s.update(size=bytearray(b'abcdefg'), x=bytearray(b'123456'),
				 y=bytearray(b'!@#$%^&*()'), id=bytearray(b'9876543210'))
		self.assertEqual(3, s.size)
		self.assertEqual(2, s.x)
		self.assertEqual(1, s.y)
		self.assertEqual(7, s.id)

	def test_no_args_with_memoryview_kwargs(self):
		s = Square(4, 3, 2, 5)
		s.update(size=memoryview(b'abcdefg'), x=memoryview(b'123456'),
				 y=memoryview(b'!@#$%^&*()'), id=memoryview(b'9876543210'))
		self.assertEqual(4, s.size)
		self.assertEqual(3, s.x)
		self.assertEqual(2, s.y)
		self.assertEqual(5, s.id)

	def test_no_args_with_inf_kwargs(self):
		s = Square(5, 0, 0, 6)
		s.update(size=float('inf'), x=float('inf'), y=float('inf'), id=float('inf'))
		self.assertEqual(5, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(float('inf'), s.id)

	def test_no_args_with_nan_kwargs(self):
		s = Square(2, 0, 2, 9)
		s.update(size=float('nan'), x=float('nan'), y=float('nan'), id=float('nan'))
		self.assertEqual(2, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(2, s.y)
		self.assertEqual(float('nan'), s.id)

	def test_no_args_negative_kwargs(self):
		s = Square(4, 0, 0, 7)
		s.update(size=-1, x=-5, y=-3, id=-6)
		self.assertEqual(4, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(7, s.id)

	def test_no_args_zero_kwargs(self):
		s = Square(3, 0, 0, 8)
		s.update(size=0, x=0, y=0, id=0)
		self.assertEqual(3, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(8, s.id)


class TestSquare_update_no_args_no_kwargs(unittest.TestCase):
	"""Unittests for testing the update method with no *args and no **kwargs in Square class."""

	def test_no_args_no_kwargs(self):
		s = Square(4, 0, 0, 1)
		s.update()
		self.assertEqual(4, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(1, s.id)

	def test_no_args_no_kwargs_changed_attributes(self):
		s = Square(2, 0, 0, 1)
		s.size = 5
		s.x = 2
		s.y = 3
		s.id = 4
		s.update()
		self.assertEqual(2, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(1, s.id)

	def test_no_args_no_kwargs_set_attributes(self):
		s = Square(3, 2, 1, 9)
		s.update()
		self.assertEqual(3, s.size)
		self.assertEqual(0, s.x)
		self.assertEqual(0, s.y)
		self.assertEqual(9, s.id)

	def test_no_args_no_kwargs_set_changed_attributes(self):
		s = Square(4, 0

, 0, 1)
		s.size = 5
		s.x = 2
		s.y = 3
		s.id = 4
		s.update()
		self.assertEqual(5, s.size)
		self.assertEqual(2, s.x)
		self.assertEqual(3, s.y)
		self.assertEqual(4, s.id)


if __name__ == '__main__':
	unittest.main()
