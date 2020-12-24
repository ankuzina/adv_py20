#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = '^[a]{1}$'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^[a]{1}[abc]{1}[b]{1}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = '^[a-z]{5}\W[m]{1}[p]{1}[34]{1}$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '^[tvrnsz]{1,2}[aeuio]{1}[tvrnsz]{1,2}[aeuio]{1}[a-z]{1,3]$'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '^[ab]{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '^[A-Za-z]{6}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '^[Aa]{3}\s[Aa]{3}\s[Aa]{s}$'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = '^[^A1#]{0,4}$'