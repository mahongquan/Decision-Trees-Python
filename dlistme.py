#!/usr/bin/env python
# -*- coding: utf-8 -*-
def linkab(a,b):
    a.next=b#link node
    b.prev=a    
def unlinkab(a,b):
    a.next=None
    b.prev=None
class Node(object):
    def __init__(self, value=None):
        self.prev = None
        self.next = None
        self.value = value
    def str_left(self):
        s=str(self.value)
        n=self.prev
        while n!=None:
            s+="->"+str(n.value)
            n=n.prev
        return s        
    def str_right(self):
        s=str(self.value)
        n=self.next
        while n!=None:
            s+="->"+str(n.value)
            n=n.next
        return s
    def str(self):
        return self.head().str_right() 
    def link_right(self,b):
        self.next=b
        b.prev=self
    def link_left(self,b):
        self.prev=b
        b.next=self
    def unlink_right(self):
        b=self.next
        self.next=None
        if b!=None:
            b.prev=None
    def unlink_left(self):
        b=self.prev
        self.prev=None
        if b!=None:
            b.next=None
    def head(self):
        if self.prev==None:
            return self
        else:
            return self.prev.head()
    def tail(self):
        if self.next==None:
            return self
        else:
            return self.next.tail()
    # def cut_prev(self):
    #     before=self.prev
    #     if before!=None:
    #     else:
    #         unlinkab(before,self)
    def remove_self(self):
        before=self.prev
        after=self.next

        self.unlink_left()
        self.unlink_right()

        if before!=None and after!=None:
            before.link_right(after)
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
    def cut_before(self,node):
        if node==None:
            return
        before=node.prev
        if before==None:
            self.head=None
            self.tail=None
        node.prev=None
        return node
    def insert_before(self,node,newnode):
        if node==None:
            return
        prev=node.prev
        linkab(prev,newnode)
        linkab(newnode,node)
    def remove(self,node):
        if node==None:
            return
        before=node.prev
        after=node.next
        if before!=None:
            #
            if after!=None:
                #middle
                unlinkab(before,node)
                unlinkab(node,after)
                linkab(before,after)
            else:
                #tail
                unlinkab(before,node)
                self.tail=before
        else:
            #remove first
            if after!=None:
                #
                unlinkab(node,after)
                self.head=after
            else:
                #remove lastone
                self.head=None
                self.tail=None

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
    def pop(self):
        if self.tail==None:
            return None
        last=self.tail
        newlast=last.prev
        unlinkab(newlast,last)
        last.next=None
        return last
def main():
    a=Linkedlist()
    n1=Node(1)
    a.append(n1)
    #a.appendright(n)
    n2=Node(2)
    #a.appendright(n2)
    a.append(n2)
    n3=Node(3)
    a.insert_before(n2,n3)
    print a
    #print a.str2()
    #b=a.pop()
    a.remove(n3)
    print a
    #print b.value,b.prev,b.next
def test2():
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n1.link_right(n2)
    n2.link_right(n3)
    #n2.unlink_left()
    n2.remove_self()
    print n2.str()# n2.str_left()#n1.str_right()
    print n1.str()
if __name__=="__main__":
    #main()
    test2()

