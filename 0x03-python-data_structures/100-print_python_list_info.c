#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *arr;
	PyObject *elem;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	arr = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", arr->allocated);

	for (i = 0; i < size; i++)
	{
		elem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);
	}
}
