import os
import sys

from hazm import *

genre_map = {"پرسش و پاسخ آنلاین حوزه خانواده": "تبادل نظر آنلاین", "تبادل نظر انلاین نی نی سایت": "تبادل نظر آنلاین",
             "تبادل نظر آنلاین-خانه‌داری": "تبادل نظر آنلاین", "نظرات سایت دیجی کالا": "نظرات سایت خرید",
             "نظرات سایت مشرق نیوز": "نظرات سایت‌های خبری", "انجمن علمی آموزشی": "تبادل نظر آنلاین",
             "تالار گفتگو مشاوره و روانشناسی": "تبادل نظر آنلاین", "تالار گفتگوی سیاسی": "تبادل نظر آنلاین",
             "تالار گفتگوی سیاسی و مذهبی": "تبادل نظر آنلاین", "نظرات ادبیات داستانی": "تبادل نظر آنلاین",
             "مشاوره و روانشناسی": "تبادل نظر آنلاین", "گفتمان مذهبی": "تبادل نظر آنلاین",
             "زیرنویس سریال": "فیلم و نمایش", "روانشناسی و مشاوره خانواده": "تبادل نظر آنلاین",
             "گفت و گوی تلگرامی": "گفت و گوی تلگرامی", "کودک و نوجوان- ترجمه": "کودک و نوجوان- ترجمه",
             "رمان ترجمه": "رمان ترجمه", "رمان تألیفی": "رمان تألیفی", "وبلاگ": "وبلاگ",
             "نظرات سایت‌های خبری": "نظرات سایت‌های خبری", "وبلاگ- کودک": "وبلاگ", "فیلم‌نامه": "فیلم و نمایش",
             "نمایشنامه": "فیلم و نمایش"}
input_file = os.path.abspath(sys.argv[1])
output_file = os.path.abspath(sys.argv[2])
output_tok_file = os.path.abspath(sys.argv[3])

normalizer = Normalizer()

with open(input_file, "r") as r, open(output_file, "w") as w, open(output_tok_file, "w") as tw:
    for line in r:
        line = line.strip().replace("\r", "").replace("*", "")
        spl = line.split("\t")
        if len(spl[2]) == 0:
            spl[2] = spl[1]
        if len(spl) < 5:
            spl.append("-")
        if len(spl[4]) == 0:
            spl[4] = "-"
        spl[3] = genre_map[spl[3].strip()]
        columns = [normalizer.normalize(s) for s in spl[:3]] + spl[3:]
        columns_tok = [" ".join(word_tokenize(s)).replace("_", " ") for s in columns[:3]] + columns[3:]
        w.write("\t".join(columns) + "\n")
        tw.write("\t".join(columns_tok) + "\n")
