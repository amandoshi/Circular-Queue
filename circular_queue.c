#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// declare functions
bool enqueue(char* value);
bool dequeue(void);
bool isEmpty(void);
bool isFull(void);

// declare const for max. length of queue
#define MAXLENGTH 6

// declare circular queue
char* CQUEUE[MAXLENGTH];
unsigned int HEAD = 0;
unsigned int TAIL = -1;

int main(void)
{
	// add elements to circular queue
	char* names[6] = { "Aman", "Pratyush", "Tom", "Dawud", "Mr. Wood", "Mr. Forsyth" };
	bool valid;
	for (int i = 0; i < 6; i++)
	{
		valid = enqueue(names[i]);
		printf("name: %s, queue: %d, head: %d, tail: %d\n", names[i], valid, HEAD, TAIL);
	}

	// add elemnt to queue - should reject element
	valid = enqueue("John");
	printf("name: %s, queue: %d, head: %d, tail: %d\n\n", "John", valid, HEAD, TAIL);

	// dequeue all items (and more)
	for (int i = 0; i < 9; i++)
	{
		valid = dequeue();
		printf("index: %d, dequeue: %d, head: %d, tail: %d\n", i, valid, HEAD, TAIL);
	}

	// add elements back to queue
	printf("\n");
	for (int i = 0; i < 6; i++)
	{
		valid = enqueue(names[i]);
		printf("name: %s, queue: %d, head: %d, tail: %d\n", names[i], valid, HEAD, TAIL);
	}

	// add element to queue - should reject element
	valid = enqueue("John");
	printf("name: %s, queue: %d, head: %d, tail: %d\n\n", "John", valid, HEAD, TAIL);

	return 0;
}

bool enqueue(char* value)
{
	// check if queue is empty
	if (isEmpty())
	{
		TAIL = HEAD;
	}
	// check if queue if full
	else if (isFull())
	{
		return false;
	}
	// add value at queue[head]
	else
	{
		// tail++
		TAIL = (TAIL + 1) % MAXLENGTH;	
	}


	CQUEUE[TAIL] = value;
	return true;

}

bool dequeue(void)
{
	// check if queue is not empty
	if (!isEmpty())
	{
		// delete queue[head]
		CQUEUE[HEAD] = "";

		// remove tail if head equals tail
		if (HEAD == TAIL)
		{
			TAIL = -1;
		}
		else
		{
			// head++
			HEAD = (HEAD + 1) % MAXLENGTH;
		}
		return true;
	}
	return false;
}

bool isEmpty(void) { return TAIL == -1; }
bool isFull(void) { return  (TAIL + 1) % MAXLENGTH == HEAD; }