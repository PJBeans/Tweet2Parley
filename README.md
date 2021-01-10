# Tweet2Parley
Tweet2Parley finds tweets from Twitter and sends them as parleys to Parler.

**DISCLAIMER:** We have absoultely NO political affiliation nor preference. Say what you will about both Parler and Twitter, their user bases, and ideologies; our goal is simply to make all information as accessible as possible.

Tweet2Parley attempts to fill in the gap left by larger, mainstream Twitter accounts who do not have Parler. It is designed as a solution to help move from Twitter to Parler entirely. Currently, it only forwards tweets from a select few accounts (some important, many... not so important :)  )

## How does it work:
There is a "forward list" called "scrapeUsers." The bot will search for the past 25 tweets made by each user in that list. If it finds a tweet, AND that tweet was tweeted on the same day it was found (i.e.: if the tweet was made today), *AND* that tweet hasn't been forwarded to Parler already, a new Parley is created in the following format:
```
@#twitterUserX tweeted:
wow this is insane
im vibing with the cows right now

but wait, what time is it?
Oh no i need to take my #ibuprofen
(Tweeted on 2020-01-09 at 12:01:05)
```
and includes a link to the original tweet. Unfortunatly, links included in tweets are removed and added to the array at the bottom of each Parley, but that's probably the only formatting issue.

The bot waits 15 seconds between sending a new parley, and 30 minutes between "scraping sessions," to avoid potentially overloading Parler's servers. These time limits can be increased should the Parler staff complain. 

## Can I Contribute?
Please! Feel free to modify this bot if you have some neat ideas. Another great way to contribute is to add Twitter accounts you'd like this bot to scrape, by either creating a pull request or sending a message to @Tweet2Parley on Parler.
### Criteria for adding Twitter accounts:
- They should have some sort of national or global significance (such as POTUS, companies, or large organizations)
- They should NOT have a Parler account (as this would create redundancy). If a user in the forward list creates a Parler account, they should be removed.
- The account should not promote nudity, violate Parler ToS (or for that matter, Twitter ToS as well), be designed to scam or spam, nor promote/contain illegal content (such as CP, selling illegal drugs, etc)

## To Do:
- Automate adding accounts. Currently, it is not possible to search/scrape Parler for data or keywords. If such a method becomes possible, may account creation can be automated by Parleying something like `Follow TwitterUserX @Tweet2Parley`. (All ears on suggestions to automate this process now, though!)

You can message @Tweet2Parley on Parler to request for Twitter accounts to be added, or create a pull request here.

Note that the Parler API we use is unofficial; as such, we understand we must do everything we can to prevent getting banned from the platform. We have absoultely no intention to spam. Such parleys (such as from a hacked Twitter account in the forward list) will be deleted ASAP.
