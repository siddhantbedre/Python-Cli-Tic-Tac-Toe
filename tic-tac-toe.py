# Importing Modules ===============

import random

import time

# =================================

print("""
      Welcome to Tic Tac Toe Game
  
        |---------------|
        |TIC - TAC - TOE|
        |---------------|

	""")

win_method = None

def start_page(): # Start Page for Tic Tac Toe Game
  print("""
    =============================
      """)
  
  print("     Press S to Start Game") 
  time.sleep(0.3)
  print("     Press I to Get Info of Game")
  time.sleep(0.3)        
  print("     Press Q to Exit")  
  print("""
    =============================
      """)

  option = input("""
        >> """)
  option = str.upper(option)
  if option in ("S","I","Q"):
    if option == "S":
      time.sleep(1)
      main_game()
    elif option == "I":
      info_r = open("Info.txt","r")
      print(info_r.read())
      info_r.close()
      start_page()
    if option == "Q":
      print("""
        Exiting From Game ......
        """)
      time.sleep(1)
      exit()
  else:
    print("""
      !!!! Invalid Input !!!!

      Choose Between S , I and Q """)
    start_page()

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

Game_play = True

winner = None

# Random Turn Generator ==================

turn_option = ["X","O"]

current_turn = random.choice(turn_option)

# ========================================

def main_game(): # Main Game Loop
  print("""
    ==============================================
    ==============================================
    """)
  show_board()
  while Game_play:
    use_turn(current_turn)
    game_over()
    change_player()
  time.sleep(0.5)
  end_game()



def show_board(): # Display Game Board
  print("                "+ "----" + "-----" + "----")
  print("                "+ "| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
  print("                "+ "----" + "-----" + "----")
  print("                "+ "| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
  print("                "+ "----" + "-----" + "----")
  print("                "+ "| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
  print("                "+ "----" + "-----" + "----")

def use_turn(current_turn): # Insert X and O on Board

  print("""
          """+ current_turn + "'s turn." +"""
          ----------------""")
  position = input("""
          Choose Position on board 1 to 9 )>> """)
  if position in ("1","2","3","4","5","6","7","8","9"):
    position = int(position) - 1
    if board[position] == "-":
      board[position] = current_turn
    elif board[position] == "X" or "O":
      print("""

        ===================================
        !!!! Place is already occupied !!!!
                  Try Another
        ===================================
        
        """)
  else :
    print("""
          =====================
          !!! Invalid Input !!!
          =====================
          """)
    change_player()
    time.sleep(1)

  time.sleep(0.3)
  show_board()

def game_over(): # Check Whether Anyone won or Game Tied
  check_winner()
  check_tie()

def check_winner(): # Check Winner
  global winner
  global win_method
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
    win_method = "Win By Row-line"
  elif column_winner:
    winner = column_winner
    win_method = "Win By Column-line"
  elif diagonal_winner:
    winner = diagonal_winner
    win_method = "Win By Diagonal-line"
  else:
    winner = None

def change_player(): # Change Player Turn
    global current_turn
    if current_turn == "X":
      current_turn = "O"
    elif current_turn == "O":
      current_turn = "X"

def check_rows(): # Check Row Win
  global Game_play
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    Game_play = False
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  else:
    return None

def check_columns(): # Check Column Win
  global Game_play
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  if col_1 or col_2 or col_3:
    Game_play = False
  if col_1:
    return board[0] 
  elif col_2:
    return board[1] 
  elif col_3:
    return board[2]
  else:
    return None

def check_diagonals(): # Check Diagonal Win 
  global Game_play
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    Game_play = False
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return None

def check_tie(): # Check Tie in Game
  global Game_play
  if "-" not in board:
    Game_play = False
    winner = None
  else :
  	return True

def end_game(): # Display Winner and Winning Method
  if winner == "X" or winner == "O":
    print("""
      """ + winner +" is winner")
    time.sleep(0.5)
    print("""
      """ + "Winner " + win_method)
    print("""
      Game close after 3 Second..........
      """)
    time.sleep(3)
    exit()
  elif winner == None :
    print("""
      Game is Tie

      """)
    print("""
      Game close after 3 Second..........
      """)
    time.sleep(3)
    exit()


start_page()