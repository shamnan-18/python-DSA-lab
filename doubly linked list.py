class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete node by value
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            if self.head:  # Update prev link of new head
                self.head.prev = None
            temp = None
            return True

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            return False

        if temp.next:   # If not last node
            temp.next.prev = temp.prev
        if temp.prev:   # If not first node
            temp.prev.next = temp.next

        temp = None
        return True

    # Update node value
    def update(self, old_value, new_value):
        temp = self.head
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                return True
            temp = temp.next
        return False
    
     # Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            last = temp   # Keep track of last node
            temp = temp.next
        print("None")
        return last  # return tail node for reverse display

    # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next   # move to last node
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


def main():
    dll = DoublyLinkedList()

    while True:
        print("\n----- Doubly Linked List Menu -----")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Display Forward")
        print("5. Display Backward")
        print("6. Exit")

        choice = int(input("Enter your choice: "))


        if choice == 1:
            data = int(input("Enter value to insert: "))
            dll.insert(data)
            print("Node inserted.")
        elif choice == 2:
            key = int(input("Enter value to delete: "))
            if dll.delete(key):
                print("Node deleted.")
            else:
                print("Value not found.")

        elif choice == 3:
            old_val = int(input("Enter value to update: "))
            new_val = int(input("Enter new value: "))
            if dll.update(old_val, new_val):
                print("Node updated.")
            else:
                print("Value not found.")
        elif choice == 4:
            print("Forward Traversal:")
            dll.display_forward()
        elif choice == 5:
            print("Backward Traversal:")
            dll.display_backward()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()