#! /usr/bin/python


import csv


def make_list(file_name):
    lst = []
    test_lst = _parser(file_name)
    for item in test_lst[1:]:
        lst.append(dict(zip(test_lst[0], item)))
    return lst


def _parser(file_name):
    lst = []
    try:
        with open(file_name, 'rb') as csv_file:
            filereader = csv.reader(csv_file)
            for row in filereader:
                lst.append(row)
        return lst
    except IOError:
        return []


def fff(file_name):
    """passed_tests_count, failed_tests_count, created_at"""
    lst = make_list(file_name)
    for item in lst:
        return item.items()



ddd = ['commit_id', 'passed_tests_count', 'pending_tests_count', 'num_workers',
       'failed_tests_count', 'created_at', 'spointummary_status',
       'skipped_tests_count', 'session_id', 'started_by', 'started_tests_count',
       'worker_time', 'branch', 'bundle_time', 'duration', 'error_tests_count']


if __name__ == '__main__':
    print fff('session_history.csv')
    # print "2014-09-10 05:38:55 UTC"[:10]