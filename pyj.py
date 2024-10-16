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
negative_count = sum(1 for word in words if word in self.negative_words)
main()

