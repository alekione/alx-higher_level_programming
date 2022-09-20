#include "lists.h"
#include "stdlib.h"

/**
 * insert_node - inserts a node at a specific location
 * @head: linked list head
 * @number: node position
 * Return: address position of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *current;

	if (head == NULL)
		return (NULL);
	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	ptr->next = NULL;
	current = *head;
	if (current == NULL)
	{
		*head = ptr;
		return (*head);
	}
	if (current->n >= number)
	{
		ptr->next = *head;
		*head = ptr;
		return (ptr);
	}
	while (current->next != NULL)
	{
		if (current->next->n >= number)
		{
			ptr->next = current->next;
			current->next = ptr;
			return (ptr);
		}
		current = current->next;
	}
	current->next = ptr;
	return (ptr);
}
