from node import Node
from linkedList import LinkedList
from print_linked_list import print_linkList_item

def merge_sorted_linkedList(linkedList1:LinkedList, linkedList2:LinkedList) -> LinkedList:
    dummy = Node(0)
    current = dummy

    current1 = linkedList1.first
    current2 = linkedList2.first

    while current1 is not None and current2 is not None:
        if current1.item > current2.item:
            current.next = current2
            current2 = current2.next
        else:
            current.next = current1
            current1 = current1.next
        current = current.next
    
    if current1 is not None:
        current.next = current1
    if current2 is not None:
        current.next = current2
    
    merged_linkedList = LinkedList()
    merged_linkedList.first = dummy.next
    return merged_linkedList

if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(10)
    node4 = Node(13)
    node5 = Node(15)
    node6 = Node(17)
    node7 = Node(19)
    node8 = Node(21)
    node9 = Node(25)
    node10 = Node(27)
    
    linkedList1 = LinkedList()
    linkedList1.first = node1

    linkedList2 = LinkedList()
    linkedList2.first = node2

    node1.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node9

    node2.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node10

    merged_linkedList = merge_sorted_linkedList(linkedList1, linkedList2)
    print_linkList_item(merged_linkedList)
    