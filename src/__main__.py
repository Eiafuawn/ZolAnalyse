from TextProcessing import TextProcesser


def main():
    path = "C:\\Users\\kenan\\code\\python\\nlp\\characterAnalysis\\letranger.txt"
    textProcesser = TextProcesser(path)
    textProcesser.render("entities")
    # textProcesser.getEntities(False)
    # textProcesser.getSentence(False)
    # textProcesser.getProcessedTxt(False)

if __name__ == "__main__":
    main()
