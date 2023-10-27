import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.arc(300, 200, 150, 0, math.pi/2)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

ctx.arc(300, 200, 50, 0, 2 * math.pi)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

ctx.arc(300, 200, 100, 0, 2 * math.pi)
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(10)
ctx.stroke()

ctx.arc(300, 200, 150, 0, 2 * math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png("arc.png")
