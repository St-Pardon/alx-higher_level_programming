#include "lists.h"

/**
 * reverse - reverses the second half of the list
 * @h_r: head of the second half
 */

void reverse(listint_t **h_r)
{
	listint_t *prev, *curr, *nest;

	prev = NULL;
	curr = *h_r;

	while (curr != NULL)
	{
		nest = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nest;
	}

	*h_r = prev;
}

/**
 * compare - compares each int of the list
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1, *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *half;
	int isp;

	slow = fast = prev_slow = *head;
	half = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			half = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (half != NULL)
		{
			prev_slow->next = half;
			half->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
