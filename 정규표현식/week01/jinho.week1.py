#1. Matching Specific String
import re
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

#2. Matching Digits & Non-Digit Characters
# \.이것은 점을 의미함 $은 문자열 종료?를 말하는걸로 알고있음.
import re
regex_pattern = r"...\....\....\....$"	# Do not delete 'r'.

#3.Matching Anything But a Newline
# 문제에서 x는 숫자,X는 문자라고했으니까
import re
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.


#4. Matching Whitespace & Non-Whitespace Character
import re
Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.
# 문제에서 \s:any whitespace character
#         \S:any non-whitespace character

#5. Matching Word & Non-Word Character
import re
Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

#6. Matching Start & End
import re
Regex_Pattern = r"^[0-9]\w\w\w\w\.$"	# Do not delete 'r'.
#문제조건1:숫자시작이므로 ^[0-9]
#문제조건2:x가 word character이므로 \w\w\w\w
#문제조건3:.으로 끝나야함 따라서 \.$를 해줬음.

#7.Matching Specific Characters
import re
Regex_Pattern = r'^[1|2|3][1|2|0][0|s|x][0|3|a|A][s|u|x][.|,]'
#or연산(|)하고 ^문자열시작이 핵심임

#8.Excluding Specific Characters
import re
Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'	# Do not delete 'r'.
#\D는 숫자가 아닌 것과 매치된다.


#9.Matching Character Ranges
import re
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.
# ^는 []안에서쓰이지않으면 문자열시작을 알리는것이 핵심이다.


#10.Matching Word Boundaries
import re
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'# Do not delete 'r'.
# The matched word can be of any length.
# 이런 조건이 있어서,, 마지막에 반복(*)을해주었다.아아아아아ㅏ아아아

#11.Capturing & Non-Capturing Groups
import re
Regex_Pattern = r'(ok){3,}'	# Do not delete 'r'.
# 문제에서 ok를 3번반복하라했으니까

#12 Alternative Matching
import re
Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]{1,}$'	# Do not delete 'r'.
# 일단 저 문자들로 시작한다했으니까 그룹핑한다음에 ^써줌
# 그리고 \.은 .을의미
# 마지막은 문자열 a-zA-Z니까저렇게써주고 1번이상이라고 문제에서 그랬으니까{1,}
# 그리고 문자열을 저렇게 종료해야되니까$


#13 Matching {x} Repetitions
import re
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579 \t\n\r\f\v]{5}$'	# Do not delete 'r'.
# 0도 짝수로치네,,

#14 Matching {x, y} Repetitions
import re
Regex_Pattern = r'^[123]{1,2}[a-zA-Z]{3,}\.{0,3}$'	# Do not delete 'r'.

#15 Matching Zero Or More Repetitions
import re
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.

#16 Matching One Or More Repetitions
import re
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.

#17 Matching Ending Items
import re
Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

# *는 0번부터 반복, +는 1번부터반복
# $는 뭘로 끝나야 한다. ^는 뭘로 시작해야 한다.
# \.은 .을 의미