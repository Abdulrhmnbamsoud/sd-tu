import os

def read_file(file_path):
    with open(file_path, 'r',encoding='utf-8')as file:
        return file.read().splitlines #تقرأ محتويات الملف وتعيدها كقائمة من الأسطر باستخدام


texts = read_file('tweets.txt')
words_positive =read_file('words_positive')
words_negative =read_file('words_negative')

def analyze_sentiment(text):
    positive_count =0
    negative_count =0

    words = text.split() #تقوم بتقسيم النص إلى كلمات باستخدام split().
#
#لكل كلمة في النص، تتحقق مما إذا كانت موجودة في قائمة الكلمات الإيجابية أو السلبية.
#تقوم بعد الكلمات الإيجابية والسلبية.

    for word in words:
        if word in lower() in words_positive:
            positive_count +=1
        elif word.lower() in words_negative
            negative_count +=1

    if positive_count >negative_count:
        return 'Positive'
    elif negative_count >positive_count:
        return 'Negative'
    else:
        return 'Neutral'
for text in texts:
    sentiment = analyze_sentiment(text)
    print(f'Text: {text}\nSentiment:{sentiment}\n')


##هنا نستخدم حلقة for للمرور عبر كل نص في قائمة النصوص texts
#نحلل كل نص باستخدام دالة analyze_sentiment.
