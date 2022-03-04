// 1.
var Regex_Pattern = /hackerrank/;

// 2. xxx.xxx.xxx.xxx
var Regex_Pattern = /^.{3}(\..{3}){3}$/g;

// 3. xxXxxXxxxx x는 숫자, X는 숫자가 아닌 문자
var Regex_Pattern = /(\d\d\D){2}\d{4}/;

// 4.  XXxXXxXX  x는 공백문자, X는 공백이 아닌 문자
var Regex_Pattern = /(\S\S\s){2}\S\S/;

// 5.  xxxXxxxxxxxxxxXxxx x는 문자 X는 문자가 아닌것. 
var Regen_Pattern = /\w{3}\W\w{10}\W\w{3}/ 

// 6.  Xxxxx  X는 숫자여야하고, x는 모든문자 .로 끝나야 한다.
var Regex_Pattern = /^\d\w{4}\.$/;

