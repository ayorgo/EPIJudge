from test_framework import generic_test


def h_index(citations):
    count = 0
    for citation in reversed(sorted(citations)):
        if citation <= count:
            return count
        count += 1
    return count


if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
