#ifndef FILTER_SKY_H
#define FILTER_SKY_H

#include <QMainWindow>

namespace Ui {
class filter_sky;
}

class filter_sky : public QMainWindow
{
    Q_OBJECT

    enum {Main=0,Tf=1,System = 2,Temperature=3};

public:
    explicit filter_sky(QWidget *parent = 0);
    ~filter_sky();

private slots:
    void on_pushButton_4_clicked();

    void on_pushButton_16_clicked();

    void on_pushButton_12_clicked();

    void on_pushButton_21_clicked();

    void on_pushButton_22_clicked();

private:
    Ui::filter_sky *ui;
};

#endif // FILTER_SKY_H
