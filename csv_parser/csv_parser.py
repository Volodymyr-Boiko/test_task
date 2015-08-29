#! /usr/bin/python


import csv
from collections import OrderedDict


def passed_tests(file_name):
    """passed_tests_count, failed_tests_count, created_at"""
    lst = _parser(file_name)
    test_dct = {}
    date_list = _list_maker(file_name)
    for item in date_list:
        s = 0
        for sec_item in lst:
            if item == sec_item.get('created_at')[:10]:
                s += int(sec_item.get('passed_tests_count'))
                test_dct[sec_item.get('created_at')[:10]] = s
    return test_dct


def failed_tests(file_name):
    """passed_tests_count, failed_tests_count, created_at"""
    lst = _parser(file_name)
    test_dct = {}
    date_list = _list_maker(file_name)
    for item in date_list:
        s = 0
        for sec_item in lst:
            if item == sec_item.get('created_at')[:10]:
                s += int(sec_item.get('failed_tests_count'))
                test_dct[sec_item.get('created_at')[:10]] = s
    return test_dct


def _list_maker(file_name):
    lst = _parser(file_name)
    test_lst = [item.get('created_at')[:10] for item in lst]
    return list(OrderedDict.fromkeys(test_lst))


def _parser(file_name):
    lst = []
    try:
        with open(file_name, 'rb') as csv_file:
            filereader = csv.DictReader(csv_file)
            for row in filereader:
                lst.append(row)
        return lst
    except IOError:
        return []


if __name__ == '__main__':
    print failed_tests('session_history.csv')
