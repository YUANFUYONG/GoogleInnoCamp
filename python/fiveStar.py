from turtle import * 

def main():  
    p=Turtle() 
    p.shape('turtle')
    p.speed(1)  
    p.pensize(2)  
    p.pencolor("black")  
    p.fillcolor("red")  
    p.begin_fill()  
    for i in range(5):  
        p.forward(200)  
        p.right(144)  
    p.end_fill()  
    done()

main()