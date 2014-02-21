#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value=None):
        self.prev = None
        self.next = None
        self.value = value

class Linkedlist(object):
    def __init__(self):
        self.first = None
        self.last = None
    def __str__(self):
        s=""
        n=self.first
        if n!=None:
            s=str(n.value)
        n=n.next
        while n!=None:
            s+="->"+str(n.value)
            n=n.next
        return s
    def appendleft(self, node):
        node.prev=None
        node.next=None
        if self.first==None:
            self.first=node
            self.last=node
        else:
            node.next=self.first
            self.first.prev=node
            self.first=node
    def appendright(self, node):
        if self.last==None:
            self.last=node
            self.first=node
        else:
            node.prev=self.last
            self.last.next=node
            self.last=node
    def append(self, node):
        return self.appendright(node)
def main():
    a=Linkedlist()
    n=Node(1)
    a.appendright(n)
    n=Node(2)
    a.appendright(n)
    print a
main()

