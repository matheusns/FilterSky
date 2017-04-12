#ifndef FILTER_SKY_H
#define FILTER_SKY_H

#include <QMainWindow>

namespace Ui {
class filter_sky;
}

class filter_sky : public QMainWindow
{
    Q_OBJECT

    enum {Main=0,Tf=1,System = 2,Temperature=3,Block_Temperature=4,V105_Tf=5,V104_Tf=6,Tic_Tf=7,Bomba_tf=8,Aquece_tf=9};

public:
    explicit filter_sky(QWidget *parent = 0);
    ~filter_sky();

private slots:
    void on_pushButton_4_clicked();

    void on_pushButton_16_clicked();

    void on_pushButton_12_clicked();

    void on_pushButton_21_clicked();

    void on_pushButton_22_clicked();

    void on_pushButton_31_clicked();

    void on_pushButton_27_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_67_clicked();

    void on_pushButton_111_clicked();

    void on_pushButton_160_clicked();

    void on_pushButton_30_clicked();

    void on_pushButton_28_clicked();

    void on_pushButton_29_clicked();

    void on_pushButton_171_clicked();

    void on_pushButton_165_clicked();

private:
    Ui::filter_sky *ui;
};

#endif // FILTER_SKY_H
