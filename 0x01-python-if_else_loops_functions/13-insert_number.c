#include "lists.h"

/**
* insert_node - insert new node
* @head: head of linked list
* @number: Date of structure
* Return: New node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL;
	listint_t *lastNode = NULL, *aux = NULL;

	if (head == NULL)
	{
		return (NULL);
	}
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
	{
		return (NULL);
	}
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	if (number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	lastNode = *head;
	while (lastNode->next != NULL && lastNode->n < number)
	{
		aux = lastNode;
		lastNode = lastNode->next;
	}
	if (lastNode != NULL)
	{
		newNode->next = lastNode;
		aux->next = newNode;
		return (newNode);
	}
	lastNode->next = newNode;
	return (newNode);
}
