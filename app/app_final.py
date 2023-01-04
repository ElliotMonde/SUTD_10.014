import turtle
import time
import winsound as wi


turtle.screensize(600, 800)  # x,y
turtle.setup(width=800, height=900, startx=0, starty=0)
screen = turtle.getscreen()
# screen.bgpic('Ganyu.gif')
screen.bgpic('game_background_1.gif')

border = turtle.Turtle()
border.speed(0)
border.pensize(10)
border.pu()
border.setpos(-400, -350)    # Score line at y=-350
border.pd()
border.setpos(400, -350)
for i in range(-400, 401, 200):
    border.pu()
    border.setpos(i, 600)
    border.pd()
    border.setpos(i, -600)
border.ht()


result = {}


class notes(turtle.Turtle):
    id_counter = 0

    def __init__(self, xpos, shape, note, timing=0, ypos=350, size=(5, 5, 9)):
        super().__init__()
        self.id = notes.id_counter
        notes.id_counter += 1
        self.triggered = False
        self.note = note
        self.timing = timing  # time at which it  si launched
        self.xpos = xpos
        self.ypos = ypos
        self.shapes = shape
        self.size = size
        self.ht()

    def moveNote(self, elapsedtime):
        timespent = elapsedtime-self.timing
        if timespent == 0:
            if self.note == 'kick':
                self.color('#66ff33')
            elif self.note == 'snare':
                self.color('#ff0066')
            elif self.note == 'hihat':
                self.color('#28b1ff')
            elif self.note == 'crash':
                self.color('#ffeb28')
            self.pu()
            self.speed(0)
            self.pos = self.setpos(self.xpos, self.ypos)
            self.shape(self.shapes)
            self.shapesize(self.size[0], self.size[1], self.size[2])
            self.st()
            if self.id == 0:
                global initial_time
                initial_time = time.time() + 5
            return

        if self.triggered:
            self.ht()
            return True
        time_to_goal = 5  # Reaches scoreline in 5s
        self.ypos = 500-((850/time_to_goal)*timespent)
        self.sety(self.ypos)
        if self.ypos < -400:
            self.ht()
            return True

    def tap(self):
        # If note is registered in results return False
        # or If note is out of range return false
        if self.triggered or self.ypos < -400:
            return False
        # If note isn't register in results, continue this codes
        # These codes registers the note into result
        if -300 > self.ypos > -400:
            result[self.id] = 'Successful'
        else:
            result[self.id] = 'Failure'

        # Make note disappear
        self.triggered = True

        return True

    def getTriggered(self):
        return self.triggered

    def getnote(self):
        return self.note

    def show(self):
        self.st()

    # creating a new shape in turtle
    diamond_turtle = turtle.Turtle()
    coords = ((0, 10), (-10, 20), (0, 30), (10, 20))
    turtle.register_shape('diamond', coords)
    # diamond_turtle.shape('diamond')

    # using beat variable to draw ypos of shape
    # use endtime-starttime to measure timedelta
    # if timedelta in dict, create drum

"""
## Lvl 1 : sample list
kickls = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 16.0, 16.375, 16.75, 16.875, 17.25, 17.625, 18.0, 18.375, 18.75, 18.875, 19.125, 19.25, 19.75, 20.0, 20.375, 20.75, 20.875, 21.125, 21.25, 21.625, 22.0, 22.375, 22.75, 22.875, 24.0, 24.375, 24.75, 24.875, 25.25, 25.625, 26.0, 26.375, 26.75, 26.875, 27.125, 27.25, 27.75, 28.0, 28.375, 28.75, 28.875, 29.125, 29.25, 29.625, 30.0, 30.375, 30.75, 30.875, 31.25, 31.625, 32.0, 32.375, 32.75, 32.875, 33.25, 33.625, 34.0, 34.375, 34.75, 34.875, 35.125, 35.25, 35.75, 36.0, 36.375, 36.75, 36.875, 37.125, 37.25, 37.625, 38.0, 38.375, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 64.0, 64.5, 65.0, 65.5,
           66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 72.0, 72.375, 72.75, 72.875, 73.25, 73.625, 74.0, 74.375, 74.75, 74.875, 75.125, 75.25, 75.75, 76.0, 76.375, 76.75, 76.875, 77.125, 77.25, 77.625, 78.0, 78.375, 78.75, 78.875, 79.25, 79.625, 80.0, 80.375, 80.75, 80.875, 81.25, 81.625, 82.0, 82.375, 82.75, 82.875, 83.125, 83.25, 83.75, 84.0, 84.375, 84.75, 84.875, 85.125, 85.25, 85.625, 86.0, 86.375, 86.75, 86.875, 87.25, 87.625, 88.0, 88.375, 88.75, 88.875, 89.25, 89.625, 90.0, 90.375, 90.75, 90.875, 91.125, 91.25, 91.75, 92.0, 92.375, 92.75, 92.875, 93.125, 93.25, 93.625, 94.0, 94.375, 94.75, 94.875, 95.25, 95.625, 96.0, 96.375, 96.75, 96.875, 97.25, 97.625, 98.0, 98.375, 98.75, 98.875, 99.125, 99.25, 99.75, 100.0, 100.375, 100.75, 100.875, 101.125, 101.25, 101.625, 102.0, 102.375, 102.75, 102.875, 103.25, 103.625]
snarels = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 56.5,
            57.5, 58.5, 59.5, 60.5, 61.5, 64.5, 65.5, 66.5, 67.5, 68.5, 69.5, 72.5, 73.5, 74.5, 75.5, 76.5, 77.5, 78.5, 79.5, 80.5, 81.5, 82.5, 83.5, 84.5, 85.5, 86.5, 87.5, 88.5, 89.5, 90.5, 91.5, 92.5, 93.5, 94.5, 95.5, 96.5, 97.5, 98.5, 99.5, 100.5, 101.5, 102.5, 103.5]
hihatls = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 13.0, 14.0, 16.0, 16.25, 16.5, 16.75, 16.875, 17.0, 17.125, 17.25, 17.5, 17.75, 17.875, 18.0, 18.25, 18.5, 18.75, 18.875, 19.0, 19.125, 19.25, 19.5, 19.75, 19.875, 20.0, 20.25, 20.5, 20.75, 20.875, 21.0, 21.125, 21.25, 21.5, 21.75, 21.875, 22.0, 22.25, 22.5, 22.75, 22.875, 24.0, 24.25, 24.5, 24.75, 25.0, 25.25, 25.5, 25.75, 25.875, 26.0, 26.25, 26.5, 26.75, 27.0, 27.25, 27.5, 27.75, 27.875, 28.0, 28.25, 28.5, 28.75, 29.0, 29.25, 29.5, 29.75, 29.875, 30.0, 30.25, 30.5, 30.75, 31.0, 31.25, 31.5, 31.75, 31.875, 32.0, 32.25, 32.5, 32.75, 33.0, 33.25, 33.5, 33.75, 33.875, 34.0, 34.25, 34.5, 34.75, 35.0, 35.25, 35.5, 35.75, 35.875, 36.0, 36.25, 36.5, 36.75, 37.0, 37.25, 37.5, 37.75, 37.875, 38.0, 38.25, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 56.0, 57.0, 58.0, 60.0, 61.0, 62.0, 64.0, 65.0, 66.0, 68.0, 69.0, 70.0, 72.0, 72.25, 72.5, 72.75, 73.0, 73.25, 73.5, 73.75,
            73.875, 74.0, 74.25, 74.5, 74.75, 75.0, 75.25, 75.5, 75.75, 75.875, 76.0, 76.25, 76.5, 76.75, 77.0, 77.25, 77.5, 77.75, 77.875, 78.0, 78.25, 78.5, 78.75, 79.0, 79.25, 79.5, 79.75, 79.875, 80.0, 80.25, 80.5, 80.75, 81.0, 81.25, 81.5, 81.75, 81.875, 82.0, 82.25, 82.5, 82.75, 83.0, 83.25, 83.5, 83.75, 83.875, 84.0, 84.25, 84.5, 84.75, 85.0, 85.25, 85.5, 85.75, 85.875, 86.0, 86.25, 86.5, 86.75, 87.0, 87.25, 87.5, 87.75, 87.875, 88.0, 88.25, 88.5, 88.75, 89.0, 89.25, 89.5, 89.75, 89.875, 90.0, 90.25, 90.5, 90.75, 91.0, 91.25, 91.5, 91.75, 91.875, 92.0, 92.25, 92.5, 92.75, 93.0, 93.25, 93.5, 93.75, 93.875, 94.0, 94.25, 94.5, 94.75, 95.0, 95.25, 95.5, 95.75, 95.875, 96.0, 96.25, 96.5, 96.75, 97.0, 97.25, 97.5, 97.75, 97.875, 98.0, 98.25, 98.5, 98.75, 99.0, 99.25, 99.5, 99.75, 99.875, 100.0, 100.25, 100.5, 100.75, 101.0, 101.25, 101.5, 101.75, 101.875, 102.0, 102.25, 102.5, 102.75, 103.0, 103.25, 103.5, 103.75, 103.875]
crashls = [56.0, 72.0]

## Lvl 2 : Billie Jeans by Michael Jackson 
kickls = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0]

snarels = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5, 50.5, 51.5, 52.5, 53.5, 54.5, 55.5, 56.5, 57.5, 58.5, 59.5, 60.5, 61.5, 62.5, 63.5, 64.5, 65.5, 66.5, 67.5, 68.5, 69.5, 70.5, 71.5, 72.5, 73.5, 74.5, 75.5, 76.5, 77.5, 78.5, 79.5, 80.5, 81.5, 82.5, 83.5, 84.5, 85.5, 86.5, 87.5, 88.5, 89.5, 90.5, 91.5, 92.5, 93.5, 94.5, 95.5, 96.5, 97.5, 98.5, 99.5, 100.5, 101.5, 102.5, 103.5, 104.5, 105.5]

hihatls = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5, 75.0, 75.5, 76.0, 76.5, 77.0, 77.5, 78.0, 78.5, 79.0, 79.5, 80.0, 80.5, 81.0, 81.5, 82.0, 82.5, 83.0, 83.5, 84.0, 84.5, 85.0, 85.5, 86.0, 86.5, 87.0, 87.5, 88.0, 88.5, 89.0, 89.5, 90.0, 90.5, 91.0, 91.5, 92.0, 92.5, 93.0, 93.5, 94.0, 94.5, 95.0, 95.5, 96.0, 96.5, 97.0, 97.5, 98.0, 98.5, 99.0, 99.5, 100.0, 100.5, 101.0, 101.5, 102.0, 102.5, 103.0, 103.5, 104.0, 104.5, 105.0, 105.5]

crashls = [66.0, 82.0]
"""
## Lvl 4 : Stronger (Cover) by Anton 
kickls = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 16.0, 16.375, 16.75, 16.875, 17.25, 17.625, 18.0, 18.375, 18.75, 18.875, 19.125, 19.25, 19.75, 20.0, 20.375, 20.75, 20.875, 21.125, 21.25, 21.625, 22.0, 22.375, 22.75, 22.875, 24.0, 24.375, 24.75, 24.875, 25.25, 25.625, 26.0, 26.375, 26.75, 26.875, 27.125, 27.25, 27.75, 28.0, 28.375, 28.75, 28.875, 29.125, 29.25, 29.625, 30.0, 30.375, 30.75, 30.875, 31.25, 31.625, 32.0, 32.375, 32.75, 32.875, 33.25, 33.625, 34.0, 34.375, 34.75, 34.875, 35.125, 35.25, 35.75, 36.0, 36.375, 36.75, 36.875, 37.125, 37.25, 37.625, 38.0, 38.375, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 72.0, 72.375, 72.75, 72.875, 73.25, 73.625, 74.0, 74.375, 74.75, 74.875, 75.125, 75.25, 75.75, 76.0, 76.375, 76.75, 76.875, 77.125, 77.25, 77.625, 78.0, 78.375, 78.75, 78.875, 79.25, 79.625, 80.0, 80.375, 80.75, 80.875, 81.25, 81.625, 82.0, 82.375, 82.75, 82.875, 83.125, 83.25, 83.75, 84.0, 84.375, 84.75, 84.875, 85.125, 85.25, 85.625, 86.0, 86.375, 86.75, 86.875, 87.25, 87.625, 88.0, 88.375, 88.75, 88.875, 89.25, 89.625, 90.0, 90.375, 90.75, 90.875, 91.125, 91.25, 91.75, 92.0, 92.375, 92.75, 92.875, 93.125, 93.25, 93.625, 94.0, 94.375, 94.75, 94.875, 95.25, 95.625, 96.0, 96.375, 96.75, 96.875, 97.25, 97.625, 98.0, 98.375, 98.75, 98.875, 99.125, 99.25, 99.75, 100.0, 100.375, 100.75, 100.875, 101.125, 101.25, 101.625, 102.0, 102.375, 102.75, 102.875, 103.25, 103.625]
snarels = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 56.5, 57.5, 58.5, 59.5, 60.5, 61.5, 64.5, 65.5, 66.5, 67.5, 68.5, 69.5, 72.5, 73.5, 74.5, 75.5, 76.5, 77.5, 78.5, 79.5, 80.5, 81.5, 82.5, 83.5, 84.5, 85.5, 86.5, 87.5, 88.5, 89.5, 90.5, 91.5, 92.5, 93.5, 94.5, 95.5, 96.5, 97.5, 98.5, 99.5, 100.5, 101.5, 102.5, 103.5]
hihatls = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 13.0, 14.0, 16.0, 16.25, 16.5, 16.75, 16.875, 17.0, 17.125, 17.25, 17.5, 17.75, 17.875, 18.0, 18.25, 18.5, 18.75, 18.875, 19.0, 19.125, 19.25, 19.5, 19.75, 19.875, 20.0, 20.25, 20.5, 20.75, 20.875, 21.0, 21.125, 21.25, 21.5, 21.75, 21.875, 22.0, 22.25, 22.5, 22.75, 22.875, 24.0, 24.25, 24.5, 24.75, 25.0, 25.25, 25.5, 25.75, 25.875, 26.0, 26.25, 26.5, 26.75, 27.0, 27.25, 27.5, 27.75, 27.875, 28.0, 28.25, 28.5, 28.75, 29.0, 29.25, 29.5, 29.75, 29.875, 30.0, 30.25, 30.5, 30.75, 31.0, 31.25, 31.5, 31.75, 31.875, 32.0, 32.25, 32.5, 32.75, 33.0, 33.25, 33.5, 33.75, 33.875, 34.0, 34.25, 34.5, 34.75, 35.0, 35.25, 35.5, 35.75, 35.875, 36.0, 36.25, 36.5, 36.75, 37.0, 37.25, 37.5, 37.75, 37.875, 38.0, 38.25, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 56.0, 57.0, 58.0, 60.0, 61.0, 62.0, 64.0, 65.0, 66.0, 68.0, 69.0, 70.0, 72.0, 72.25, 72.5, 72.75, 73.0, 73.25, 73.5, 73.75, 73.875, 74.0, 74.25, 74.5, 74.75, 75.0, 75.25, 75.5, 75.75, 75.875, 76.0, 76.25, 76.5, 76.75, 77.0, 77.25, 77.5, 77.75, 77.875, 78.0, 78.25, 78.5, 78.75, 79.0, 79.25, 79.5, 79.75, 79.875, 80.0, 80.25, 80.5, 80.75, 81.0, 81.25, 81.5, 81.75, 81.875, 82.0, 82.25, 82.5, 82.75, 83.0, 83.25, 83.5, 83.75, 83.875, 84.0, 84.25, 84.5, 84.75, 85.0, 85.25, 85.5, 85.75, 85.875, 86.0, 86.25, 86.5, 86.75, 87.0, 87.25, 87.5, 87.75, 87.875, 88.0, 88.25, 88.5, 88.75, 89.0, 89.25, 89.5, 89.75, 89.875, 90.0, 90.25, 90.5, 90.75, 91.0, 91.25, 91.5, 91.75, 91.875, 92.0, 92.25, 92.5, 92.75, 93.0, 93.25, 93.5, 93.75, 93.875, 94.0, 94.25, 94.5, 94.75, 95.0, 95.25, 95.5, 95.75, 95.875, 96.0, 96.25, 96.5, 96.75, 97.0, 97.25, 97.5, 97.75, 97.875, 98.0, 98.25, 98.5, 98.75, 99.0, 99.25, 99.5, 99.75, 99.875, 100.0, 100.25, 100.5, 100.75, 101.0, 101.25, 101.5, 101.75, 101.875, 102.0, 102.25, 102.5, 102.75, 103.0, 103.25, 103.5, 103.75, 103.875]
crashls = [56.0, 72.0]



song = (kickls, snarels, hihatls, crashls)

dic_notes = {'kick': [], 'snare': [], 'hihat': [],
             'crash': []}


def converter(compiled):
    dic = {}  # contains key of timings and values of notes
    char = ([-300, 'triangle', 'kick'], [-100, 'circle', 'snare'],
            [-7, 'diamond', 'hihat'], [300, 'square', 'crash'])
    for type in range(len(compiled)):
        for timing in compiled[type]:
            note_name = char[type][2]
            note = notes(char[type][0], char[type][1], note_name, timing)
            dic_notes[note_name].append(note)
            if timing not in dic:
                dic[timing] = [note]
            else:
                dic[timing].append(note)

    return dic


mapped = converter(song)

# for i in mapped:
#     if i == initial_time:
def tapKick():
    for kick in dic_notes['kick']:
        if kick.tap():
            break


def tapSnare():
    for snare in dic_notes['snare']:
        if snare.tap():
            break


def tapHihat():
    for hihat in dic_notes['hihat']:
        if hihat.tap():
            break


def tapCrash():
    for crash in dic_notes['crash']:
        if crash.tap():
            break

# get seconds since game started


def get_time(initial_time):
    return abs(round(time.time() - initial_time, 3))


def get_beat_range(beat_ls):  # params: list of beat timings in seconds, returns: list of tuples of left-range, center, and right-range of each beat timings in input list

    range_ls = []
    left_range = ()
    right_range = ()

    for i in range(len(beat_ls)):
        if len(beat_ls) > 1:
            if i != 0 and i != len(beat_ls)-1:
                # get left and right bound of each ls[i]
                left_range = (beat_ls[i-1] + 0.5 *
                              (beat_ls[i]-beat_ls[i-1]), beat_ls[i])
                right_range = (beat_ls[i], beat_ls[i] +
                               0.5*(beat_ls[i+1]-beat_ls[i]))
            elif i == 0:
                left_range = None
                right_range = (beat_ls[i], beat_ls[i] +
                               0.5*(beat_ls[i+1]-beat_ls[i]))
            elif i == len(beat_ls)-1:
                left_range = (beat_ls[i-1] + 0.5 *
                              (beat_ls[i]-beat_ls[i-1]), beat_ls[i])
                right_range = None

        range_ls.append((left_range, beat_ls[i], right_range))

    return range_ls


def get_beat_ind(range_ls, initial_time):  # params: a list of beat timings-ranges, initial time in seconds. returns: the index of beat at which current key pressed corresponds to (within range), and the current elasped time since game started
    # theres around a +/- 0.045 seconds delay..
    elasped = get_time(initial_time)
    print("elasped in get_beat_ind: ", elasped)
    for i in range(len(range_ls)):
        if not (i == 0 or i == len(range_ls)-1) and (range_ls[i][0][0] <= elasped < range_ls[i][2][1]):
            return i, elasped
        elif (i == 0 and elasped < range_ls[i][2][1]):
            return i, elasped
        elif (i == len(range_ls)-1 and elasped >= range_ls[i][0][0]):
            return i, elasped

# call get_accuracy when keypress where range_ls is the ls of timings for that particular drum


# params: time in seconds since game elasped, beat time-ranges list, index of beat for current key pressed. returns: float accuracy (or score) of current key pressed
def get_accuracy(elasped, range_ls, ind):
    accuracy = 0
    if not (ind == 0 or ind == len(range_ls)-1):
        if range_ls[ind][0][0] <= elasped < range_ls[ind][0][1]:  # left range
            accuracy = 100 * \
                (1 - abs((range_ls[ind][1] - elasped) /
                 (range_ls[ind][0][1] - range_ls[ind][0][0])))
            print("left")
        elif range_ls[ind][2][0] <= elasped < range_ls[ind][2][1]:  # right range
            accuracy = 100 * \
                abs((range_ls[ind][2][1] - elasped) /
                    (range_ls[ind][2][1] - range_ls[ind][2][0]))
            print("right")

    elif ind == 0:  # right range only
        accuracy = 100 * \
            abs((range_ls[ind][2][1] - elasped) /
                (range_ls[ind][2][1] - range_ls[ind][2][0]))

    elif ind == len(range_ls)-1:  # left range only
        accuracy = 100 * \
            (1 - abs((range_ls[ind][1] - elasped) /
             (range_ls[ind][0][1] - range_ls[ind][0][0])))

    return accuracy

# score ranges and add to total_score


def beat_rating(acc):  # params: float accuracy (or score) of current beat. returns a string rating for corresponding accuracy
    if 90 <= acc <= 100:
        return "Perfect"
    elif 65 <= acc < 90:
        return "Great"
    elif 30 <= acc < 65:
        return "Good"
    return "Bad"

# to initialise the different kinds of drum to control and track


class Drum:  # params: (self, *args = (list of beat time, int initial time in seconds, float initial total score, float total time of current game, bool state to check if game ended))
    def __init__(self, beat_ls, initial_time, total_score, total_time, end):
        self.beat_ls = beat_ls
        self.index_played = 0
        self.range_ls = get_beat_range(beat_ls)
        self.index = 0
        self.elasped = 0  # keep track of time since game elasped
        self.args = (initial_time, total_score, total_time, end)
        self.ratings = {
            "Miss": 0,
            "Bad": 0,
            "Good": 0,
            "Great": 0,
            "Perfect": 0}

    # trigger the score counting functions and track which current beat its on
    def press_drum(self, initial_time, total_score, total_time, end):  # params: *self.args
        if self.elasped < total_time + 2:  # 2 seconds buffer after song ends. trigger the function in onkeypress only if player pressed during song duration
            # end[0] = False
            self.index, self.elasped = get_beat_ind(
                self.range_ls, initial_time)
            if self.index_played < self.index:
                self.index_played = self.index
                acc = round(get_accuracy(
                    self.elasped, self.range_ls, self.index), 3)
                if acc < 0:
                    acc = 0
                rating = beat_rating(acc)
                total_score["total"] += acc
                print(
                    f"index: {self.index}, elasped: {self.elasped}, accuracy: {acc}, rating: {rating}")
                print(" %.3f/ %d" %
                      (total_score["total"], 100*len(self.range_ls)))

                self.ratings[rating] += 1
                # call graphic function to display rating graphics
            else:
                print("Slow down! beat played")
        else:  # end game with any key after audio ends
            self.ratings["Miss"] = len(
                self.range_ls) - sum(self.ratings.values())
            [print("%s: %d" % (i, j))
             for i, j in zip(self.ratings.keys(), self.ratings.values())]
            print(" %.3f/ %d" % (total_score["total"], 100*len(self.range_ls)))
            print("Press any key to end game.")
            # display score page, or reset to menu screen, currently unimplemented
            turtle.onkeypress(quit)

    def play_call(self):
        self.press_drum(*self.args)

screen.onkeypress(tapKick, 'a')
screen.onkeypress(tapSnare, 's')
screen.onkeypress(tapHihat, 'k')
screen.onkeypress(tapCrash, 'l')
screen.listen()


def gamemapping(kickls, snarels, hihatls, crashls):
    initial_time = time.time()
    ending = max(mapped.keys())+30
    notes_to_be_run = set()
    time_controller = []  # List of 0.1 seconds, [0.1, 0.2, 0.3]

    # initialisation
    # "zero-ing" of the time/reference time at which game start
    total_score = {"total": 0}
    total_time = max([kickls[-1], snarels[-1],
                     hihatls[-1], crashls[-1]])
    # bool to check if song has ended, currently unimplemented, keypress 'x' to quit instead
    end = [False]
    args = (initial_time, total_score, total_time, end)
    
    """
    ## initialise Drum class instances to track score for each column, uncomment and view real-time score and accuracy printed to command line
    kick = Drum(kickls, *args)
    snare = Drum(snarels, *args)
    hihat = Drum(hihatls, *args)
    crash = Drum(crashls, *args)

    turtle.onkey(kick.play_call, 'a') # turtle's onkeypress takes in a function with no param
    turtle.onkey(snare.play_call, 's')
    turtle.onkey(hihat.play_call, 'k')
    turtle.onkey(crash.play_call, 'l')
    turtle.onkeypress(turtle.bye, 'x')
    turtle.listen()
    """

    songPlaying = False
    

    while time.time()-initial_time < ending + 5:
        elapsedtime = round((time.time()-initial_time), 1)
        if elapsedtime in mapped:
            ls_of_notes = mapped.get(elapsedtime)
            for note in ls_of_notes:
                notes_to_be_run.add(note)
            del mapped[elapsedtime]
        if elapsedtime not in time_controller:
            time_controller.append(elapsedtime)
            # print(elapsedtime)
            note_to_kill = []
            for note in notes_to_be_run:
                kill_me = note.moveNote(elapsedtime)
                if songPlaying == False:
                    time.sleep(5)
                    wi.PlaySound("Level4_Stronger_AntonVocals_120bpm.wav",
                                 wi.SND_FILENAME | wi.SND_ASYNC)
                    songPlaying = True
                if kill_me:
                    note_to_kill.append(note)
            for note in note_to_kill:
                notes_to_be_run.remove(note)


            # print(len(notes_to_be_run))
gamemapping(kickls, snarels, hihatls, crashls)

# #timer
# initial_time = time.time()
# def get_time():
#     elapsed_time = abs(round(time.time() - initial_time, 1))
#     return elapsed_time

# #while get_time < song duration, remove ls[0] and moves note if get_time() is in ls
# #[0.0,0.5,1.0,1.5,2.0] when get_time is 0.0 -> [0.5,1.0,1.5,2.0], note moves down
# #loop starts again
# while get_time() <= 13: #song duration
#     print(result)
#     # print(get_time())
#     for i in kickls:
#         if get_time() == kickls[0]:
#             kick.moveNote(dis,speedOfMusic)
#             kickls.remove(kickls[0])
#             # time.sleep(0.2)
#     for h in hihatls:
#         if get_time() in hihatls:
#             hihat.moveNote(dis,speedOfMusic)
#             hihatls.remove(hihatls[0])
#             # time.sleep(0.2)
#     for c in crashls:
#         if get_time() in crashls:
#             crash.moveNote(dis,speedOfMusic)
#             crashls.remove(crashls[0])
#             # time.sleep(0.2)
#     for s in snarels:
#         if get_time() in snarels:
#             snare.moveNote(dis,speedOfMusic)
#             snarels.remove(snarels[0])
#             time.sleep(0.2)
#         kick1.moveNote(dis,speedOfMusic)
#     time.sleep(0.02)
# def get_note(ls, initial_time):
#     for i in range(len(ls)):
#         if ls[i] < get_time(initial_time):
#             kick1.moveNote(dis,speedOfMusic)
#             ls.remove(ls[0])
#     return kick

# def refresh(ls,initial_time):
#     while song == True
#         get_note(kick,initial_time)
# while timer < 100:  # Duration of Song
#     print(result)
#     kick1.moveNote(dis, speedOfMusic)  # sample
#     delay = 5  # time elapsed keep at factor of 5
#     drums = [kick2, snare, hihat, crash]
#     if timer > delay:
#         for i in drums:
#             i.moveNote(dis, speedOfMusic)

#         # kick2.moveNote(dis,speedOfMusic)
#         # snare.moveNote(dis,speedOfMusic)
#         # hihat.moveNote(dis,speedOfMusic)
#         # crash.moveNote(dis,speedOfMusic)
#     timer += 1
#     time.sleep(0.2)

turtle.done()
