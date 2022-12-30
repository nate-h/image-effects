# Image Effects

The goal of this repo is to learn how to manipulate images using python.
There are 10 manipulations I intend to create:

- [x] hue mapping
- [x] 4 gamma corrected side by side
- [ ] Neon glow
- [ ] Separate rgb and draw 3 sep drawings
- [ ] Halftone
- [ ] Lines
- [ ] Something using scipy geometric transform
- [ ] Layers and messing with alpha... Use text?
- [ ] Melting
- [ ] Brush
- [ ] Pixelate and reduce number of colors

## Create environment

```sh
brew install cairo pkg-config
python3 -m pip install --user virtualenv
python3 -m venv image-effects
source image-effects/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=image-effects
```
