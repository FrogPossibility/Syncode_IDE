import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "Simple IDE"

    menuBar: MenuBar {
        Menu {
            title: "File"
            Action {
                text: "Open"
                onTriggered: {
                    fileOpen()
                }
            }
            Action {
                text: "Save"
                onTriggered: {
                    fileSave()
                }
            }
            Action {
                text: "Exit"
                onTriggered: Qt.quit()
            }
        }
    }

    TextArea {
        id: textArea
        anchors.fill: parent
        font.family: "Courier New"
        font.pointSize: 12
    }

    // Funzioni per aprire e salvare file
    function fileOpen() {
        // Chiamata alla funzione Python per aprire un file
        Qt.callLater(openFile)
    }

    function fileSave() {
        // Chiamata alla funzione Python per salvare un file
        Qt.callLater(saveFile)
    }
}