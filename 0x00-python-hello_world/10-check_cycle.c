#include "lists.h"
#include <stdio.h>
/**
* check_cycle - Check is cycle or no
* @list: Head of list
* Return: false or true
*/

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *current = list;

	while (current && tmp && current->next)
	{
		current = current->next->next;
		tmp = tmp->next;
		
		if (current == tmp)
		{
			return (1);
		}
	}
	return (0);
}
