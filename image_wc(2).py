
text = open('test.csv', mode='r', encoding='utf-8').read()
text[0:500]

import jieba
text = ' '.join(jieba.cut(text))
text[0:500]

from PIL import Image
import numpy as np
icon_path = 'panda.png'
icon = Image.open("/Users/ashleyallocca/Documents/pantsless_wc/cn_lag.png")
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

from wordcloud import ImageColorGenerator
color_func = ImageColorGenerator(mask)

font_path = ("/System/Library/Fonts/PingFang.ttc")

from wordcloud import WordCloud
import matplotlib.pyplot as plt


wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=mask, max_font_size=300, random_state=1)
wc.generate_from_text(text)
wc.recolor(color_func=color_func, random_state=2)

output_path = 'wordcloud1.png'

plt.rcParams["figure.figsize"] = (25,25)
plt.imshow(wc)
plt.axis("off")
plt.show()