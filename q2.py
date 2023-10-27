import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(150, 100, 100, 150)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

surface.write_to_png("q2.png")