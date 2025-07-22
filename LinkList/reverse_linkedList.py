from linkedList import LinkedList
from node import Node

def reverse_linkedList(linkedList:LinkedList):
    prev = None
    current_node = linkedList.first

    while current_node is not None:
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next

    linkedList.first = prev

    return linkedList

def print_linkList_item(linkedList:LinkedList):
    current_node = linkedList.first
    while current_node is not None:
        if current_node.next is not None:
            print(f"{current_node.item} --> ", end="")
        else:
            print(current_node.item)
        current_node = current_node.next


if __name__ == "__main__":
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(10)
    node4 = Node(2)
    node5 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    linkedList = LinkedList()
    linkedList.first = node1

    reversed_linkedList = reverse_linkedList(linkedList)
    print_linkList_item(reversed_linkedList)