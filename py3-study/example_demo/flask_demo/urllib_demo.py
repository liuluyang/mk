
from urllib.parse import quote, unquote, urlencode, urljoin


print(urlencode({'a':'发'}))

print(quote('发'))
print(unquote('a=%E5%8F%91'))

print(urljoin('http://www.baidu.com', 's?w=1'))