#include "lists.h"

/**
* check_cycle - Check is cycle or no
* @list: Head of list
* Return: false or true
*/

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *current = list;

	while (tmp->next != NULL && current->next != NULL)
	{
		current = current->next->next;
		tmp = tmp->next;
		if (current == tmp)
		{
			return (1);
		}
		else
		{
			return (0);
		}
	}
	return (0);
}
