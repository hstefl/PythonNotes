"""
https://edube.org/learn/pcpp1-5/lab-xml-lab-2

<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>
"""

import xml.etree.ElementTree
from os import write
from xml.etree.ElementTree import ElementTree, Element, dump, SubElement

root = Element('shop')
category = SubElement(root, 'category', {'name':'Vegan Products'})

product1 = SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})
type1 = SubElement(product1, 'type', )
type1.text = 'beverages'
producer1 = SubElement(product1, 'producer', )
producer1.text = 'Drinks4Coders Inc.'
price1 = SubElement(product1, 'price', )
price1.text = '19.75'
currency1 = SubElement(product1, 'currency', )
currency1.text = 'USD'

product2 = SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
type2 = SubElement(product2, 'type', )
type2.text = 'pasta'
producer2 = SubElement(product2, 'producer', )
producer2.text = 'Programmers Eat Pasta'
price2 = SubElement(product2, 'price', )
price2.text = '15.49'
currency2 = SubElement(product2, 'currency', )
currency2.text = 'EUR'

dump(root)

ElementTree(root).write('products.xml')
