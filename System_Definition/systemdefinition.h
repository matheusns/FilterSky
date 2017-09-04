#ifndef SYSTEMDEFINITION_H
#define SYSTEMDEFINITION_H

#include <QMainWindow>

namespace Ui {
class SystemDefinition;
}

class SystemDefinition : public QMainWindow
{
    Q_OBJECT

public:
    explicit SystemDefinition(QWidget *parent = 0);
    ~SystemDefinition();

private:
    Ui::SystemDefinition *ui;
};

#endif // SYSTEMDEFINITION_H
