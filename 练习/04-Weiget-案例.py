import sys
from PyQt5.Qt import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("313应力报表")
window.resize(500, 500)
window.move(100, 100)


window.show()
sys.exit(app.exec_())
