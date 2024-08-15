#!usr/bin/env python3
def index_range(page, page_size):
    total_pages = page_size * page
    return ((page - 1) * page_size, total_pages)

