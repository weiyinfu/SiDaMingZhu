"""
把行进行合并，只要处于同一个章回，同一个段落，如果结尾不为。！，则进行merge
"""
import os

import re
from typing import List


def split_by_pos(content: str, splitters: List[int]) -> List[str]:
    """
    对content按照splitter进行切分，切分成若干部分，每一部分都是一篇文章

    :param content:
    :param splitters:
    :return:
    """
    splitters = sorted(splitters)
    if splitters[0] != 0:
        splitters.insert(0, 0)
    if splitters[-1] != len(content):
        splitters.append(len(content))
    a = []
    for i in range(0, len(splitters) - 1):
        a.append(content[splitters[i]:splitters[i + 1]])
    return a


def get_pos(res: List[re.Match]):
    """
    把res映射成int列表

    :param res:
    :return:
    """
    beg_list = []
    for i in res:
        beg = i.start()
        beg_list.append(beg)
    return beg_list


def get_parts(content: str):
    a = re.finditer('\n\s*第[一二三四五六七八九十1234567890]+[章回](.+?)?\n', content)
    splitters = get_pos(a)
    s = split_by_pos(content, splitters)
    return s


def merge_lines(s: str):
    # s是一个章回
    s = s.strip()
    lines = [i.strip() for i in s.splitlines()]
    ans = [lines[0]]
    last_end = True
    for i in lines[1:]:
        if last_end:
            ans.append(i)
        else:
            ans[-1] += i
        if i:
            if i[-1] in "：。！？":
                last_end = True
            else:
                last_end = False
    return '\n'.join(ans)


def handle(s: str):
    s = get_parts(s)
    for i in range(len(s)):
        s[i] = merge_lines(s[i])
    return '\n'.join(s)


for i in os.listdir('src'):
    filepath = os.path.join('src/' + i)
    content = open(filepath).read()
    content = handle(content)
    open(filepath, 'w').write(content)
