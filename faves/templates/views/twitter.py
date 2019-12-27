import twitter
from django.http import HttpResponseRedirect
from django.urls import reverse

from myfaves.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_ACCESS_TOKEN_KEY, \
    TWITTER_CONSUMER_TOKEN_SECRET

TWITTER_API = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                          consumer_secret=TWITTER_CONSUMER_SECRET,
                          access_token_key=TWITTER_CONSUMER_ACCESS_TOKEN_KEY,
                          access_token_secret=TWITTER_CONSUMER_TOKEN_SECRET)


# TODO implement add_twitter_user
def add_twitter_user(request, sport):
    print(add_twitter_user.__name__)
    print(request)
    print(request.get_full_path())
    print(sport)
    if request.method == 'POST':
        user = request.POST.get('add_twitter_user', None)
        print(user)
        # print(users_nba)
        # messages.info(request, 'Successfully added user' + user)
        try:
            data = TWITTER_API.GetUserTimeline(screen_name=user, count=5)
            # print(new_tweet)
            # print(new_tweet.id)
            if (sport.lower() == "nba"):
                print("nba!!!")
                # for new_tweet in data:
                #     users.add(user)
                #     if not any(new_tweet.id == tweet.id for tweet in tweets):
                #         tweets.add(new_tweet)
                #
                # sorted_tweets_nba = sorted(tweets,
                #                            key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                #                            reverse=True)
                return HttpResponseRedirect(reverse('faves:nba_tweets'))

            elif (sport.lower() == "mlb"):
                print("mlb!!!")
                # for new_tweet in data:
                # users_mlb.add(user)
                # if not any(new_tweet.id == tweet.id for tweet in tweets_mlb):
                #     tweets_mlb.add(new_tweet)

                # sorted_tweets_mlb = sorted(tweets_mlb,
                #                            key=lambda d: datetime.strptime(d.created_at, '%a %b %d %H:%M:%S %z %Y'),
                #                            reverse=True)
                return HttpResponseRedirect(reverse('faves:mlb_tweets'))

        except Exception as err:
            print(err.message)
            for i in err.message:
                print(i)
