public class Gohome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
	/*	1. **Matching Anything But a Newline**

		 → tester.check("...\\....\\....\\....");

		 . << 문자 한자리. \\. << .을 문자로 사용하겠다.

		3자리 . 3자리 . 3자리 . 3자리 입력마스크.

		2. **Matching Digits & Non-Digit Characters**

		→ tester.checker("\\d{2}\\D\\d{2}\\D\\d{4}"); 

		3. **Matching Specific String**

		→ tester.checker("hackerrank");

		---

		---

		1. **Matching Whitespace & Non-Whitespace Character**

		→ tester.checker("\\S{2}\\s{1}\\S{2}\\s{1}\\S{2}"); // Use \\ instead of

		/* 문자2개 공백1개

		2. **Matching Word & Non-Word Character**

		→ tester.checker("\\w{3}\\.\\w+\\.\\w{3}"); // Use \\ instead of using \

		주소3개 + . + 중간에 문자 수 개 + . 

		3. **Matching Start & End**

		→ tester.checker("^\\d{1}\\w{4}[.]{1}$"); // Use \\ instead of using \

		---

		---

		1. **Matching Specific Characters**

		→ tester.checker("^[123][120][xs0][30Aa][xsu][\\.,]$"); // Use \\

		 /* [abc]는 abc중에 있다라는 뜻.  그냥 .은 한 문자를 뜻하므로 \\. 으로 .을 문자로 쓴다는 것을 명시.

		2. **Excluding Specific Characters** 

		 → tester.checker("^[^\\d][^aeiou][^bcDF][^\\s][^AEIOU][^\\.,]$"); // Use \\ instead of using \

		3. **Matching Character Ranges**

		 → tester.checker("^[a-z][1-9][^a-z][^A-Z][A-Z].*"); // Use \\ instead of using \

		 /* ^는 문자열이 시작되었음을 알려줌 /  . * << 문자가 수 개 반복된다.
		
		 ============================================================================================

         1. **Matching Word Boundaries**

		tester.checker("\\b[aeiuoAEIOU][a-zA-z]*\\b"); // Use \\ instead of using \

		→ 맨 앞 글자는 대소문자 모음, 이후엔 알파벳이 수 개 올 것, 앞뒤 문자 경계 줄 것

		2. **Capturing & Non-Capturing Groups**

		tester.checker("(ok){3,}"); // Use \\ instead of using \

		→ ok가 최소 3개 . ( )에 넣으면 한 문자로 취급 ok, {3,} 최소 3개.

		3. **Alternative Matching**

		tester.checker("^(Mr|Mrs|Ms|Dr|Er)\\.[A-Za-z]+$"); // Use \\ instead of using \

		→ 문자 ^ $안에 넣어줘야하는 조건을 잘 모르겠음.

		-------------------------------------------------------------------------------------------
		-------------------------------------------------------------------------------------------
1. **Matching {x} Repetitions**

tester.checker("^[a-zA-Z02468]{40}[13579\\s]{5}$");

- must be of length equal to **`45`**.
- The first  characters should consist of **`letters`**(both lowercase and uppercase), or of **`even digits`**.
- The last  characters should consist of **`odd digits`** or **`whitespace characters`**.

2. **Matching {x, y} Repetitions**

tester.checker("^\\d{1,2}[a-zA-Z]{3,}\\.{0,3}$"); // Use \\ instead of using \

- should begin with  or  **`digits`**.
- After that,  should have  or more **`letters`** (both lowercase and uppercase).
- Then  should end with up to  **`.`** symbol(s). You can end with  to  `.` symbol(s), inclusively.

3. **Matching Zero Or More Repetitions**

tester.checker("^\\d{2,}[a-z]*[A-Z]*$"); // Use \\ instead of using \

- should begin with  or more **`digits`**.
- After that,  should have  or more **`lowercase letters`**.
- should end with  or more **`uppercase letters`**

4. **Matching One Or More Repetitions**

tester.checker("^\\d+[A-Z]+[a-z]+$"); // Use \\ instead of using \

- should begin with  or more **`digits`**.
- After that,  should have  or more **`uppercase letters`**.
- should end with  or more **`lowercase letters`**.

5. **Matching Ending Items**

tester.checker("^[a-zA-Z]*s$"); // Use \\ instead of using \

- should consist of only lowercase and uppercase letters (no numbers or symbols).
- should end in `s`.
		*/


	}

}