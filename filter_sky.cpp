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
    ui->stackedWidget->setCurrentIndex(Tf);
}



void filter_sky::on_pushButton_21_clicked()
{
    ui->stackedWidget->setCurrentIndex(System);
}

void filter_sky::on_pushButton_22_clicked()
{
    ui->stackedWidget->setCurrentIndex(System);
}
