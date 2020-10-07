class CQueue:
    """Queue Implementation
    
    Circular queue implemented using static array (implicit)
    Contains all necessary functions associated with queues (enqueue, dequeue)
    Uses helper functions (queue_empty, queue_full) to carry out main functions
    
    Atributes:
        _queue_size (int): The maximum number elements which can be stored in the queue
        _queue (:obj:`list` of :obj:`int`): Array stores elements in queue
        _head (int): Pointer pointing to index of head of queue
        _tail (int, None): Pointer pointing to index of end of queue. Defaults to `None` when queue is empty.
    """
    def __init__(self, queue_size: int = 10):
        """Initailise Queue

        Args:
            queue_size (int, optional): The maximum length of the queue. Defaults to 10.
        """
        self._queue_size = queue_size
        self._queue = [None] * queue_size
        self._head = 0
        self._tail = None
    
    def enqueue(self, value: int) -> bool:
        """Enqueue method

        Args:
            value (int): value which will be enqueued to the end of the queue

        Returns:
            bool: indicates if enqueue was successful or unsuccessful (queue was full)
        """
        
        # sets tail if list is empty
        if self.queue_empty():
            self._tail = self._head
        # prevents enqueue if queue is full
        elif self.queue_full():
            return False
        else:
            # increments tail to next empty element in queue
            self._tail = (self._tail + 1) % self._queue_size
        
        # enqueue `value` into queue
        self._queue[self._tail] = value
        
        return True
    
    def dequeue(self) -> [bool, int]:
        """Dequeue method

        Returns:
            [bool, int]: 
                False, if dequeue was unsuccessful (queue was empty). 
                Int, which is value dequeued from list.
        """
        
        if not self.queue_empty():
            # copy and dequeue head of queue
            return_value = self._queue[self._head]
            self._queue[self._head] = None
            
            # update head to current start of queue
            self._head = (self._head + 1) % self._queue_size
            return return_value
        
        # unsuccessful action (empty queue)
        return False

    def queue_empty(self) -> bool:
        """Helper Function: checks if queue is empty

        Returns:
            bool: True, if queue is empty. False if queue is empty.
        """
        return self._tail == None

    def queue_full(self) -> bool:
        """Helper function: checks if queue is full

        Returns:
            bool: True if queue is full. False if queue is empty.
        """
        return (self._tail + 1) % 6 == self._head
        
        
def main():
    """Main function
    
    Tests methods in `CQueue` class 
    """
    myQueue = CQueue(5)
    
    # add elements to queue
    for i in range(3):
        myQueue.enqueue(i)
        print(myQueue._queue)
    
    # remove all elements from queue - reject dequeues when queue is empty
    for i in range(5):
        myQueue.dequeue()
    print(myQueue._queue)
    
    # add elements to queue - reject elements when full
    for i in range(6):
        myQueue.enqueue(i)
        print(myQueue._queue)
    
    # dequeue elements from queue - reject dequeues when queue is empty
    for i in range(1000):
        myQueue.dequeue()
    print(myQueue._queue)
    
if __name__ == "__main__":
    main()