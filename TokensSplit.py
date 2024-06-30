import os
import glob
txt_folder = "pixiv\pixiv_top50_moat"#文件名 该文件下所有txt文件均认为是标签文件
#默认标签文件使用 ', '分割

txt_files = glob.glob(os.path.join(txt_folder, "*.txt"))
all_labels = {}
for txt_file in txt_files:
    with open(txt_file, "r") as f:
        text = f.read().strip().split(", ")
        for i in text:
            try:
                all_labels[i] += 1
            except KeyError:
                all_labels[i] = 1

num=0
labels=[]
for key,value in all_labels.items():
    if value<=1000:#出现次数低于1000的标签不作为标签
        num+=1
    else:
        labels+=[key]

print(num)#输出被排除的标签数量
print(len(labels))#输出最终选定的标签数量
with open("tokens.txt", "w") as f:
    for label in labels:
        f.write(label + "\n")