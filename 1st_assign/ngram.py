sample_text = "Colaboratory(또는 줄여서 'Colab')를 사용하면 브라우저에서 Python을 작성하고 실행할 수 있습니다."
n=4

def list2String(str_list):
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()

def n_gram(sample_text,n):
    n_gram_list = [] 
    word_list = sample_text.split() 
    start = 0 
    end = n 
    for i in range(len(word_list)-n+1): 
        n_gram = word_list[start:end]
        n_gram = list2String(n_gram)
        n_gram_list.append(n_gram)
        start = start + 1
        end = end + 1
    print(n_gram_list)

if __name__ == "__main__":
    n_gram(sample_text,n)