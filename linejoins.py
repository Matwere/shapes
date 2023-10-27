import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(20)

ctx.move_to(50, 100)
ctx.line_to(200, 300)
ctx.line_to(50, 300)
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.stroke()

ctx.move_to(240, 100)
ctx.line_to(370, 300)
ctx.line_to(240, 300)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

ctx.move_to(430, 100)
ctx.line_to(560, 300)
ctx.line_to(430, 300)
ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
ctx.stroke()

surface.write_to_png("join.png")