Here is the code with spaces removed from the beginning and end of lines and replaced with tabs:

```python
#!/usr/bin/python3

def safe_print_division(a, b):
	"""Returns the division of a by b."""
	try:
		div = a / b
	except (TypeError, ZeroDivisionError):
		div = None
	finally:
		print("Inside result: {}".format(div))
	return (div)
