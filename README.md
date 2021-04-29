# Warpify.py
### Creating slit-scan and time-displacement effects
-------

<!-- ![Warpify Demo](\images\demo.gif) -->
![Warpify Demo](https://github.com/csaddison/Slit-Scan-Compositing/blob/main/images/demo.gif)

Warpify provides a simple CLI to warp and save videos. Simply launch the application with `python warpify.py` to get started. Alternatively, warpify also provides direct access to it's inner functions for use in your own projects. A simple case could look like this:

``` python
from warpify import SlitScan

warp = SlitScan('path/to/file.avi')
mask = warp.GenerateLinearMask(displacement=30, 'vertical')
warp.Slice(mask)
warp.Render('warped.avi', fps=60)
```

<br>

#### Changelog:
Warpify v0.9 is still in beta stages and the next update will have better error handling.