import numpy as np
import pygame
import sys
nrow=6
ncol=7

def create_board():
	board = np.zeros((6,7))
	return board
def droppiece(board, row, col, piece):
	board[row][col]=piece
def isvalid(board,col):
	return board[5][col]==0
def getnextopenrow(board,col):
	for r in range(nrow):
		if board [r][col]==0:
			return r
def printboard(board):
	print(np.flip(board,0))
def winning(board,piece):
	for c in range(ncol):
		for r in range(nrow-3):
			if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece :
				return True
	for c in range(ncol-3):
		for r in range(nrow):
			if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece :
				return True
	for c in range(ncol-3):
		for r in range(nrow-3):
			if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece :
				return True
def draw_board(board):
	pass
board=create_board()
gameover=False
turn=0
pygame.init()
SQUARESIZE=100
width=ncol*SQUARESIZE
height=(nrow+1)*SQUARESIZE
size=(width,height)
screen=pygame.display.set_mode(size)

while not gameover:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			
			if turn%2==0:
				col=int(input("Player 1 make your move(0-6):"))
				if isvalid(board,col):
					row=getnextopenrow(board,col)
					droppiece(board,row,col,1)
					if winning(board,1):
						print("Player 1 Wins!!")
						gameover=True
			else:
				col=int(input("Player 2 make your move(0-6):"))
				if isvalid(board,col):
					row=getnextopenrow(board,col)
					droppiece(board,row,col,2)
					if winning(board,2):
						print("Player 2 Wins!!")
						gameover=True
			printboard(board)
			turn+=1
