import turtle as t
m = 30
t.screensize(2000,2000) #
t.up() #
t.tracer(0) # отмена трасировки
for x in range(50): # рисует сетку
    for y in range(50):
        t.goto(x*m,y*m)
        t.dot(5)
t.width(5)
t.home() # возвращает в начальную точку
t.left(90) # влево
t.down() # опутить хвост
for i in range(2):
    t.forward(8*m) # вперед
    t.right(90) # вправо
    t.forward(18*m)
    t.right(90)
t.up()
t.forward(4*m) # вперед
t.right(90) # вправо
t.forward(10*m)
t.left(90)
t.down()
for i in range(2):
    t.forward(17*m)  # вперед
    t.right(90)  # вправо
    t.forward(7*m)
    t.right(90)
t.update()
t.done()
