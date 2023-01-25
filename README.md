# Image Effects

I've been wanting to recreate some photoshop effects using mostly numpy and opencv.
Started doing so in this [notebook](./run.ipynb) and got carried away just
having fun with opencv. Managed to create a couple dozen trivial examples with
more to come when I have free time :)

## Create environment

```sh
brew install cairo pkg-config
python3 -m pip install --user virtualenv
python3 -m venv image-effects
source image-effects/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=image-effects
```
