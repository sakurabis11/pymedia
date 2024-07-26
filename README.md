## Language

[![Python Version](https://img.shields.io/badge/Python-3.10.0-blue)](https://www.python.org/)

## Pinterest Image Downloader Package

This Python package helps you download images from Pinterest URLs.

**Installation:**

1. Make sure you have Python 3 installed.
2. Install the package using pip:

```bash
pip install py-media-tool
```

**Call the pinterest image download package & how to use it**
``` python
from pymedia.pinterest import download_pin

url = "https://pin.it/2BojCfoIP"

download_pin(url)
```

**I create some shortcut's**

x show() -> we change the print to show to display the value given inside the parameters.

``` python
from pymedia.shortcut import show, add, subtract, sqrt, division, timedate, multi

show("Hi") #ouput: Hi
```

**Also added google ai**
``` python
from pymedia.ai import bard_ai

bard_ai("hi')
```
