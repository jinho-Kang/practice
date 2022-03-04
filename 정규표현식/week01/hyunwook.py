# 2월 28일
#1. **Matching Specific String**
Regex_Pattern = r'hackerrank'

#2. **Matching Anything But a Newline**
""" ^로 시작점 작성후
 임의의 1자리(.) * 3 + (. + 임의의 3자리(. * 3)) * 3
 $로 종료점 작성하여 xxx.xxx.xxx.xxx 형태 유지
"""
regex_pattern = r"^.{3}(\..{3}){3}$"

#3. **Matching Digits & Non-Digit Characters**
"""
xxXxxXxxxx
x = 숫자
X = 숫자가 아닌 것 이므로
(xxX) * 2 + x * 4
"""
Regex_Pattern = r"(\d\d\D){2}\d{4}"

# 3월 1일
#1. **Matching Whitespace & Non-Whitespace Character**
"""
XXxXXxXX
x = 공백문자
X = 공백문자가 아닌 것 이므로
X * 2 + (xXX) * 2
"""
Regex_Pattern = r"\S{2}(\s\S\S){2}"

#2. **Matching Word & Non-Word Character**
"""
xxxXxxxxxxxxxxXxXxXx
x = 알파벳 + 숫자 + _ 중 하나
X = x 아닌 것
"""
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"

#3. **Matching Start & End**
"""
^는 시작, $는 끝
xyyyy
x = 숫자
y = 알파벳 + 숫자 + _ 중 하나
"""
Regex_Pattern = r"^\d\w{4}\.$"

# 3월 2일
#1. **Matching Specific Characters**
"""
첫번째문자 1,2,3중하나
두번째 1,2,0중하나
세번째 x,s,0
네번째 3 0 A a
다섯번째 x s u
여섯번째 . 이나 ,
"""
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
#2. **Excluding Specific Characters**
"""
첫번째 0부터 9 아님 숫자아님
두번째 aeiou 아님
세번째 bcDF 아님
네번째 공백문자 아님
다섯번째 AEIOU 아님
여섯번째 ., 아님
"""
Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'
#3. **Matching Character Ranges**
"""
문자열의 길이가 5보다 커야하므로 앞5글자 이후에는 제한을 두지 않음
첫번째 a부터 z
두번째 1부터 9
세번째 a부터 z 아님
네번째 A부터 Z 아님
다섯번째 A부터 Z
"""
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

# 3월 3일
#1. **Matching Word Boundaries**
"""
\b는 경계, 범위? 를 지정하기 위해 사용함
첫문자가 모음으로 시작하는 문자가 있는지 확인
"""
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
#2. **Capturing & Non-Capturing Groups**
"""
( )를 통해 문자를 그룹설정함
ok가 3번이상 반복
"""
Regex_Pattern = r'(ok){3,}'	
#3. **Alternative Matching**
"""
| 는 or 연산
[a-zA-Z]가 1번이상 반복
"""
Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'

# 3월 4일
#1. **Matching {x} Repetitions**
"""
앞뒤 글자수 제한
정해진 조건에 대해 40번 반복
5번반복
"""
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
#2. **Matching {x, y} Repetitions**
"""
앞뒤 글자수 제한
1~2번 반복
3번이상 반복
0~3번 반복(0은 생략가능)
"""
Regex_Pattern = r'^\w{1,2}[a-zA-Z]{3,}\W{,3}$'
#3. **Matching Zero Or More Repetitions**
"""
앞뒤 글자수 제한
2번이상 반복
* -> 0번또는 그이상 반복
"""
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'
#4. **Matching One Or More Repetitions**
"""
+ 앞의 문자는 1번이상 반복
"""
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'
#5. **Matching Ending Items**
"""
앞의 그룹문자 0번 또는 그이상반복
마지막문자 s
"""
Regex_Pattern = r'^[a-zA-Z]*s$' 