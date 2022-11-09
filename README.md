# TicTacToe 
The project is about finding a winning solution to the O player on tictactoe i.e having three consecutive O’s on the TicTacToe board. The test was taken from codingame. Following is the URL of the quiz:

https://www.codingame.com/ide/puzzle/tictactoe

## The Problem
The solution is to find three O’s that are in line/diagonal. The two constraints are that the final resulting board must be the same as the input one, and the input entered manually can’t be the winner itself. We have to work around these constraints and attempt to find a nice answer to this TicTacToe problem. 
Tools Used
Python was used as the core language to perform this task. The following libraries were taken use of during the process.
- Numpy
-	Sys

## The Approach
Before going ahead, knowledge of python and some of its core libraries like Numpy is needed. For this programming quiz, a simple and straightforward approach was devised. Following are the list of steps taken to find the solution:
-	The problem has three main value indicators i.e X, O, and DOT(.)
-	We have to find a solution that can make O the winner i.e three consecutive O’s.
- We first take the 3x3 matrix grid containing some X and O values including DOT.
-	Those values are replaced by the following; X by -1, O by 1, and DOT by 0.
-	To reach the solution, we take a sum of the rows, columns and both diagonals. These sum of values give us an idea about how many O’s, dots , and X’s are there, and how we need to handle the problem in a way as to produce 3 consecutive O’s. be it row-wise, column-wise, or diagonally.
-	 If the sum of any row, column, or diagonal equates to 3, we already have our solution.
-	If the sum is 2 in any row, column, or diagonal, we replace the dot by 1 to have the required 3 O’s.
-	An important point is the fact that input and output must be the same other than the addition of O to make O win.
-	The value of X should also be remembered, hence why the ii_x variable is used.


## Running the Project
If you intend to run the project at codingame, you simply need to copy the code and paste it there on the project quiz link given above. For the local running, you need to have a Python IDE installed like Jupyter Notebook etc.
One also needs to have all the required libraries properly installed and imported. Numpy doesn’t come with the official Python package. So, it has to be installed and imported manually. The sys library comes packaged with the Python tool. The libraries can be installed with the following command:

                                          pip install {library-name}
                                                 
For Jupyter Notebook, add a **!** or a **%** at the start of the index tab before running the terminal command. If you intend to run it directly in the terminal, you can use the command as it is.

## Learnings from this Test
The aim of this test was to find a solution that fits. The main aim was not to find the best solution possible for it. So, as an open-source piece of code, one is free to modify it and make changes to it to have a better output if they want.
