# 先安装lxml
# 用 lxml 来解析HTML代码

from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="0.html">item 0 </a></li>
        <li class="item-1"><a href="1.html">item 1 </a></li>
        <li class="item-2"><a href="2.html">item 2 </a></li>
        <li class="item-3"><a href="3.html">item 3 </a></li>
        <li class="item-4"><a href="4.html">item 4 </a></li>
        <li class="item-5"><a href="5.html">item 5 </a></li>
    </ul>     
</div>
'''

# 利用 etree.HTML 把字符串解析成 HTML 文件
html = etree.HTML(text)
s = etree.tostring(html).decode()

print(s)