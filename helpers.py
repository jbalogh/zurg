import operator

import rfc3339


def sortby(seq, key, reverse=False):
    return sorted(seq, key=operator.attrgetter(key), reverse=reverse)


def xml_date(date):
    return rfc3339.rfc3339(date)


filters = [sortby, xml_date]
