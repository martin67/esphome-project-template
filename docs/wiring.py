from pathlib import Path
import schemdraw
import schemdraw.elements as elm

outfile = Path(__file__).with_suffix(".svg")

with schemdraw.Drawing(file=str(outfile)) as d:
    d += elm.SourceV().label("5V")
    d += elm.Resistor().label("220Ω")
    d += elm.LED()
    d += elm.Ground()

# IMPORTANT: just save, do NOT open
d.save(str(outfile))
