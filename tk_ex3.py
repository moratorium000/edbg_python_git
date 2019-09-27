import tkinter as tk
from tkinter import ttk, Frame, Canvas, Tk, mainloop



class Omok():
    def __init__(self):
        self.coord = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # 19* 19 바둑판 좌표
        self.count = 0
        #odd even count

        self.mult_check = []
        #중복 바둑돌 체크

        self.winner_winner = False
        # 승리 조건 카운트

    def badukpan(self):
        str_badukal = list(map(lambda x: ' '.join([str(y) for y in x]), self.coord))
        h = '\n'.join(str_badukal)
        # 바둑판 형태의 str

        self.graphic_badukpan_str = h.replace("0","┼").replace("1","○").replace("2","●")
        return self.graphic_badukpan_str


    def pos_selec(self):
        # 좌표 지정

        self.new_coord = eval(input("input coord"))
        if self.new_coord in self.mult_check:
            print("wrong input")
            self.pos_selec(self)
        if self.count % 2 == 0:
            self.coord[self.new_coord[0]][self.new_coord[1]] = 1
            self.count += 1
            print("black")
        elif self.count %2 == 1:
            self.coord[self.new_coord[0]][self.new_coord[1]] = 2
            self.count += 1
            print("white")
        self.mult_check.append(self.new_coord)
        #홀짝 결정

        self.winning_condition()


    def winning_condition(self):
        #승리조건 확인 개꼬임ㅎㅎ

        if type(self.new_coord) == tuple:
            self.row, self.column = self.new_coord
        #타입에러방지

        self.check_space = [x[self.column-4 if self.column > 3 else 0:self.column+5] for x in self.coord[self.row-4 if self.row > 3 else 0:self.row+5]]
        #9*9 공간 형성, 단 중앙공간에 있을 경우만

        if self.count %2 ==1:
            char_white_or_black = "11111"
        elif self.count %2 ==0:
            char_white_or_black = "22222"
        #홀짝 체크용

        if self.new_coord in [(x, y) for x in range(4, 15) for y in range(4, 15)]:
            # general하게 중앙 공간에 있을 경우만
            r = self.check_space[4]
            finding_string_row = ''.join([str(x) for x in r])
            c_r = finding_string_row.find(char_white_or_black)
            #가로로 조건확인 str로 만들어버리기@@

            c = [x[4] for x in self.check_space]
            finding_string_column = ''.join([str(x) for x in c])
            c_c = finding_string_column.find(char_white_or_black)
            # 세로로 조건확인 마찬가지로 str

            rs = [] #사선 \
            for pos, val in enumerate(self.check_space):
                rs.append(val[pos])
            finding_string_rev_sl = ''.join([str(x) for x in rs])
            c_rs = finding_string_rev_sl.find(char_white_or_black)
            # 사선 조건확인

            s = [] # 사선 /
            for pos, val in enumerate(self.check_space):
                s.append(val[-pos-1])
            finding_string_sl = ''.join([str(x) for x in s])
            c_s = finding_string_sl.find(char_white_or_black)
            #사건 조건확인2

            if set([c_r, c_c, c_s, c_rs]) != {-1}:
                #하나라도 승리조건일 경우
                print("winner_winner?")
                self.winner_winner = True

        else:# self.new_coord[0] in range(4, 15) and self.new_coord[1] in range(4, 15) == False:
            bumper = [0]*4
            bumper_top = [0]*27
            # bumper 은 [0000000000000] 같은 외곽의 허공간을 형성
            self.new_check_coord= [bumper_top]*4 +[bumper + x + bumper for x in self.coord] + [bumper_top]*4
            self.new_coord_modified = self.new_coord[0] + 4, self.new_coord[1] +4
            # 9*9 공간 만들기 위해 coord 의 앞, 뒤, 열 , 행에 0000으로 이루어진 공간 생성

            self.ncolumn, self.nrow = self.new_coord_modified
            # 좌표도 selec으로 지정한 좌표에서 변화

            self.check_space = [x[self.ncolumn-4:self.ncolumn+5] for x in self.new_check_coord[self.nrow-4:self.nrow+5]]
            r = self.check_space[4]
            finding_string_row = ''.join([str(x) for x in r])
            c_r = finding_string_row.find(char_white_or_black)
            #가로로 조건확인 str로 만들어버리기@@

            c = [x[4] for x in self.check_space]
            finding_string_column = ''.join([str(x) for x in c])
            c_c = finding_string_column.find(char_white_or_black)
            # 세로로 조건확인 마찬가지로 str

            rs = [] #사선 \
            for pos, val in enumerate(self.check_space):
                rs.append(val[pos])
            finding_string_rev_sl = ''.join([str(x) for x in rs])
            c_rs = finding_string_rev_sl.find(char_white_or_black)
            # 사선 조건확인

            s = [] # 사선 /
            for pos, val in enumerate(self.check_space):
                s.append(val[-pos-1])
            finding_string_sl = ''.join([str(x) for x in s])
            c_s = finding_string_sl.find(char_white_or_black)
            #사건 조건확인2

            if set([c_r, c_c, c_s, c_rs]) != {-1}:
                #하나라도 승리조건일 경우
                print("winner_winner?")
                self.winner_winner = True


# tk는 gui. 윈도우 형성과, 그래픽 구현
class Badukpan_TK(tk.Frame):
    def __init__(self, master =None, omokgame=None):
        super().__init__(master)
        self.newtext = None
        if isinstance(omokgame, Omok):
            self.newtext = omokgame.badukpan()
        self.root = master
        self.count = 0
        self.endcount =0



    def create_widgets(self, omokgame=None):
        try:
            if omokgame.winner_winner == True and self.endcount > 0:
                self.canvas.pack()
                input("end")
                self.root.destroy()

            else:
                omokgame.pos_selec()
        except TypeError or IndexError:
            pass
        if self.count == 0:
            self.count += 1
            self.canvas = Canvas(self.root, width=500, height=500, bg="white")
#            if omokgame.winner_winner == True:
#                self.canvas = Canvas(self.root)
        self.canvas.delete(tk.ALL)

        self.canvas.create_text(250, 250, text=omokgame.badukpan())


        self.canvas.create_text(105, 100, text='0')
        self.canvas.create_text(121, 100, text='1')
        self.canvas.create_text(137, 100, text='2')
        self.canvas.create_text(153, 100, text='3')
        self.canvas.create_text(169, 100, text='4')
        self.canvas.create_text(185, 100, text='5')
        self.canvas.create_text(201, 100, text='6')
        self.canvas.create_text(217, 100, text='7')
        self.canvas.create_text(233, 100, text='8')
        self.canvas.create_text(249, 100, text='9')
        self.canvas.create_text(265, 100, text='10')
        self.canvas.create_text(282, 100, text='11')
        self.canvas.create_text(298, 100, text='12')
        self.canvas.create_text(314, 100, text='13')
        self.canvas.create_text(330, 100, text='14')
        self.canvas.create_text(347, 100, text='15')
        self.canvas.create_text(362, 100, text='16')
        self.canvas.create_text(378, 100, text='17')
        self.canvas.create_text(394, 100, text='18')
        self.canvas.create_text(85, 250, text='\n'.join([str(x) for x in list(range(0, 19))]))
        if omokgame.winner_winner == True:
            print("win!")
            if omokgame.count % 2 == 0:
                self.canvas.create_text(250, 45, text="""black""")
            else:
                self.canvas.create_text(250, 45, text="""white""")
            self.canvas.create_text(250, 60, text="""victory!""")
            self.canvas.create_text(250, 80, text="""press any key to end""")
            self.endcount +=1

        self.canvas.pack()
        self.canvas.after(300, self.create_widgets, omokgame)




game = Omok()
root = tk.Tk()
root.geometry('900x900+200+200')

initiation_tk = Badukpan_TK(omokgame=game, master=root)
initiation_tk.after(30, initiation_tk.create_widgets(game))
initiation_tk.mainloop()
