#!/usr/bin/env python3
import csv
import math
from typing import List


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
        if looking[0] > len(fulldata):
            return []
        return fulldata[looking[0]:looking[1]]

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the indexes contained in a page given a page_size
    """
    return ((page - 1) * page_size, page * page_size)
