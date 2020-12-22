from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square



def main():

    print("\nДубянский Антон Игоревич, ИУ5Ц-71Б, Лаб №2\n")

    rectangle = Rectangle("синего", 2, 2)
    circle = Circle("зеленого", 2)
    square = Square("красного", 2)

    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()
