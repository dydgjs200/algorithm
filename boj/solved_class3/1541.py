# 적절한 괄호로 최소값 만들기
# 중첩 괄호 고려 필요 x (덧셈, 뺄셈만이여서)

import re

inp = input()
num = re.findall(r'\d+', inp)
operator = re.findall(r'[-+]', inp)

