# ScalableWriter
SV (*ScalableWriter*) is a small library which can generate SVG code.

# Install
```
# PIP
pip install Scalable

# GIT+PIP
pip install git+https://github.com/ZSendokame/Scalable.git
```

# Use
```py
import scalable

# Specify output file, it also accepts a width and height arguments.
svg = scalable.SVG("output.html")

# The functions accept every keyword, translating them into SVG.
svg.rectangle(
    x=150, y=60, width=25, height=75,
    fill="red", stroke="black", stroke_width=2
)
svg.ellipse(cx=205, cy=120, rx=43, ry=91, fill="red", stroke="black")
svg.ellipse(cx=210, cy=70, rx=30, ry=15, fill="white", stroke="black")
svg.line(x1=151, y1=62, x2=169, y2=62, stroke="#aa0000", stroke_width=2)

# Save the file.
svg.save()
```