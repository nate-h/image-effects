# lines

Draws a picture using many overlapping lines. The location of the lines are chosen randomly
and they're used if the final picture will benefit from the line.

## Create environment

brew install cairo pkg-config
python3 -m pip install --user virtualenv
python3 -m venv lines
source lines/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=lines