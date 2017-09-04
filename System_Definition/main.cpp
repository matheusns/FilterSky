#include "systemdefinition.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SystemDefinition w;
    w.show();

    return a.exec();
}
