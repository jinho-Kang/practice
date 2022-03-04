// 2월 28일
// 1.
var Regex_Pattern = /hackerrank/;

// 2. xxx.xxx.xxx.xxx
var Regex_Pattern = /^.{3}(\..{3}){3}$/g;

// 3. xxXxxXxxxx x는 숫자, X는 숫자가 아닌 문자
var Regex_Pattern = /(\d\d\D){2}\d{4}/;


// 3월 1일
// 4.  XXxXXxXX  x는 공백문자, X는 공백이 아닌 문자
var Regex_Pattern = /(\S\S\s){2}\S\S/;

// 5.  xxxXxxxxxxxxxxXxxx x는 문자 X는 문자가 아닌것. 
var Regen_Pattern = /\w{3}\W\w{10}\W\w{3}/ 

// 6.  Xxxxx  X는 숫자여야하고, x는 모든문자 .로 끝나야 한다.
var Regex_Pattern = /^\d\w{4}\.$/;


// 3월 2일 
// 7. 길이가 6개, 1번째 [123], 2번째 [120], 3번째 [xs0], 4번째 [30Aa], 5번째 [xsu], 6번째 [.,]
var Regex_Pattern = /^[123][120][xs0][30Aa][xsu][.,]$/;

// 8. 길이가 6개, 1번째가 숫자x, 2번째 [^aeiou], 3번째 [^bcDF] 4번째 [\W] 5번째 [^AEIOU] 6번째 [^.,] 
var Regex_Pattern = /^[\D][^aeiou][^bcDF][^\W][^AEIOU][^.,]$/;

// 9. 길이가 5이하, 1번째 소문자알파벳, 2번째 양수 숫자, 3번째 소문자x, 4번째 대문자x, 5번째 대문자 
var Regex_Pattern = /^[a-z][1-9][^a-z][^A-Z][A-Z]/
