# my_str = "Hello! My name is Vivek and I am learning python language."
my_str = input("Enter your text here : ")

count = {}

for i in my_str:
	if i in count:
		count[i] += 1
	else:
		count[i] = 1

print(count)
