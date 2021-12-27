"""
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)
    
    def pop_front(self):
        cur = self._head
        self._head = cur.next
        if self._length == 1:
            del cur
        else:
            self._head.prev = None
            del cur
        self._length-=1 
    
    def clean(self):
        for i in range(self._length):
            self.pop_front()
            
    def insert_at_end(self, data):
        
        if self._head is None:
            new_node = MyList._ListNode(data)
            new_node.prev = None
            self._head = new_node
        else:
            new_node = MyList._ListNode(data)
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None        
            
    def insert_at_start(self, data):
        
        if self._head is None:
            new_node = MyList._ListNode(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = MyList._ListNode(data)
            self._head.prev = new_node
            new_node.next = self._head
            self._head = new_node
            new_node.prev = None
                    
    def insert_before_item(self, index, data):
        cur = self._head
        
        if  index == 0:
            self.insert_at_start(data) 
        elif index == len(self):
            self.insert_at_end(data)                     
        else:
            cur = self.get_node_index(index)
            new_node = MyList._ListNode(data)
            prev = cur.prev
            prev.next = new_node
            cur.prev = new_node    
            new_node.next = cur
            new_node.prev = prev
        cur = cur.next             
        
    def get_node_index(self, index):
        if index < 0:
            index += len(self)
            
        node = self._head
        for _ in range(index):
            node = node.next
        return node 
    
    def get_node_value(self, index):
        if index < 0:
            index += len(self)
            
        node = self._head
        for _ in range(index):
            node = node.next
        return node.value 
    
    def remove(self, node_value):
        current_node = self._head
        if node_value == self.get_node_value(len(self)):
            self.delete_at_end()
        else:    
            while current_node is not None:
                if current_node.value == node_value:
                    if current_node.prev is not None:                   
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    else:
                        self._head = current_node.next
                        current_node.next.prev = None
                current_node = current_node.next    
    
    def delete_at_end(self):
        if self._head is None:
            print("The list has no element to delete")
            return 
        if self._head.next is None:
            self._head = None
            return
        n = self._head
        while n.next is not None:
            n = n.next
        n.prev.next = None        

def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    my_list.pop_front()

    # Повторный обход списка
    for element in my_list:
        print(element)
    print("\n")
    my_list.insert_before_item(2,12)  
    for element in my_list:
        print(element)

    print("\n")
    
    my_list.remove(12)
    for element in my_list:
        print(element)
        
if __name__ == '__main__':
    main()