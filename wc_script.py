import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])



#Read text
text = open('test.csv', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wordcloud = WordCloud(font_path="/System/Library/Fonts/PingFang.ttc").generate(text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()