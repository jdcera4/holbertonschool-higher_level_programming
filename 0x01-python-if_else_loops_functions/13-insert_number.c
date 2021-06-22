#include "lists.h"

/**
* insert_node - insert new node
* @head: head of linked list
* @number: Date of structure
* Return: New node
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode = *head;

    newNode = malloc(sizeof(listint_t));
	newNode->n = number;
    newNode->next = NULL;
    if (*head == NULL)
    {
        return (NULL);
    }
    else
    {
        listint_t *lastNode = *head;
        while (lastNode->next != NULL)
        {
            lastNode = lastNode->next;
        }
        lastNode->next = newNode;
    }
	return (newNode);
}
