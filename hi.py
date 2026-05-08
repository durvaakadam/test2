class Demo:
    def main(self):
        source = "too long"
        dest = [""] * 5
        trigger = 5

        if trigger == 5:
            for i in range(len(source)):
                dest[i] = source[i]

        print("Done")


if __name__ == "__main__":
    d = Demo()
    d.main()
