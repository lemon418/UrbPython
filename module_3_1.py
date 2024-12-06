
calls = 0

def count():
    global calls
    calls += 1

def string_info(string):
    count()
    lent = len(string)
    return lent, string.upper(), string.lower()

def is_contains(string, list_to_search):
    count()
    bool = False
    for i in list_to_search:
        if i == string:
            bool = True
            return bool
    return bool

print(string_info('Night'))
print(string_info('Morning'))
print(is_contains('Day', ['Day', 'Night', 'Morning', 'Evening']))
print(is_contains('Moon', ['Day', 'Night', 'Morning', 'Evening']))
print(calls)
