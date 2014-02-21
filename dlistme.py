#!/usr/bin/env python
# -*- coding: utf-8 -*-
def linkab(a,b):
    a.next=b#link node
    b.prev=a    
class Node(object):
    def __init__(self, value=None):
        self.prev = None
        self.next = None
        self.value = value

class Linkedlist(object):
    def __init__(self):
        self.head     = None
        self.tail     = None
    def __str__(self):
        s=""
        n=self.head    
        if n!=None:
            s=str(n.value)
        n=n.next
        while n!=None:
            s+="->"+str(n.value)
            n=n.next
        return s
    def str2(self):
        s=""
        n=self.tail    
        if n!=None:
            s=str(n.value)
        n=n.prev
        while n!=None:
            s+="->"+str(n.value)
            n=n.prev
        return s
    def insert_before(self,node,newnode):
        if node==None:
            return
        prev=node.prev
        linkab(prev,newnode)
        linkab(newnode,node)
    def appendleft(self, node):
        if self.head    ==None:
            self.head    =node
            self.tail    =node
        else:
            linkab(node,self.head    )
            self.head    =node
    def appendright(self, node):
        if self.tail    ==None:
            self.tail    =node
            self.head    =node
        else:
            linkab(self.tail    ,node)
            self.tail    =node
    def append(self, node):
        return self.appendright(node)
def main():
    a=Linkedlist()
    n=Node(1)
    a.appendright(n)
    n2=Node(2)
    a.appendright(n2)
    n=Node(3)
    a.insert_before(n2,n)
    print a
    print a.str2()
main()

