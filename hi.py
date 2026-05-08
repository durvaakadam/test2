def main():
    source = "too long"
    dest = [""] * 5
    trigger = 5

    if trigger == 5:

        # Simulating unsafe copy
        for i in range(len(source)):
            dest[i] = source[i]

    print("Done")


if __name__ == "__main__":
    main()
