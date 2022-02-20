'''
Fractal Tree Generator

Initial Tree:
    1. InitialPoint(n=0)  = (0,0)
       TerminalPoint(n=0) = (0,1).
    In complex numbers: line from 0+0i to 0+1i.
    
    2. User defines point (x,y) where the extreme point (0,1) moves to after one iteration.
    x+yi = factor * 0+1i   -->  factor = (x+yi) / (0+1i)
    
    3. At each iteration n
    InitialPoint(n)  = TerminalPoint(n-1)
    TerminalPoint(n) = TerminalPoint(n-1) + factor * (TerminalPoint(n-1) - InitialPoint(n-1))
    
    InitialPoint(n)  = TerminalPoint(n-1)
    TerminalPoint(n) = TerminalPoint(n-1) + factor.conjugate() * (TerminalPoint(n-1) - InitialPoint(n-1)

Created by Jorge A. Garcia
2022
'''

import matplotlib.pyplot as plt

class FractalTree:
    def __init__(self,levels,generator=(0.3,0.7)):
        real,imag = generator
        self.factor = complex(-real,imag) / complex(0,1)
        self.tree = {
            0: [ (complex(0,0), complex(0,1)) ]
            }
        for level in range(levels):
            self.iterOnce(level+1)
    
    def iterOnce(self,level):
        self.tree[level] = []
        for points in self.tree[level-1]:
            self.tree[level].append(
                ( points[1], points[1] + self.factor * (points[1] - points[0]) )
                )
            self.tree[level].append(
                ( points[1], points[1] + self.factor.conjugate() * (points[1] - points[0]) )
                )
    
    def plotTree(self,**kwargs):
        y_max = 1
        y_min = 0
        fig,ax = plt.subplots()
        for level in self.tree.keys():
            for points in self.tree[level]:
                x = [points[0].real, points[1].real]
                y = [points[0].imag, points[1].imag]
                y_max = max([y_max] + y)
                y_min = min([y_min] + y)
                ax.plot(x,y,**kwargs)
        ax.set_ylim([1.1 * y_min,1.1 * y_max])
        ax.set_axis_off()
        fig.patch.set_facecolor('k')
        fig.tight_layout()
        self.fig = fig
    
    def savePlot(self,**kwargs):
        self.fig.savefig(**kwargs)

if __name__ == '__main__':
    generator = (0.65, 0.0)
    T = FractalTree(10,generator)
    T.plotTree(linewidth=1,color='orangered')
    T.savePlot(fname='/Users/ja4garci/Documents/PythonFiles/projects2022/treeFractal_4.jpg',
               dpi=200)
    


