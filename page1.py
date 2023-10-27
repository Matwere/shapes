import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


ctx.rectangle(100, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

ctx.rectangle(250, 100, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(5)
ctx.stroke()

# fill and stroke
ctx.rectangle(400, 100, 100, 240)
ctx.set_source_rgb(0, 0, 1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png("rectangle.png")
