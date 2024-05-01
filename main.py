from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config

choice = ['X', '0']
switch = 0

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')
coordinate_x = []
coordinate_0 = []
coord = []
class TicTacToeApp(App):

    def tic_tac_toe(self, arg):
        global switch
        global coordinate_0
        global coordinate_x
        global coord

        arg.disabled = True
        arg.text = choice[switch]
        arg.color = [1, 1, 1, 1]

        for i in range(9):
            if self.button[i].text != '' and i not in coord:
                coord.append(i)
        print(coord[-1])  # нынешняя позиция

        if not switch:
            switch = 1
            coordinate_x.append(coord[-1])
            print(coordinate_x)
        else:
            switch = 0
            coordinate_0.append(coord[-1])
            print(coordinate_0)

        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        )
        if len(coordinate_x) == 3:
            self.button[coordinate_x[0]].color = [1, 0, 0, 1]

        if len(coordinate_0) == 3:
            self.button[coordinate_0[0]].color = [1, 0, 0, 1]

        if len(coordinate_x) > 3:
            self.button[coordinate_x[0]].text = ''
            self.button[coordinate_x[0]].disabled = False
            coord.remove(coordinate_x[0])
            coordinate_x.pop(0)

        if len(coordinate_0) > 3:
            self.button[coordinate_0[0]].text = ''
            self.button[coordinate_0[0]].disabled = False
            coord.remove(coordinate_0[0])
            coordinate_0.pop(0)

        vector = (
            [self.button[x].text for x in (0, 1, 2)],
            [self.button[x].text for x in (3, 4, 5)],
            [self.button[x].text for x in (6, 7, 8)],

            [self.button[y].text for y in (0, 3, 6)],
            [self.button[y].text for y in (1, 4, 7)],
            [self.button[y].text for y in (2, 5, 8)],

            [self.button[d].text for d in (0, 4, 8)],
            [self.button[d].text for d in (2, 4, 6)],
        )

        win = False
        color = [0, 1, 0, 1]  # Green

        for index in range(8):
            if vector[index].count('X') == 3 \
                    or vector[index].count('0') == 3:
                win = True
                for i in coordinate[index]:
                    self.button[i].color = color
                break
        if win:
            for index in range(9):
                self.button[index].disabled = True

    def restart(self, arg):
        global switch
        switch = 0

        for index in range(9):
            self.button[index].color = [0, 0, 0, 0]
            self.button[index].text = ''
            self.button[index].disabled = False
        global coordinate_x
        global coordinate_0
        global coord
        coord = []
        coordinate_x = []
        coordinate_0 = []

    def build(self):
        self.title = "Крестики-нолики"

        root = BoxLayout(orientation="vertical", padding=5)

        grid = GridLayout(cols=3)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(
                color=[0, 0, 0, 0],
                font_size=24,
                disabled=False,
                on_press=self.tic_tac_toe
            )
            grid.add_widget(self.button[index])
        root.add_widget(grid)

        root.add_widget(
            Button(
                text='Restart',
                size_hint=[1, .1],
                on_press=self.restart
            )
        )
        return root


if __name__ == '__main__':
    TicTacToeApp().run()
