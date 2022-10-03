from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTabWidget, QCheckBox
import sys
from stocks import stock_tracker as st

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Stock Tracker v1'
        self.left = 10
        self.top = 10
        self.width = 1080 # window width
        self.height = 920 # window height

        # our stock tracker class
        self.stockTracker = st.StockTracker()

        # init the UI
        self.initUI()
    
    def homePageUI(self):
        """Create the home page UI"""
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("General Option 1"))
        layout.addWidget(QCheckBox("General Option 2"))
        generalTab.setLayout(layout)
        return generalTab

    def configurationTabUI(self):
        """Create the Network page UI."""
        networkTab = QWidget()
        layout = QVBoxLayout()
        currStocks = self.stockTracker.get_stock_price("MSFT")
        layout.addWidget(QCheckBox(str(currStocks)))
        layout.addWidget(QCheckBox("Network Option 2"))
        networkTab.setLayout(layout)
        return networkTab

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Create widget
        label = QLabel('PyQt5 label', self)
        label.move(50,50)
        
        button = QPushButton('PyQt5 button', self)
        button.move(100,100)

        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.homePageUI(), "Home")
        tabs.addTab(self.configurationTabUI(), "Configuration")
        layout.addWidget(tabs)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())