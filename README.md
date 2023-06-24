# Sudoku Solver❓
---
### You must be familiar with Sudoku as a numerical table! This game was introduced for the first time in 1986 in Japan and since 2005 achieved global popularity. The most common type of sudoku is a 9 x 9 table, which is divided into 9 smaller 3 x 3 tables has been In this table, some numbers are placed by default
### the rest of the numbers should be found by observing the following three rules:
> * #### The first rule: in each row of the table, the numbers 1 to 9 should be placed without repetition
> * #### The second rule: in each column of the table, the numbers 1 to 9 should be placed without repetition
> * #### The third rule: numbers 1 to 9 should be placed without repetition in each 3x3 area of ​​the table
---
### In this project, we want to write a program that automatically completes the values ​​of a sudoku table. For this, it is necessary first Read the initial filled values ​​from the input.txt file. This file has 9 lines of information. 9 numbers in each line separated by a space character have became. The value of the i-th number from the j-th row indicates the value placed in row j and column i of the sudoku table (the number 0 indicates empty being a table cell.) After reading the table from this input file, by choosing one of the methods mentioned in the artificial intelligence lesson (to find suitable numbers for CSP cells, CSP+heuristics, CSP+local search, Search Algorithms,...)Empty the table and pay according to the three rules of Sudoku. Finally, the output is obtained and the algorithm execution time is printed in the output.txt file do
## 🥇Example🥇
> #### For example, for the sudoku table below, the contents of the input.txt file are as follows, for example, the first line of the file shows It is that in the first row of the table, the numbers 3, 5, and 7 are placed in columns 2, 1, and 5, respectively, and the rest of the cells in this row are empty. are
> #### 5 3 0 0 7 0 0 0 0
> #### 6 0 0 1 9 5 0 0 0
> #### 0 9 8 0 0 0 0 6 0
> #### 8 0 0 0 6 0 0 0 3
> #### 4 0 0 8 0 3 0 0 1
> #### 7 0 0 0 2 0 0 0 6
> #### 0 6 0 0 0 0 2 8 0
> #### 0 0 0 4 1 9 0 0 5
> #### 0 0 0 0 8 0 0 7 9
