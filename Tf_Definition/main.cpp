#include "tfdefinition.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    TfDefinition w;
    w.show();

    return a.exec();
}
