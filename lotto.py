import random

numbers = range(1,46)
# 마치 [1,2,3,...,45] 과 비슷하다
# 배열은 아님

# alt + shift + up/down
# alt + up/down

# 중복 없이
lotto = random.sample(numbers,6)
print(sorted(lotto))