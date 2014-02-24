from graphics import *

def main0():
    xtable = [10, 20, 30, 40, 50]
    ytable = [10, 20, 30, 40, 50]
    t=Transform(600,600,0,0,60,60)
    win = GraphWin("PlotXY", 600,600)
    for i in range(len(xtable)-1):
        (x,y)=t.screen(xtable[i],ytable[i])
        (x2,y2)=t.screen(xtable[i+1],ytable[i+1])
        l = Line(Point(x,y),Point(x2,y2))
        l.draw(win)
        c=Circle(Point(x,y),2)
        c.setFill("red")
        c.draw(win)
    (x,y)=t.screen(xtable[-1],ytable[-1])
    c=Circle(Point(x,y),2)
    c.setFill("red")
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
main0()
