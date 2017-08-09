#include "filter_sky.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    filter_sky w;
    w.show();

    return a.exec();
}
