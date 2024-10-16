import re
class TextAnalyzer:
def __init__(self):
self.stopwords = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'])
self.positive_words = set(['good', 'great', 'excellent', 'positive', 'fortunate', 'correct', 'superior'])
self.negative_words = set(['bad', 'poor', 'wrong', 'negative', 'unfortunate', 'incorrect', 'inferior'])
def clean_text(self, text):
# Remove special characters and numbers
text = re.sub(r'\W+', ' ', text)
text = re.sub(r'\d+', '', text)
return text.lower()
def extract_data(self, text):
# Extract sentences and words, removing stopwords
sentences = text.split('.')
words = re.findall(r'\b\w+\b', text)
words = [word for word in words if word not in self.stopwords]
return sentences, words
def sentiment_analysis(self, text):
# Perform sentiment analysis using a simple approach
words = text.split()
positive_count = sum(1 for word in words if word in self.positive_words)
subjectivity = (positive_count + negative_count) / len(words) if len(words) > 0 else 0
return polarity, subjectivity
def keyword_identification(self, text, num_keywords=10):
# Simple keyword identification based on word frequency
words = re.findall(r'\b\w+\b', text)
frequency = {}
for word in words:
frequency[word] = frequency.get(word, 0) + 1
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
keywords = [word for word, freq in sorted_words[:num_keywords]]
return keywords
def analyze_text(self, text):
cleaned_text = self.clean_text(text)
sentences, words = self.extract_data(cleaned_text)
polarity, subjectivity = self.sentiment_analysis(cleaned_text)
keywords = self.keyword_identification(cleaned_text)
return {"sentences": sentences, "words": words, "polarity": polarity, "subjectivity": subjectivity, "keywords": keywords}

def main():
print('-----TEXT ANALYZER-----')
text_analyzer = TextAnalyzer()
user_input = input("Enter the text to analyze: ")
analysis_result = text_analyzer.analyze_text(user_input)
print("\nExtracted Sentences:")
for i, sentence in enumerate(analysis_result['sentences'], 1):
print(f"{i}. {sentence.strip()}")
print("\nExtracted Words:")
print(analysis_result['words'])
print("\nSentiment Analysis:")
print(f"Polarity: {analysis_result['polarity']}")
print(f"Subjectivity: {analysis_result['subjectivity']}")
print("\nIdentified Keywords:")
print(analysis_result['keywords'])
if __name__ == "__main__":
main()
