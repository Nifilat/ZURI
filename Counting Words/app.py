
given_text = "I am so excited to be a recipient of the I4G X Zuri internship"
list_of_words = given_text.split()
text_count = len(list_of_words)


print(list_of_words)
print(text_count)


score = int(input("Enter your score here"))


if score < 40:
    print('FAIL')

elif score >= 40 or score <= 55:
    print('PASS')

elif score >= 55 or score < 70:
    print('MERIT')

elif score >= 70:
    print('Distinction')
