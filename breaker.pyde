xCoordinate = random (50, 200)
yCoordinate = random (50, 200)
ySpeed = 3
xSpeed = 5

ellipseSize = 20

def setup ():
    size(800, 800)
    


def draw():
    background(0, 0, 0)
    fill(0, 156, 159)
    rect(0, 0, 80, 30)
    fill(255, 102, 204)
    rect(80, 0, 80, 30)
    fill(0, 102, 0)
    rect(160, 0, 80, 30)
    fill(102, 0, 255)
    rect(240, 0 , 80, 30)
    fill(255, 204, 0)
    rect(320, 0, 80, 30)
    fill(255, 153, 0)
    rect(400, 0, 80, 30)
    fill(255, 0, 0)
    rect(480, 0, 80, 30)
    fill(204, 153, 255)
    rect(560, 0, 80, 30)
    fill(0, 204, 255)
    rect(640, 0, 80, 30)
    fill(204, 153, 255)
    rect(720, 0, 80, 30)
    fill(204, 255, 153)
    rect(800, 0, 80, 30) 
    
    
    r = random (50, 400)
    global xCoordinate, yCoordinate, xSpeed, ySpeed, ellipseSize
    topBoundary = ellipseSize / 2+30
    bottomBoundary =800 - ellipseSize /2
    
    leftBoundary = ellipseSize / 2
    rightBoundary =800 - ellipseSize /2
    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
      ySpeed = -ySpeed  #reverse ball
      yCoordinate += ySpeed
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
       xSpeed =-xSpeed
    
    yCoordinate += ySpeed
    xCoordinate += xSpeed
    noStroke()
    fill(0,255,0)
    ellipse (xCoordinate, yCoordinate, ellipseSize, ellipseSize)
            
