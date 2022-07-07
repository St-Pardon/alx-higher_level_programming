#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object param
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, n;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		n = 10;
	else
		n = size + 1;

	printf("  first %ld bytes:", n);

	for (i = 0; i < n; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object param
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *arr;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	arr = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", arr->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
