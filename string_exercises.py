##with open('positive.txt') as f:
##    positive_data = f.read()
##
##with open('negative.txt') as f:
##    negative_data = f.read()
##
##positive_words = positive_data.split('\n')
##
##negative_words = negative_data.split('\n')
##
##text = input("Enter some text: ")
##
##words = text.split()
##
##positive_count = 0
##
##negative_count = 0
##
##for word in words:
##    if word in positive_words:
##        positive_count += 1
##    if word in negative_words:
##        negative_count += 1
##
##if positive_count > negative_count:
##    print("The text is positive.")
##elif negative_count > positive_count:
##    print("The text is negative.")
##else:
##    print("The text is neutral.")

