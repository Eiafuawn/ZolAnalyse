# ZolAnalyse

## Introduction

ZolAnalyse is an ongoing project that tackles the challenging task of Named Entity Recognition (NER) for character analysis in French texts, with a specific emphasis on the works of L'étranger by Albert Camus. This README aims to provide insights into the thought process, challenges faced, and key decisions made during the development of the project.

## Thought Process

### Choice of NER Model

Creating an effective NER model for French proved to be more challenging than anticipated. After experimenting with various approaches, I discovered a promising solution on GitHub ([hzjken/character-network](https://github.com/hzjken/character-network/)) and adapted it to meet the specific needs of ZolAnalyse. You can see all my trial and errors in the [non-working](./non-working/) folder. For each part of the project, I take a lot of time trying to understand and optimize everything. So there's quite a lot of trial and error and not a lot of achievement.

### Model Initialization

For NER I used spaCy as it's trained model seemed quite easy to understand. I will probably try with camembert later.
The project utilizes pre-trained models for tokenization and sequence classification, specifically the `camembert-base` model. This choice was motivated by its compatibility with French text, offering a solid foundation for further adaptations.

### Challenges in Sentiment Analysis

The sentiment analysis component of the project leverages the Camembert model as well. While the model provides valuable insights, challenges arose in mapping sentiment scores to specific characters or sections of the text. Further refinements are necessary to enhance the granularity of sentiment analysis.
## French Emotion detection

Still haven't been able to make it work for now

## Project Structure

- **`zolanalyse.py`**: The core script for character analysis.
- **`requirements.txt`**: Dependencies for the project.
- **`/data`**: A directory for storing sample data or datasets.
- **`/docs`**: Project documentation (if applicable).
- **`/tests`**: Unit tests (if applicable).

## Reflections

### Overcoming NER Challenges

The adapted NER model significantly improved the project's accuracy in identifying named entities, particularly characters and organizations. The process involved converting identified entities to lowercase, removing possessive forms, and filtering out short names for improved recognition accuracy.

### Sentiment Analysis Dilemma

Mapping sentiment scores to specific characters or sections proved to be a complex task. The current approach provides an overall sentiment score for each sentence, but further work is needed to connect sentiments to individual entities.

## Next Steps

- **Enhance Sentiment Analysis**: Develop a mechanism to attribute sentiment scores to specific characters or sections of the text.
- **Explore Additional NLP Techniques**: Investigate other NLP techniques to further improve the accuracy and granularity of character analysis.
- **Try and Find a working emotion detection model in French**

## Contributions

Contributions to ZolAnalyse are welcome! Feel free to open issues or submit pull requests to enhance the project.

## Conclusion

ZolAnalyse is an evolving project with a focus on understing NLP and trying to automate character analysis in French texts. The journey involves overcoming challenges, adapting existing solutions, and continually refining the project to deliver more accurate and meaningful insights.

