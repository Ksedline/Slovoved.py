import random as r
import string as s

# Размер матрицы
i,j = 16,16

# Генерим матрицу 
buff = s.ascii_uppercase
matrix = [[buff[r.randint(0, len(buff)-1)] for y in range(i)] for x in range(j)]

# Вывод матрицы
for i in range(j):
    print(matrix[i])
    pass
	
	
words = ["test", "wild", "hello", "world", "word", "mississisipi", "shit", "Ksed", "Line"]	


for i in range(j):
    pull = r.randint(0, len(words)-1)
    arraySize = len(matrix[i])
    wordSize = len(words[pull])
    word = words[pull]
    word = word.upper()
    if wordSize > arraySize:
        continue
        
    maxPos = arraySize - wordSize
    wordPos = r.randint(0, maxPos)

    l = wordPos - 1
    for k in range(0, wordSize):
        l += 1
        matrix[i][l] = word[k]  
        pass
    
    print('row: ' + str(i+1) + '; word: ' + word + '; wordSize ' + str(wordSize) + '; wordPos: ' + str(wordPos) + '; maxPos: ' + str(maxPos))
    pass


# Вывод измененной матрицы 
print()
res = ""
for i in range(j):
    for l in range(len(matrix[i])):
        res += matrix[i][l] + " "
        pass
    res += '\n'
    pass
    
print(res)