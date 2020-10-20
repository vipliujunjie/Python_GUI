from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

window = QWidget()
# window.setFixedSize(500, 500)
label = QLabel(window)
label.setText("社会顺")
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")


def BtnPlus():
    new_content = label.text() + "社会顺"
    # QApplication.processEvents()    # 刷新label
    label.setText(new_content)
    label.repaint()
    label.adjustSize()
    window.adjustSize()


btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100, 300)
btn.clicked.connect(BtnPlus)

window.show()

# 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
