# Image Effects

The goal of this repo is to come up with several dozen ways to manipulate
python images. View [run.ipynb](./run.ipynb) to see the full results.

The effects are roughly ordered from easiest to hardest to implement.



## Create environment

```sh
brew install cairo pkg-config
python3 -m pip install --user virtualenv
python3 -m venv image-effects
source image-effects/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=image-effects
```
