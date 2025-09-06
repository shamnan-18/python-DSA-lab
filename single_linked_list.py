class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            print(f"Deleted node with value {key}")
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next
        print(f"Deleted node with value {key}")

    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                print(f"Updated node value from {old_value} to {new_value}")
                return
            current = current.next
        print(f"Node with value {old_value} not found.")

    def display(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    ll = SinglyLinkedList()

    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            ll.insert(value)
        elif choice == '2':
            value = int(input("Enter value to delete: "))

            ll.delete(value)
        elif choice == '3':
            old_value = int(input("Enter value to update: "))
            new_value = int(input("Enter new value: "))
            ll.update(old_value, new_value)
        elif choice == '4':
            ll.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
