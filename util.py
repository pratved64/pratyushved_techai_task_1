class Color:
    GRAY = 100
    GREEN = 102
    YELLOW = 43
    BLACK = 40
    WHITE = 97

    @staticmethod
    def background(code):
        # 40 and 47, 100 and 107
        return "\33[{code}m".format(code=code)

    @staticmethod
    def style_text(code):
        # 0 and 8
        return "\33[{code}m".format(code=code)

    @staticmethod
    def color_text(code):
        # 30 and 37, 90 and 97
        return "\33[{code}m".format(code=code)

    @staticmethod
    def reset():
        return "\033[0m"

    @staticmethod
    def style(bg, style, text):
        return "\33[{style};{text};{bg}m".format(style=style, bg=bg, text=text)

class Score:
    def __init__(self, fpath):
        self.fpath = fpath
        with open(fpath, 'a+') as scoreFile:
            scoreFile.seek(0)
            content = scoreFile.read()
            if content == '':
                scoreFile.write('0')
                self.score = 0
            else:
                self.score = int(content)

    def increment(self):
        with open(self.fpath, 'w') as scoreFile:
            scoreFile.write(str(self.score + 1))
            self.score += 1


    
if __name__ == "__main__":
    # for i in range(100, 108):
    #     example = Color.background(i) + "{i} ".format(i=i)
    #     print(example, end=Color.reset())
    # print()
    # for i in range(40, 48):
    #     example = Color.background(i) + "{i} ".format(i=i)
    #     print(example, end=Color.reset())
    sc = Score("score.txt")
    print(sc.score)
    sc.increment()