from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    
    ll.insert_at_front(1)
    ll.insert_at_front(2)
    ll.insert_at_front(3)

    
    print("Initial list:")
    ll.display()

    total = ll.recursive_sum()
    print(f"Sum of all node data (recursive): {total}")

    target = 2
    found = ll.recursive_search(target)
    print(f"Search for {target}: {'found' if found else 'not found'}")

    target = 999
    found = ll.recursive_search(target)
    print(f"Search for {target}: {'found' if found else 'not found'}")

    print("Reversing list recursively...")
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()