import re

text = r"When my time comes, forget the wrong that I've done, help me leave behind some reasons to be missed.\
       And don't resent me, when you're feeling empty, keep me in your memory,  \
       leave out all the rest, leave out all the rest.  \
       Forgetting all the hurt inside you've learned to hide so well.  \
       Pretending someone else can come and save me from myself. \
       I can\'t be who you are, I can\'t be who you are "



but_what_if_they_are_chinese_characters = r"垂死病中惊坐起，笑问客从何处来。我是一只猫猫，猫猫喵喵猫猫喵,躺在地上一整天，每日沐足笑开颜"

comb = text + but_what_if_they_are_chinese_characters
comb += '1ce upon a tim3, 有一个女孩名叫huaweirongyao，生于19840427'

tc = re.findall(r'[a-zA-Z0-9{4,6}\u4e00-\u9fa5]', comb)
print(tc)