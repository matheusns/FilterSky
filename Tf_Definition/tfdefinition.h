#ifndef TFDEFINITION_H
#define TFDEFINITION_H

#include <QMainWindow>

namespace Ui {
class TfDefinition;
}

class TfDefinition : public QMainWindow
{
    Q_OBJECT

public:
    explicit TfDefinition(QWidget *parent = 0);
    ~TfDefinition();

private:
    Ui::TfDefinition *ui;
};

#endif // TFDEFINITION_H
