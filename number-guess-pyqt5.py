import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import random

number = random.randint(1, 20)

class NumberGuess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guess the Number")
        self.setFixedSize(300, 300)
        
        # Create a central widget and layout
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        # Main layout
        self.generalLayout = QVBoxLayout(self.centralWidget)
        
        # Create display and buttons
        self.createDisplay()
        self.createButtons()

    def createDisplay(self):
        # Input field for user to enter their guess
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setPlaceholderText("Enter your guess")
        self.generalLayout.addWidget(self.display)

        # Label to show feedback about the guess
        self.feedbackLabel = QLabel()
        self.feedbackLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.generalLayout.addWidget(self.feedbackLabel)

    def createButtons(self):
        # Button to check the user's guess
        self.b1 = QPushButton("Check")
        self.b1.setFixedSize(100, 30)
        
        # Connect the button to the checkNumber method
        self.b1.clicked.connect(self.checkNumber)

        # Add button to central widget (without layout)
        self.b1.setParent(self.centralWidget)
        self.b1.move(100, 230)  # Manual position (x, y) in the central widget

    def checkNumber(self):
        try:
            # Get user's guess and convert to an integer
            userGuess = int(self.display.text())
            
            # Compare the user's guess with the random number
            if userGuess < number:
                self.feedbackLabel.setText("Low! Try again.")
            elif userGuess > number:
                self.feedbackLabel.setText("High! Try again.")
            else:
                self.feedbackLabel.setText("Correct! You guessed the number.")
        except ValueError:
            # Handle non-numeric input
            self.feedbackLabel.setText("Please enter a valid number.")

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

def main():
    gameApp = QApplication(sys.argv)
    game = NumberGuess()
    game.show()
    sys.exit(gameApp.exec())

if __name__ == "__main__":
    main()
