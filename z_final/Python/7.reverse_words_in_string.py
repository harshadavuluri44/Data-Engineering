text = "Data Engineering Interview at Siemens"

words = text.split(' ')

reverse_words = [x[::-1] for x in words]

f = ' '.join(reverse_words)
print(f)
