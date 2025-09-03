# rishi/utils.py

def list_reverse(lst):
    return lst[::-1]

def get_unique_elements(lst):
    return list(set(lst))

def word_count(text):
    return len(text.split())
