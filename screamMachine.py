#!/usr/bin/python
import random

#TODO: tweets types (bland, hashtag heavy, super general, song), deciding link format, 
localTagList = ['dc', 'dmv', 'dcmusic', 'dmvmusic', 'novamusic', 'arlingtonva', 'alexandriava', 'ustreet', 'dcrock', 'dcfolk', 'dcarts', 'nova', 'md', 'mdmusic']
generalTagList = ['music', 'folk', 'acoustic', 'awesome', 'song', 'indiemusic', 'localmusic']
openerList = ['You gotta see this', 'Better than Nickelback?', 'Reviewing #dc venues', '#DC review', 'Classic blopost', 'The best bloggers in DC?']
reviewLinksList = ['thecapitolheights.com/?p=2460', 'thecapitolheights.com/?p=2321', 'http://www.thecapitolheights.com/?p=2211', 'http://www.thecapitolheights.com/?p=2122']
songLinkList = []

def chooseLocalTag():
        index = random.randint(0, len(localTagList)-1)
        return localTagList[index]

def chooseOpener():
        index = random.randint(0, len(openerList)-1)
        return openerList[index]

def chooseLink():
        index = random.randint(0, len(reviewLinksList)-1)
        return reviewLinksList[index]

def createTweet():
        opener = chooseOpener()
        link = chooseLink()
        localTag = chooseLocalTag()
        print str(opener) + ' ' + str(link) + ' #' + str(localTag)

#tweet = createTweet(opener, link, localTag)
i = 0
while i < 20:
        print str(createTweet())
        i = i + 1



