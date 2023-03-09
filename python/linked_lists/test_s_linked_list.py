import unittest
import s_linked_list

# Test all functions of SLinkedList class
class TestSLinkedList(unittest.TestCase):
    def test_s_linked_list_initialization(self):
        self.assertEqual(s_linked_list.SLinkedList().head, None)

    def test_s_linked_list_add_head(self):
        llist = s_linked_list.SLinkedList()
        for i in range(1, 100):
            llist.addHead(i)
        
        tmp = llist.head
        while tmp != None:
            self.assertEqual(tmp.dataval, i)
            tmp = tmp.nextval
            i -= 1

    def test_s_linked_list_add_tail(self):
        llist = s_linked_list.SLinkedList()

        for i in range(1, 100):
            llist.addTail(i)

        tmp = llist.head
        i = 1
        while (tmp != None):
            self.assertEqual(tmp.dataval, i)
            tmp = tmp.nextval
            i += 1

    def test_s_linked_list_remove_head(self):
        llist = s_linked_list.SLinkedList()

        for i in range(1, 100):
            llist.addTail(i)

        for i in range(1, 100):
            llist.removeHead()

        self.assertEqual(llist.head, None)

        llist.removeHead()
        self.assertEqual(llist.head, None)
    
    def test_s_linked_list_remove_tail(self):
        llist = s_linked_list.SLinkedList()

        for i in range(1, 100):
            llist.addTail(i)

        for i in range(1, 100):
            llist.removeTail()

        self.assertEqual(llist.head, None)

        llist.removeTail()
        self.assertEqual(llist.head, None)
    
    def test_s_linked_list_remove(self):
        llist = s_linked_list.SLinkedList()

        for i in range(1, 100):
            llist.addTail(i)

        for i in range(1, 100):
            llist.remove(i)

        self.assertEqual(llist.head, None)

        llist.remove(i)
        self.assertEqual(llist.head, None)

    def test_s_linked_list_reverse(self):
        llist = s_linked_list.SLinkedList()

        llist.reverse()
        self.assertEqual(llist.head, None)

        for i in range(1, 100):
            llist.addTail(i)
        
        llist.reverse()

        tmp = llist.head
        i = 99
        while (tmp != None):
            self.assertEqual(tmp.dataval, i)
            tmp = tmp.nextval
            i -= 1



if __name__ == '__main__':
    unittest.main()