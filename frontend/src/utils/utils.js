import stopWordsList from "../stopwords.json";

const stopWordsSet = new Set(stopWordsList["stopwords"]);

/**
 * Creates a filtered bag of words given a text
 * 
 * @param {string} text input string
 * @returns filtered bag of words
 */
export function createBagOfWords(text) {
  const words = text.replace(/[.?!"':;%*@#]/g, "").toLowerCase().split(" ");
  const filtered = words.filter((word) => !stopWordsSet.has(word));

  const bagOfWords = {};
  filtered.forEach((word) => {
    if (bagOfWords[word]) {
      bagOfWords[word]++;
    } else {
      bagOfWords[word] = 1;
    }
  });
  return bagOfWords;
}
