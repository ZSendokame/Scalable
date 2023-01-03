# ScalableWriter
*ScalableWriter* is a small library which can generate SVG code.

# Install
```
# PIP
pip install ScalableWriter

# GIT+PIP
pip install git+https://github.com/ZSendokame/Scalable.git
```

# Use
```py
import scalable

# Specify output file, it also accepts a width and height arguments.
svg = scalable.SVG('chess.svg', width=600)
y = 10
x = 10
color = False

for row in range(8):
    for rectangle in range(8):
        rectangle_color = 'white' if not color else 'black'
        color = not color

        # The functions accept every keyword, translating them into SVG.
        svg.rectangle(
            height=30, width=30, x=x * 3, y=y,
            stroke='black', fill=rectangle_color
        )

        x += 10
        color = not color if rectangle == 7 else color

    x = 10
    y += 30

# Save file.
svg.save()
```