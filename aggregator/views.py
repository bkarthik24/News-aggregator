from django.shortcuts import render
import feedparser
import requests
import math

#Function to aggregate Top Stories
def topstories(request):
	label_list_index=0
	topstories_list=[]
	topstories_dict={}
	topstories_feed=[]
	label_list=['feed_one','feed_two','feed_three','feed_four','feed_five','feed_six','feed_seven','feed_eight','feed_nine','feed_ten','feed_eleven','feed_twelve','feed_thirteen','feed_fourteen','feed_fifteen','feed_sixteen']
	topstories_rss_url=['http://feeds.feedburner.com/ndtvnews-top-stories']
	for a in range(len(topstories_rss_url)):
		topstories_feed=feedparser.parse(topstories_rss_url[a])
		for d in topstories_feed.entries:
			for j in d.links:
				entities_list=[d.title,j.href,d.storyimage]
				for i in range(len(entities_list)):
					topstories_list.append(entities_list[i])
				topstories_dict.update({label_list[label_list_index]:topstories_list})
			entities_list=[]
			topstories_list=[]
			if label_list_index!=15:
				label_list_index=label_list_index+1
	return render(request,'aggregator/frontpage.html',{'content':topstories_dict})
#Function to aggregate World News
def worldnews(request):
	label_list_index=0
	worldnews_list=[]
	worldnews_dict={}
	worldnews_feed=[]
	label_list=['feed_one','feed_two','feed_three','feed_four','feed_five','feed_six','feed_seven','feed_eight','feed_nine','feed_ten','feed_eleven','feed_twelve','feed_thirteen','feed_fourteen','feed_fifteen','feed_sixteen']
	worldnews_rss_url=['http://feeds.feedburner.com/ndtvnews-world-news']
	for z in range(len(worldnews_rss_url)):
		worldnews_feed=feedparser.parse(worldnews_rss_url[z])
		for b in worldnews_feed.entries:
			for c in b.links:
				entities_list=[b.title,c.href,b.storyimage]
				for i in range(len(entities_list)):
					worldnews_list.append(entities_list[i])
				worldnews_dict.update({label_list[label_list_index]:worldnews_list})
				entities_list=[]
			worldnews_list=[]
			if label_list_index!=15:
				label_list_index=label_list_index+1
	return render(request,'aggregator/worldnews.html',{'world':worldnews_dict})

#Function to aggregate Sports News
def sportsnews(request):
	label_list_index=0
	sportsnews_list=[]
	sportsnews_dict={}
	sportsnews_feed=[]
	label_list=['feed_one','feed_two','feed_three','feed_four','feed_five','feed_six','feed_seven','feed_eight','feed_nine','feed_ten','feed_eleven','feed_twelve','feed_thirteen','feed_fourteen','feed_fifteen','feed_sixteen']
	sportsnews_rss_url=['http://feeds.feedburner.com/ndtvsports-latest']
	for z in range(len(sportsnews_rss_url)):
		sportsnews_feed=feedparser.parse(sportsnews_rss_url[z])
		for b in sportsnews_feed.entries:
			for c in b.links:
				entities_list=[b.title,c.href,b.storyimage]
				for i in range(len(entities_list)):
					sportsnews_list.append(entities_list[i])
				sportsnews_dict.update({label_list[label_list_index]:sportsnews_list})
				entities_list=[]
			sportsnews_list=[]
			if label_list_index!=15:
				label_list_index=label_list_index+1
	return render(request,'aggregator/sportsnews.html',{'sports':sportsnews_dict})
	
#Function to aggregate Business News
def businessnews(request):
	label_list_index=0
	businessnews_list=[]
	businessnews_dict={}
	businessnews_feed=[]
	label_list=['feed_one','feed_two','feed_three','feed_four','feed_five','feed_six','feed_seven','feed_eight','feed_nine','feed_ten','feed_eleven','feed_twelve','feed_thirteen','feed_fourteen','feed_fifteen','feed_sixteen']
	businessnews_rss_url=['http://feeds.feedburner.com/ndtvprofit-latest']
	for z in range(len(businessnews_rss_url)):
		businessnews_feed=feedparser.parse(businessnews_rss_url[z])
		for b in businessnews_feed.entries:
			for c in b.links:
				entities_list=[b.title,c.href,b.storyimage]
				for i in range(len(entities_list)):
					businessnews_list.append(entities_list[i])
				businessnews_dict.update({label_list[label_list_index]:businessnews_list})
				entities_list=[]
			businessnews_list=[]
			if label_list_index!=15:
				label_list_index=label_list_index+1
	return render(request,'aggregator/businessnews.html',{'business':businessnews_dict})
	
#Function to aggregate Tech News
def technews(request):
	label_list_index=0
	technews_list=[]
	technews_dict={}
	technews_feed=[]
	label_list=['feed_one','feed_two','feed_three','feed_four','feed_five','feed_six','feed_seven','feed_eight','feed_nine','feed_ten','feed_eleven','feed_twelve','feed_thirteen','feed_fourteen','feed_fifteen','feed_sixteen']
	technews_rss_url=['http://feeds.feedburner.com/gadgets360-latest']
	for z in range(len(technews_rss_url)):
		technews_feed=feedparser.parse(technews_rss_url[z])
		for b in technews_feed.entries:
			for c in b.links:
				entities_list=[b.title,c.href,b.storyimage]
				for i in range(len(entities_list)):
					technews_list.append(entities_list[i])
				technews_dict.update({label_list[label_list_index]:technews_list})
				entities_list=[]
			technews_list=[]
			if label_list_index!=15:
				label_list_index=label_list_index+1
	return render(request,'aggregator/technews.html',{'tech':technews_dict})
	
def entertainment(request):
	label_list_index=0
	entertainment_list=[]
	entertainment_dict={}
	entertainment_feed=[]
	label_list=['feed_one','feed_two','feed_three','feed_four','feed_five','feed_six','feed_seven','feed_eight','feed_nine','feed_ten','feed_eleven','feed_twelve','feed_thirteen','feed_fourteen','feed_fifteen','feed_sixteen']
	entertainment_rss_url=['http://feeds.feedburner.com/ndtvmovies-latest']
	for z in range(len(entertainment_rss_url)):
		entertainment_feed=feedparser.parse(entertainment_rss_url[z])
		for b in entertainment_feed.entries:
			for c in b.links:
				entities_list=[b.title,c.href,b.storyimage]
				for i in range(len(entities_list)):
					entertainment_list.append(entities_list[i])
				entertainment_dict.update({label_list[label_list_index]:entertainment_list})
				entities_list=[]
			entertainment_list=[]
			if label_list_index!=15:
				label_list_index=label_list_index+1
	return render(request,'aggregator/entertainment.html',{'entertainment':entertainment_dict})