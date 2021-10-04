def reversevowels(s):
    li = []
    result = list(s)
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
            li.append(i)

    end = 1

    for i in range(int(len(li)/2)):
        result[li[i]], result[li[-end]] = result[li[-end]], result[li[i]]

        end += 1
    return "".join(map(str, result))


if __name__ == "__main__":
    print(reversevowels("hello"))
    print(reversevowels("leetcode"))
