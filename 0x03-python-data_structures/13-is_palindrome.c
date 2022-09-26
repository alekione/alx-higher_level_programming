#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks whether a given linked list is a palindrome
 * @head: linked list head
 * Return: 1 if true 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *start;
	int ind = 0, arr[200];

	if (head == NULL || *head == NULL)
		return (1);
	start = *head;
	while (start->next != NULL)
	{
		arr[ind] = start->n;
		if (start->next->n == arr[ind])
		{
			start = start->next;
			while (ind != 0 && start != NULL)
			{
				if (start->next->n != arr[ind - 1])
					return (0);
				start = start->next;
				ind--;
			}
			if (ind != 0 || start->next != NULL)
				return (0);
			break;
		}
		ind++;
		start = start->next;
	}
	return (1);
}
