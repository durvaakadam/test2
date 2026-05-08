class Demo:
    def main(self):
        source = "too long"
        dest = [""] * 5
        trigger = 5
class Calculator:

    def add(self, a, b):
        result = a + b
        return result

    def subtract(self, a, b):
        result = a - b
        return result


class Message:

    def display(self, text):
        print(text)


def main():

    calc = Calculator()
    msg = Message()

    sum_result = calc.add(10, 5)
    sub_result = calc.subtract(10, 5)

    if sum_result > sub_result:
        msg.display("Addition result is greater")
    else:
        msg.display("Subtraction result is greater")


if __name__ == "__main__":
    main()
        if trigger == 5:
            for i in range(len(source)):
                dest[i] = source[i]

        print("Done")


if __name__ == "__main__":
    d = Demo()
    d.main()
