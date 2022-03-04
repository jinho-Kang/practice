#2주차 정규표현식
#1. Branch Reset Groups -> 해당 언어가 없어서 스킵

#2. Matching Same Text Again & Again
Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'
#3. Backreferences To Failed Groups
Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"
#4. Forward References -> 파이썬은 스킵, 자바는 풀이 진행

#5. Positive Lookahead
Regex_Pattern = r'o(?=oo)'
#6. Negative Lookahead
Regex_Pattern = r"(.)(?!\1)"
#7. Positive Lookbehind
Regex_Pattern = r"(?<=[13579])\d"
#8. Negative Lookbehind
Regex_Pattern = r"(?<![aeiouAEIOU])."