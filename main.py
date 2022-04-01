from pytube import YouTube
from collections import Counter
from youtube_transcript_api import YouTubeTranscriptApi

keyterms = [] #add custom keyterms here
link = 'VIDEOURLHERE'
text = []
correct = []

def get_facts(text):
  words = []
  video = YouTube(link)
  common = open('common.txt','r').read().split('\n')
  description = video.description.lower()
  for word in common:
    description = description.replace(word, '')
  for punc in list(',.?/"!@#$%^&*()+=-_'):
    description = description.replace(punc, '')
  description = description.split()
  common = open('10000.txt','r').read().split('\n')
  for word in description:
    if word in common:
      words.append(word)
  description.clear()
  for word in words:
    if len(word) > 2: description.append(word)
  description = list(Counter(description).keys())
  return description
  

for i, char in enumerate(link):
  if link[i] == '=':
    break 
srt = list(YouTubeTranscriptApi.get_transcript(link[i+1:len(link)]))
for item in srt: text.append(item['text'].replace('\n',' '))
string = ' '.join(text)
text.clear()
start = 0
for index, char in enumerate(string):
  if string[index:index+2] == '. ':
    text.append(string[start:index+2])
    start = index+2
keyterms = get_facts(text)
for line in text:
  for term in keyterms:
    if term in line.lower().split(): correct.append(line)
correct = list(Counter(correct).keys())
print('\n'.join(correct))
