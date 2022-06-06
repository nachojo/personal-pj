#QUIZ Generating password program for each sites.
'''
for example) http://naver.com
rule1 : exclude http:// => naver.com
rule2 : exclude after dot(.) => naver
rule3 : first three digits of remaining letters(nav) + number of letters(5) + number of 'e'(1) + "!"

example : "/'http://naver.com/' password generated : nav51!"
'''

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] #(0-4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} password generated : {1}" .format(url, password))
