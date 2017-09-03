#include "tfdefinition.h"
#include "ui_tfdefinition.h"

TfDefinition::TfDefinition(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TfDefinition)
{
    ui->setupUi(this);
}

TfDefinition::~TfDefinition()
{
    delete ui;
}
