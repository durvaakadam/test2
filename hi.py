class VulnerableFunction:

    def main(self):

        source = "too long"
        dest = [""] * 5
        trigger = 5

        if trigger == 5:

            # Simulated unsafe copy
            for i in range(len(source)):
                dest[i] = source[i]

        return 0


if __name__ == "__main__":
    vf = VulnerableFunction()
    vf.main()
