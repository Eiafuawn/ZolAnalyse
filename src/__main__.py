from TextProcessing import TextProcesser


def main():
    path = "C:\\Users\\kenan\\code\\python\\nlp\\characterAnalysis\\letranger2.txt"
    textProcesser = TextProcesser(path)
    textProcesser.processBySentence()
    textProcesser.render("entities_by_sentence")
    textProcesser.render("sentence")

if __name__ == "__main__":
    main()
