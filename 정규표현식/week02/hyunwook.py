#2주차 정규표현식
#1. Branch Reset Groups -> 해당 언어가 없어서 스킵

#2. Matching Same Text Again & Again
"""
20글자를 위해 앞뒤에 ^와 $ c처리를 하고 20글자의 표현식을 작성하였고 조건에 따라
1캐릭터: lowercase letter.
2캐릭터: word character.
3캐릭터: whitespace character.
4캐릭터: non word character.
5캐릭터: digit.
6캐릭터: non digit.
7캐릭터: uppercase letter.
8문자: letter(소문자 또는 대문자).
9문자: vowel(a, e, i , o , u, A, E, I, O 또는 U).
10캐릭터: non whitespace character.
11문자: 와 같아야 합니다 1st character.
12문자: 와 같아야 합니다 2nd character.
13문자: 와 같아야 합니다 3rd character.
14문자: 와 같아야 합니다 4th character.
15문자: 와 같아야 합니다 5th character.
16문자: 와 같아야 합니다 6th character.
17문자: 와 같아야 합니다 7th character.
18문자: 와 같아야 합니다 8th character.
19문자: 와 같아야 합니다 9th character.
20문자: 와 같아야 합니다 10th character.
"""
Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'
#3. Backreferences To Failed Groups
"""
8자리구성을 위해 ^ $ 처리
-가 들어갈 수도 있고 안들어갈수도 있어서 ?처리로 들어가면 다들어가고
안들어가면 안들어가게 처리
"""
Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"
#4. Forward References -> 파이썬은 스킵, 자바는 풀이 진행

#5. Positive Lookahead
"""
o문자 다음에 oo문자가 나오는 횟수
"""
Regex_Pattern = r'o(?=oo)'
#6. Negative Lookahead
"""
임의의 한자리수 문자표현, 뒤에 오는 문자와 일치하지 않는 것 카운트
"""
Regex_Pattern = r"(.)(?!\1)"
#7. Positive Lookbehind
"""
숫자이고 앞자리가 홀수인 숫자가 나오는 카운트
"""
Regex_Pattern = r"(?<=[13579])\d"
#8. Negative Lookbehind
"""
임의의 한자리수 문자이고 그 앞에 영어 모음이 나오지 않는 카운트
"""
Regex_Pattern = r"(?<![aeiouAEIOU])."