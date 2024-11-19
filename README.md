# SandlinesScraper
Code for web scrapers to analyze political sentiment on various issues based on the news and social media.
Project inspired by: Miftahul Qorib, Rahel S Gizaw, and Junwhan Kim. 2023. Impact of Sentiment Analysis for the 2020 U.S. Presidential Election on Social Media Data. In Proceedings of the 2023 8th International Conference on Machine Learning Technologies (ICMLT '23). Association for Computing Machinery, New York, NY, USA, 28–34. https://doi.org/10.1145/3589883.3589888

A public sentiment model that can determine subsets of public opinion on specified issues.
Potential uses include:
- Local election predictions
- Inform marketing efforts and allow for more accurate targeted advertisements

11/19: Research Web Scraping Methodologies for relevant Social Media Platforms
- Scraped Data Storage: JSON? MongoDB? SQL?
- MongoDB Database: https://cloud.mongodb.com/v2/673cee9dc464e07dbea515ea#/overview
- APIs Used: Praw, Reddit
- Methods of Analysis: Keywords, Sentiment Analysis
- API vs HTML web scraping? (API access to the website data is far more scalable and adaptable)(My understanding is that HTML web scraping is for one time analysis and not concurrent live scraping)


Reddit:

Praw Documentation: https://praw.readthedocs.io/en/stable/code_overview/reddit_instance.html
Access to Reddit API: https://www.reddit.com/prefs/apps


NextDoor:
Public repository of a NextDoor scraper that could be potentially used and modified (currently exports to a csv file): https://github.com/chanwooh/Nextdoor-Script
