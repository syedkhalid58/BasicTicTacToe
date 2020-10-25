# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:53:06 2020

@author: syedk,samsul and akmal
"""

#Tic Tac Toe 5x5

board = [' ' for x in range(26)]

def insertLetter(letter, pos):
   board[pos] = letter

def spaceIsFree(pos):
   return board[pos] == ' '

def printBoard(board):
   print('   |   |   |   |   ')
   print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
   print('   |   |   |   |   ')
   print('___________________')
   print('   |   |   |   |   ')
   print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ' + board[10])
   print('   |   |   |   |   ')
   print('___________________')
   print('   |   |   |   |   ')
   print(' ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ' + board[15])
   print('   |   |   |   |   ')
   print('___________________')
   print('   |   |   |   |   ')
   print(' ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[20])
   print('   |   |   |   |   ')
   print('___________________')
   print('   |   |   |   |   ')
   print(' ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25])
   print('   |   |   |   |   ')
   print('___________________')

def isWinner(bo, le):
   return (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or \
          (bo[6] == le and bo[7] == le and bo[8] == le and bo[9] == le and bo[10] == le) or \
          (bo[11] == le and bo[12] == le and bo[13] == le and bo[14] == le and bo[15] == le) or \
          (bo[16] == le and bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or \
          (bo[21] == le and bo[22] == le and bo[23] == le and bo[24] == le and bo[25] == le) or \
          (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le and bo[21] == le) or \
          (bo[2] == le and bo[7] == le and bo[12] == le and bo[17] == le and bo[22] == le) or \
          (bo[3] == le and bo[8] == le and bo[13] == le and bo[18] == le and bo[23] == le) or \
          (bo[4] == le and bo[8] == le and bo[13] == le and bo[18] == le and bo[23] == le) or \
          (bo[5] == le and bo[10] == le and bo[15] == le and bo[20] == le and bo[25] == le)  or \
          (bo[1] == le and bo[7] == le and bo[13] == le and bo[19] == le and bo[25] == le) or \
          (bo[5] == le and bo[9] == le and bo[13] == le and bo[17] == le and  bo[21] == le)


def playerMove():
   run = True
   while run:
       move = input('Select position to place an \'x\' (1-25)')
       try:
           move = int(move)
           if move>0 and move<26:
               if spaceIsFree(move):
                   run = False
                   insertLetter('X', move)
               else:
                   print('Sorry, this place is occupied')
           else:
               print('Please insert a number within the range!')
       except:
           print('Please type a number')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1,5,21,25]:
            cornerOpen.append(i)
    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move

    centerOpen = []
    for i in possibleMoves:
        if i in [7,8,9,12,13,14,17,18,19]:
            centerOpen.append(i)
    if len(centerOpen) > 0:
        move = selectRandom(centerOpen)
        return move


    edgeOpen = []
    for i in possibleMoves:
        if i in [2,3,4,6,10,15,11,16,20,22,23,24]:
            edgeOpen.append(i)
    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)
    return move


def selectRandom(li):
   import random

   ln = len(li)
   r = random.randrange(0,ln)
   return li[r]


def isBoardFull(board):
   if board.count(' ') > 1:
       return False
   else:
       return True


def main():
   print('Welcome to 5x5 Tic Tac Toe!')
   printBoard(board)

   while not (isBoardFull(board)):
       if not (isWinner(board, 'O')):
           playerMove()
           printBoard(board)
       else:
           print('Sorry, O\'s won this time!')
           break

       if not (isWinner(board, 'X')):
           move = compMove()
           if move == 0:
               print('Tie Game!')
           else:
               insertLetter('O', move)
               print('Computer placed an \'O\' in position', move, ':')
               printBoard(board)
       else:
           print('X\'s won this time! Good Job!')
           break

   if isBoardFull(board):
       print('Tie Game!')





main()
