import curses
def main(stdscr):

    curses.noecho()
    stdscr.keypad(1)
    curses.start_color()
    win = curses.newwin(22, 79, 0, 0)
    win2 = curses.newwin(22,79,0,79)
    wina = win.subpad(18,18,1,0)
    winb = win2.subpad(18,19,1,80)
    wina.refresh()
    winb.refresh()
    win.border()
    win2.border()
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) #this line enables white
    curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_BLACK)
    while True:
        c = stdscr.getch()
        if c == 260:
            wina.bkgd(curses.color_pair(1))
            winb.bkgd(curses.color_pair(2))
        if c == 261:
            winb.bkgd(curses.color_pair(1))
            wina.bkgd(curses.color_pair(2))
        wina.refresh()
        winb.refresh()

curses.wrapper(main)#handles not fucking up terminal on exit
