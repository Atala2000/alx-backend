#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """
    Function to return a list of index used for pagination
    Args:
        page (int): Current page number
        page_size (int): Items per page
    """
    total_pages = page_size * page
    return ((page - 1) * page_size, total_pages)
