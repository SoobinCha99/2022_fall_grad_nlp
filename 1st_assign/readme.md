다음의 조건을 만족하는 n_gram(text, n) 함수를 작성하여 py 파일로 제출하시오.

문자열 text를 인자로 받아 n-gram 리스트를 리턴
n은 text의 어절 수보다 적다고 가정
ngram.py 파일에 구현하여 icampus에 제출. 외부 패키지 사용 없이 표준 파이썬만 사용할 것
 

실행 예제 

stext = "Colaboratory(또는 줄여서 'Colab')를 사용하면 브라우저에서 Python을 작성하고 실행할 수 있습니다."

ngrams = n_gram(stext,4)

print(ngrams)

===== 결과 =====

[" Colaboratory(또는 줄여서 'Colab')를 사용하면", " 줄여서 'Colab')를 사용하면 브라우저에서", " 'Colab')를 사용하면 브라우저에서 Python을", ' 사용하면 브라우저에서 Python을 작성하고', ' 브라우저에서 Python을 작성하고 실행할', ' Python을 작성하고 실행할 수', ' 작성하고 실행할 수 있습니다.']