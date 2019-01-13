import randm

def hangman(word):
    i = 1
    stages =["",
             "~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
             "______________      ",
             "|            |      ",
             "|            0      ",
             "|            |      ",
             "|           /|\     ",
             "|            |      ",
             "|           / \     ",
             "|                   "]
    hitomozi = list(word) #答えの文字を一文字ずつにリスト化
    kotaeawase = ["_"]*len(word) #答えの文字を_に変換。答えの文字数だけ。
    win = False
    print("ようこそ。ハングマンへ。")

    while i<len(stages): #繰り返し。stagesのリストの回数だけ。
        print("\n")
        kaitou=input("答えに含まれる文字を一文字ずつ入力して。\n"+"".join(kotaeawase)+"\n")
        if kaitou in hitomozi:
            mozibangou = hitomozi.index(kaitou)
            kotaeawase[mozibangou] = kaitou
            hitomozi[mozibangou] = "$"
        else:
            i+=1
        print("".join(kotaeawase))
        print("\n".join(stages[0:i]))

        if "_" not in kotaeawase:
            print("あなたのかち 答えは{}".format("".join(kotaeawase)))
            print("{}回の回答で正解したよ！!".format(i+len(word)-1))
            win = True
            break
    if not win:
        print("\n\n\n")
        print("あなたの負け 答えは{}".format(word))
        print("\n".join(stages[0:i]))
        print("ぶらーん・・・ぶらーん・・・")


words=["cat","dog","take"]
word=words[random.randrange(len(words))]
hangman(word)
    
