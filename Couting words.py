text = """Marco Rubio may be offered the role of secretary of state in the second Trump administration, two sources have told CBS, the BBC's US news partner.

However, while several US media outlets are reporting the Republican senator from Florida is in talks with the Trump transition team over the senior position, CBS reports that the nomination has not been finalised.

President-elect Trump may still change his mind about the top diplomatic position.

Rubio serves as the vice chairman of the Senate Intelligence Committee and sits on the Foreign Relations Committee.

His spokesperson has not responded to a request for comment."""

#print(text.split())

word_count = {}

for word in text.split ():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] +=1

print (word_count)

