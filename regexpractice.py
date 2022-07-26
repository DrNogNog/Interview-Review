import re
#print(re.search('<[^/>][^>]*>', '<table>'))
#print(re.search('</[^>]*>', '</table>'))
#re.search('<[^/>][^>]')
#re.search('</[^>]+>','</table>')
#print(re.search('<[^/>]+/>','<br />'))

#print(re.findall("[\w]+", "a b c d e f g h i j k l m n o p"))
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
#import urllib.request
#with urllib.request.urlopen('https://www.w3resource.org') as x:
#    html = x.read()
#    x.close()
#    print("open tags")
mon = re.search(r'(?P<hello>\d{4})-(?P<me>\d{2})','2018-23')
print(mon.group('hello'))
print(mon.group('me'))

date = r'2018-09-01'
print(re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1/',date))
#1 = Year, 2 = Month, 3 = Day

{
 "_id" : ObjectId("6014dc988c628fa57a508088"),
 "Age" : "Middle",
 "Gender" : "Male",
 "OwnHome" : "Rent",
 "Married" : "Single",
 "Location" : "Close",
 "Salary" : 63600,
 "Children" : 0,
 "History" : "High",
 "Catalogs" : 6,
 "AmountSpent" : 1318
}
db.marketing.find().limit(1).pretty()
db.marketing.find( {"Children": 1}).limit(1).pretty()

