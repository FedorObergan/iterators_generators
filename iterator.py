class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.start_index = 0
        self.lists_amount = len(list_of_list)

    def get_current_elements(self):
        self.current_elements = self.list_of_lists[self.current_list_index].copy()

    def __iter__(self):
        self.current_elements = []
        self.current_list_index = self.start_index - 1
        return self

    def __next__(self):
        if len(self.current_elements) == 0:
            self.current_list_index += 1
            if self.current_list_index >= self.lists_amount:
                raise StopIteration
            self.get_current_elements()
        elem = self.current_elements.pop(0)
        return elem


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
