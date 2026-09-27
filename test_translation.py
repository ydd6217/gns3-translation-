import sys
from PyQt6 import QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)

translator = QtCore.QTranslator()
qm = "/home/ydd/gns3-zh/gns3_zh_CN.qm"

if not translator.load(qm):
    print("ERROR: 无法加载翻译文件")
    sys.exit(1)

app.installTranslator(translator)

window = QtWidgets.QMainWindow()
window.setWindowTitle(
    QtCore.QCoreApplication.translate("MainWindow", "File")
)

menu = window.menuBar().addMenu(
    QtCore.QCoreApplication.translate("MainWindow", "&File")
)

menu.addAction(
    QtCore.QCoreApplication.translate("MainWindow", "Open")
)

menu.addAction(
    QtCore.QCoreApplication.translate("MainWindow", "Save")
)

menu.addAction(
    QtCore.QCoreApplication.translate("MainWindow", "Exit")
)

window.resize(500, 300)
window.show()

sys.exit(app.exec())
