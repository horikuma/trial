#!/usr/bin/env python3

from lark import Lark

program = open('program.txt').read()
rule = open('sip.lark').read()

# 文法規則をパーサジェネレータに渡してパーサを生成(字句解析もやってくれる)
parser = Lark(rule, start='generic_message', parser='lalr')

# プログラムを字句解析＆構文解析
tree = parser.parse(program)

print(tree.pretty())
