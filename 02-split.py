"""
把out.txt切分开
"""
book = """
西游记
水浒全传
三国演义
红楼梦
""".split()
book = [i for i in book if i]
print(book)
s = open('out.txt').read()
book_index = []
s = s[s.index('红楼梦') + 4:].strip()
for i in book:
    book_index.append(s.index(i))
assert book_index[0] == 0
book_index.append(len(s))
for ind, i in enumerate(book):
    beg, end = book_index[ind], book_index[ind + 1]
    content = s[beg:end]
    start = content.index('第一回')
    start = content.index('第一回', start + 3)
    content = content[start:]
    open(f'src/{i}.txt', 'w').write(content)
