#include "filter_sky.h"
#include "ui_filter_sky.h"

filter_sky::filter_sky(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::filter_sky)
{
    ui->setupUi(this);
}

filter_sky::~filter_sky()
{
    delete ui;
}

void filter_sky::on_pushButton_4_clicked()
{
    ui->stackedWidget->setCurrentIndex(System);
}

void filter_sky::on_pushButton_16_clicked()
{
    ui->stackedWidget->setCurrentIndex(Temperature);
}

void filter_sky::on_pushButton_12_clicked()
{
    ui->stackedWidget->setCurrentIndex(Block_Temperature);
}


void filter_sky::on_pushButton_21_clicked()
{
    ui->stackedWidget->setCurrentIndex(System);
}

void filter_sky::on_pushButton_22_clicked()
{
    ui->stackedWidget->setCurrentIndex(System);
}

void filter_sky::on_pushButton_31_clicked()
{
     ui->stackedWidget->setCurrentIndex(V105_Tf);
}

void filter_sky::on_pushButton_27_clicked()
{
    ui->stackedWidget->setCurrentIndex(Temperature);
}

void filter_sky::on_pushButton_6_clicked()
{
     ui->stackedWidget->setCurrentIndex(V104_Tf);
}

void filter_sky::on_pushButton_67_clicked()
{
    ui->stackedWidget->setCurrentIndex(Block_Temperature);
}

void filter_sky::on_pushButton_111_clicked()
{
    ui->stackedWidget->setCurrentIndex(Block_Temperature);
}

void filter_sky::on_pushButton_160_clicked()
{
    ui->stackedWidget->setCurrentIndex(Block_Temperature);
}

void filter_sky::on_pushButton_30_clicked()
{
     ui->stackedWidget->setCurrentIndex(Tic_Tf);
}

void filter_sky::on_pushButton_28_clicked()
{
    ui->stackedWidget->setCurrentIndex(Bomba_tf);
}

void filter_sky::on_pushButton_29_clicked()
{
    ui->stackedWidget->setCurrentIndex(Aquece_tf);
}

void filter_sky::on_pushButton_171_clicked()
{
    ui->stackedWidget->setCurrentIndex(Block_Temperature);
}

void filter_sky::on_pushButton_165_clicked()
{
   ui->stackedWidget->setCurrentIndex(Block_Temperature);
}
