"""
https://edube.org/learn/pcpp1-working-with-restful-apis/new-york-stock-exchange
"""

import xml.etree.ElementTree

just_size = 15
company_just_size = 40

nyse = xml.etree.ElementTree.parse('nyse.xml').getroot()
header = ['Company', 'Last', 'Change', 'Min', 'Max']

# Header
for header_item in header:
    if header_item == 'Company':
        print(header_item.ljust(company_just_size), end='| ')
    else:
        print(header_item.ljust(just_size), end='| ')

# Delimiter
print()
print('-' * (company_just_size + 1), end='')
print('-' * (just_size * (len(header) - 1) + len(header)*2))

# Body
for quote in nyse.findall('quote'):
    print(quote.text.ljust(company_just_size + 2), end='')
    print(quote.attrib.get('last').ljust(just_size + 2), end='')
    print(quote.attrib.get('change').ljust(just_size + 2), end='')
    print(quote.attrib.get('min').ljust(just_size + 2), end='')
    print(quote.attrib.get('max').ljust(just_size + 2))
