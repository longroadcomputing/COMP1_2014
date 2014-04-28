# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment

import random
from datetime import date

NO_OF_RECENT_SCORES = 10
ACE_HIGH = False

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = None

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  else:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  else:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save high scores')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  return Choice.lower()[0]

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  #alter based on ace value
  if ACE_HIGH and NextCard.Rank == 1:
    NextCard.Rank = 14
  if ACE_HIGH and LastCard.Rank == 1:
    LastCard.Rank = 14
  if not ACE_HIGH and NextCard.Rank == 14:
    NextCard.Rank = 1
  if not ACE_HIGH and LastCard.Rank == 14:
    LastCard.Rank = 1
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  valid = False
  while not valid:
    PlayerName = input('Please enter your name: ')
    if len(PlayerName) > 0:
      valid = True
    else:
      print("You must enter something for your name!")
  print()
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  return Choice.lower()[0]

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = None

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<12}{1:<10}{2:<5}".format("Date","Name","Score"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if RecentScores[Count].Date != None:
      ScoreDate = RecentScores[Count].Date.strftime("%d/%m/%Y")
    else:
      ScoreDate = "N/A"
    print("{0:<12}{1:<10}{2:<5}".format(ScoreDate,RecentScores[Count].Name,RecentScores[Count].Score))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  valid = False
  while not valid:
    Choice = input("Do you want to add your score to the high score table? (y or n): ")
    Choice = Choice.lower()[0]
    if Choice in ["y","n"]:
      valid = True
    else:
      print("Please enter a valid choice (y or n)")

  if Choice == "y":
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = date.today()

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def DisplayOptions():
  print()
  print('OPTION MENU')
  print()
  print('1. Set Ace to be HIGH or LOW')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetOptionChoice():
  valid = False
  while not valid:
    Option = input()
    if Option in ['1','q']:
      valid = True
    else:
      print("Please enter a valid option")
  print()
  return Option.lower()[0]

def SetOptions(OptionChoice):
  if OptionChoice == '1':
    SetAceHighOrLow()

def SetAceHighOrLow():
  global ACE_HIGH
  valid = False
  while not valid:
    AceValue = input("Do you want the Ace to be (h)igh or (l)ow: ")
    AceValue = AceValue.lower()[0]
    if AceValue in ["h" or "l"]:
      valid = True
    else:
      print("Please enter a valid choice")
    if AceValue == "h":
      ACE_HIGH = True
    else:
      ACE_HIGH = False

def BubbleSortScores(RecentScores):
  noMoreSwaps = True
  listLength = len(RecentScores)
  while noMoreSwaps == True:
      listLength = listLength - 1
      #assume the list is sorted
      noMoreSwaps = False
      for element in range(1,listLength-1):
          #check the next student against its neighbour
          if RecentScores[element].Score < RecentScores[element+1].Score:
              #place the neighbour in a temporary value
              temporaryScore = RecentScores[element+1]
              #copy the next student into the neighbour's place
              RecentScores[element+1] = RecentScores[element]
              #copy the neighbour into the next student place
              RecentScores[element] = temporaryScore
              #set noMoreSwaps to true
              noMoreSwaps = True

def SaveScores(RecentScores):
  #avoided using csv or pickle here
  with open("save_scores.txt",mode="w",encoding="utf-8") as SaveFile:
    for Score in RecentScores:
      if Score != None:
        if Score.Name != "":
          SaveFile.write(Score.Date.strftime("%d/%m/%Y")+",")
          SaveFile.write(Score.Name+",")
          SaveFile.write(str(Score.Score)+"\n")

def LoadScores():
  #avoided using csv or pickle here
  try:
    with open("save_scores.txt",mode="r",encoding="utf-8") as LoadFile:
      scores = LoadFile.read().splitlines()
      for score in range(len(scores)):
        temp = scores[score].split(",")
        scores[score] = temp
        #convert date from string to date object
        ScoreDate = scores[score][0] #gets the date string
        Day = ScoreDate[0:2]
        Month = ScoreDate[3:5]
        Year = ScoreDate[6:]
        ScoreDate = date(int(Year),int(Month),int(Day))
        scores[score][0] = ScoreDate
    RecentScores = [None]
    for score in scores:
      NewScore = TRecentScore()
      NewScore.Date = score[0]
      NewScore.Name = score[1]
      NewScore.Score = int(score[2])
      RecentScores.append(NewScore)
  except FileNotFoundError:
    RecentScores = [None]
  return RecentScores
    

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  RecentScores = LoadScores()
  if len(RecentScores) == 0 or len(RecentScores) < NO_OF_RECENT_SCORES:
    AdditionalScores = NO_OF_RECENT_SCORES - len(RecentScores) + 1
    for Count in range(1, AdditionalScores + 1):
      RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      if OptionChoice != "q":
        SetOptions(OptionChoice)
    elif Choice == '6':
      SaveScores(RecentScores)
