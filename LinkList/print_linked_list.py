from linkedList import LinkedList

def print_linkList_item(linkedList:LinkedList):
    current_node = linkedList.first
    while current_node is not None:
        if current_node.next is not None:
            print(f"{current_node.item} --> ", end="")
        else:
            print(current_node.item)
        current_node = current_node.next