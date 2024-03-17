class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_linked_list(self):
        """
        Reverses a linked list.
        No parameters.
        No return value.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort_linked_list(self, head):
        """
        Sorts a linked list using the merge sort algorithm.
        Args:
            head (ListNode): The head of the linked list to be sorted.
        Returns:
            ListNode: The head of the sorted linked list.
        """
        if head is None or head.next is None:
            return head

        mid = self.get_middle(head)
        mid_next = mid.next
        mid.next = None

        left = self.merge_sort_linked_list(head)
        right = self.merge_sort_linked_list(mid_next)

        return self.merge(left, right)

    def get_middle(self, head):
        """
        A function to find the middle element of a linked list given the head node.
        Parameters:
            self: the instance of the class
            head: the head node of the linked list
        Returns:
            The middle element of the linked list
        """
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        """
        Merge two linked lists recursively based on the data in each node.
        Parameters:
        left (ListNode): The head of the first linked list.
        right (ListNode): The head of the second linked list.
        Returns:
        ListNode: The head of the merged linked list.
        """
        if left is None:
            return right
        if right is None:
            return left

        if left.data < right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    def merge_sorted_lists(self, head1, head2):
        """
        Merge two sorted linked lists and return the head of the merged list.
        Parameters:
            head1 (Node): The head of the first sorted linked list.
            head2 (Node): The head of the second sorted linked list.
        Returns:
            Node: The head of the merged sorted linked list.
        """
        dummy_node = Node(0)
        tail = dummy_node

        while True:
            if head1 is None:
                tail.next = head2
                break
            if head2 is None:
                tail.next = head1
                break

            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

        return dummy_node.next


### Приклад використання ###

# Створення першого списку: 1 -> 3 -> 5
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

# Створення другого списку: 2 -> 4 -> 6
llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

# Об'єднання відсортованих списків
merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(llist1.head, llist2.head)

# Виведення об'єднаного списку
merged_list.print_list()  # Виведення списку: 1 -> 2 -> 3 -> 4 -> 5 -> 6
