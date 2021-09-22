import xml.etree.ElementTree as ET

#Single child tag
###Sample XML format as an example.  would actually get it from the web to parse
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
     </phone>
     <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) #.text = just get me the text
print('Attr:', tree.find('email').get('hide')) # find attr of 'hide'

####Multiple child tags
import xml.etree.ElementTree as ET

###Stuff is the manully created xml data for the example
input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x ="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input) # creates a xnl tree object to parse
lst = stuff.findall('users/user') #findall is used for trees with Multiple childs
## users/user =  finds all user tags (not the text) under "users"
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attributes', item.get(".x"))
