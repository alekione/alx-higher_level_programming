#include "lists.h"

/**
 * check_cycle - checks whether a linked list has a loop
 * @list: lined list head
 * Return: 0 if none, 1 for otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *head;

	head = list;
	while (head != NULL)
	{
		ptr = head->next;
		while (ptr != NULL)
		{
			if (ptr == head)
				return (1);
			ptr = ptr->next;
		}
		head = head->next;
	}
	return (0);
}
