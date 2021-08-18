# Load packages
source ~/.pyenv/versions/labmate/bin/activate  # Virtualenv
# pip install -r requirements.txt  # Requirments

# Build UI
pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py
pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

# Create requirements
pip freeze > requirements.txt

# Run file
python labmate.py