#include "systemdefinition.h"
#include "ui_systemdefinition.h"

SystemDefinition::SystemDefinition(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SystemDefinition)
{
    ui->setupUi(this);
}

SystemDefinition::~SystemDefinition()
{
    delete ui;
}
