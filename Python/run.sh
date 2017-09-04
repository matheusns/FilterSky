rm -rf gui.py systemdefinition.py tfdefinition.py

pyuic5 ../Qt/filter_sky.ui -o gui.py
pyuic5 ../System_Definition/systemdefinition.ui -o systemdefinition.py
pyuic5 ../Tf_Definition/tfdefinition.ui -o tfdefinition.py

python3 init.py
