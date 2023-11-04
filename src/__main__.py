from TextProcessing import TextProcesser


def main():
    path = "C:\\Users\\kenan\\code\\python\\nlp\\characterAnalysis\\letranger.txt"
    textProcesser = TextProcesser(path)
    textProcesser.printEntities()

if __name__ == "__main__":
    main()
