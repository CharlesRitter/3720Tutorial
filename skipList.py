from random import random
import sys

class skipList:
    #nodes on the skip list
    class skipNode:
        def __init__(self, value, height, next, down):
            self.value = value
            self.next = next
            self.down = down
            self.height = height

    #list constructor
    def __init__(self):
        self.head = self.skipNode(None, 0, None, None)

    #inserts a value in the list
    def insert(self, value):
        #determines the height the value will be placed at
        height = 0

        while(random() < 0.5):
            height = height + 1

        #insert into the list
        self.insertAcross(value, height, self.head, None)

    #recursively moves across and down the layers and inserts value
    def insertAcross(self, value, height, head, upper):
        #base case : if node is null, all layers have been inserted, return
        if(head == None):
            return
        #if the list isn't tall enough, make it taller
        if(head.height != None and head.height < height):
            self.head = self.skipNode(None, self.head.height + 1, None, self.head)
            #recurse to the upper layer
            self.insertAcross(value, height, self.head, None)
        #if the space where the value should be inserted is found, insert it
        elif(head.next == None or value < head.next.value):
            head.next = self.skipNode(value, None, head.next, None)
            #set the down pointer for the upper layer
            if(upper != None):
                upper.down = head.next
            #recurse to the next layer
            self.insertAcross(value, height, head.down, head.next)
        #recurse to the next node on that layer
        else:
            self.insertAcross(value, height, head.next, upper)

    def getDepth(self, head):
        if(head == None):
            return(0)
        else:
            return(1 + self.getDepth(head.down))

    def getTopLayer(self):
        head = self.head
        print(head.height)
        while(head.next != None):
            print(head.next.value)
            head = head.next

        return

    #finds a value and returns it
    def find(self, value, head):
        #base case: if head is null, the search has failed
        if(head == None):
            return(-1)
        else:
            print(head.next.value)
            #the value is found
            if(head.next != None and head.next.value == value):
                return(value)
            #the layer does not contain the value
            elif(head.next == None or value < head.next.value):
                return(self.find(value, head.down))
            else:
            #the value is not at this node
                return(self.find(value, head.next))

def rangeProductTest(numVal):
    rangeList = skipList()
    for i in range(1, (10**numVal) + 1):
        rangeList.insert(i)

    head = rangeList.head
    min = head.next.value
    max = head.next.value
    while(head.next != None):
        if(head.next.value < min):
            min = head.next.value
        if(max < head.next.value):
            max = head.next.value
        head = head.next

    return(min * max)

def main():
    sys.setrecursionlimit(1500)
    average = 0
    for i in range (0, 100):
        average += rangeProductTest(int(sys.argv[1]))
    average /= 100
    print(average)



if __name__ == '__main__':
    main()
