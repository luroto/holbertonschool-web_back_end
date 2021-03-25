#!/usr/bin/env python3
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function for getting the page content
        """
        assert isinstance(page, int) is True
        assert isinstance(page_size, int) is True
        assert page > 0
        assert page_size > 0

        looking = index_range(page, page_size)
        fulldata = self.dataset()
        return fulldata[looking[0]:looking[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Creates a dictionary hypermedia style
        """
        fulldata = self.dataset()
        total_pages = math.ceil(len(fulldata) / page_size)
        prev = 0
        nextico = 0
        nextico = page + 1 if page < total_pages else None
        prev = page - 1 if page - 1 != 0 else None
        tamapa = page_size if page <= total_pages else 0
        return {'page_size': tamapa, 'page': page,
                'data': self.get_page(page, page_size),
                'next_page': nextico,
                'prev_page': prev,
                'total_pages': total_pages}
