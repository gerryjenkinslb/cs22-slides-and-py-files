# from Text Book

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:  # unordered list

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self): # return string with items
        current = self.head
        s = "[ "
        while current != None:
            s = s + str(current.getData())
            current = current.getNext()
            if current:
                s = s + ", "
        return s + " ]"

    def add_order(self,item):
        current = self.head
        previous = None
        n = Node(item)
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current # remember
                current = current.getNext()
        if previous == None:
            n.setNext(self.head)
            self.head = n
        else:
            n.setNext(current)
            previous.setNext(n)
        return

    # missing index(item), pop(), pop(pos), insert(pos,item), set(pos,item), get(pos)

    ### note code that follows is to help debug problems by giving a way to print a crude
    #   picture of the linked list structure

    def dump(self): # new version to name the nodes found n1, n2, etc.
        # instead of dumping raw id numbers
            nodes =  {}  # dictinary to map node id to n1, n2, n2 to make reading dump easier

            def addr(x): # return a address label for node x, if one does not exits, create one n1,n2,...
                if x is None:  # address x does not point to a node
                    return "None"
                else:
                    if id(x) in nodes: # address already has label, use it
                        return nodes[id(x)]
                    else: # create next avaliable label in sequence n1,n2,n3, ... etc
                        nodes[id(x)] = "n%d"%(len(nodes)+1)
                        return nodes[id(x)]

            print ("  ","-"*20," DUMP of Deque ","-"*20)
            print ("    self.head: " , addr(self.head))
            node = self.head

            while node is not None:
                print ("\n     Node: ",addr(node))
                print ("         data: ",node.data)
                print ("         next: ",addr(node.next))
                node = node.next
            print( "  ", "-"*50)


l = UnorderedList()
l.add_order(10) # into empty list
l.add_order(3)  # at beginning
l.add_order(15) # at end
l.add_order(55)
l.add_order(11)

