import sys
import pyglet
from pyglet import gl
from pyglet.window import key
import math

class GoldStar:
  def __init__(self, window):
    self.window = window
    self.angle = 0.0
    self.step = -5.0
    self.x = self.window.get_size()[0] / 2.0
    self.y = self.window.get_size()[1] / 2.0
    
    self.label = pyglet.text.Label("You're a star!",
      font_name='Times New Roman',
      font_size=14.0,
      x=0.0, y=0.0,
      anchor_x='center', anchor_y='center',
      color=(0, 0, 0, 255))
  
  def loadStartPosition(self):
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -4.0)
    gl.glRotatef(self.angle, 0.0, 1.0, 0.0)
  
  def draw(self):
    self.loadStartPosition()
    gl.glRotatef(90.0, 0.0, 0.0, 1.0)
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(1.0, 1.0, 0.0)
    tenth = math.pi * 2.0 / 10.0
    for z in [-0.1, 0.1]:
      for i in xrange(5):
        a = float(i) * tenth * 2.0
        gl.glVertex3f(0.0, 0.0, z)
        gl.glVertex3f(0.4 * math.cos(a - tenth), 0.4 * math.sin(a - tenth), z)
        gl.glVertex3f(math.cos(a), math.sin(a), z)
        gl.glVertex3f(0.4 * math.cos(a + tenth), 0.4 * math.sin(a + tenth), z)
    for i in xrange(5):
      a = float(i) * tenth * 2.0
      gl.glVertex3f(0.4 * math.cos(a - tenth), 0.4 * math.sin(a - tenth), 0.1)
      gl.glVertex3f(math.cos(a), math.sin(a), 0.1)
      gl.glVertex3f(math.cos(a), math.sin(a), -0.1)
      gl.glVertex3f(0.4 * math.cos(a - tenth), 0.4 * math.sin(a - tenth), -0.1)
      gl.glVertex3f(0.4 * math.cos(a + tenth), 0.4 * math.sin(a + tenth), 0.1)
      gl.glVertex3f(math.cos(a), math.sin(a), 0.1)
      gl.glVertex3f(math.cos(a), math.sin(a), -0.1)
      gl.glVertex3f(0.4 * math.cos(a + tenth), 0.4 * math.sin(a + tenth), -0.1)
    gl.glEnd()
    
    self.loadStartPosition()
    gl.glTranslatef(0.0, 0.0, 0.1)
    gl.glScalef(0.01, 0.01, 0.0)
    self.label.draw()
    
    gl.glLoadIdentity()
      
  def advance(self):
    self.angle = (self.angle + self.step) % 360.0
  
  def get_info(self):
    return "%d, %d" % (self.label.content_width, self.label.content_height)

class GoldStarWindow(pyglet.window.Window):
  def __init__(self):
    super(GoldStarWindow, self).__init__()
    
    self.gold_star = GoldStar(self)
    
    def update(dt):
      self.gold_star.advance()
    pyglet.clock.schedule_interval(update, 1/30.0)
  
  def on_key_press(self, symbol, modifiers):
    if symbol == key.Q:
      sys.exit()
    elif symbol == key.I:
      print self.gold_star.get_info()
  
  def on_draw(self):
    self.clear()
    self.gold_star.draw()
  
  def on_resize(self, width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.gluPerspective(45.0, 1.0 * width / height, 0.1, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

if __name__ == "__main__":
  window = GoldStarWindow()
  pyglet.app.run()
