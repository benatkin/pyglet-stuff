import pyglet
from pyglet import gl
import time

class RotatingTriangle:
  def __init__(self, x, y, angle, step):
    self.x = x
    self.y = y
    self.angle = angle
    self.step = step
  
  def draw(self):
    gl.glLoadIdentity()
    gl.glTranslatef(self.x, self.y, 0)
    gl.glRotatef(self.angle, 0.0, 0.0, 1.0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex2f(0, 50)
    gl.glVertex2f(-50, -50)
    gl.glColor3f(0.0, 0.2, 0.0)
    gl.glVertex2f(50, -50)
    gl.glEnd()
    gl.glLoadIdentity()
    
    self.angle = (self.angle + self.step) % 360

window = pyglet.window.Window()

label = pyglet.text.Label('',
  font_name = 'Helvetica',
  font_size = 24,
  x = window.width // 2,
  y = window.height // 2,
  anchor_x = 'center',
  anchor_y = 'center')

triangles = [RotatingTriangle(300, 100, 0, 2),
  RotatingTriangle(100, 350, 90, 5),
  RotatingTriangle(100, 200, 205, 20),
  RotatingTriangle(120, 190, 205, 20),
  RotatingTriangle(140, 180, 205, 20),
  RotatingTriangle(160, 170, 205, 20)]

presses = 0
maitime = time.asctime()

def update_time(delta_t):
  global maitime
  maitime = time.asctime()

@window.event
def on_draw():
  window.clear()
  for triangle in triangles: triangle.draw()
  label.text = 'Hello, piggies! ' + str(presses) + ' ' + maitime
  label.draw()

@window.event
def on_key_press(symbol, modifiers):
  global presses
  presses = presses + 1

pyglet.clock.schedule(update_time)

pyglet.app.run()