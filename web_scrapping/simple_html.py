from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html>
<head></head>
<body>
<h1>Akshat Parakh</h1>
<p> My name is Akshat</p>

<ul>
    <li>1.</li>
    <li>2.</li>
    <li>3.</li>
    <li>4.</li>
</ul>

</body>
</html>
'''


simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')
print(simple_soup.find('h1'))
print(simple_soup.find('h1').string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    [str(item) for item in list_items]
    print(list_items)
    
    
find_list_items()
    
def find_subtitle():
    paragraph = simple_soup.find('p')
    print(paragraph.string)
    
find_subtitle()
