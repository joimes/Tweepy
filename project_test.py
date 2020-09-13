import tweepy           #imports the package so that it can be used for this Python file.

#Declaring and Initializing key variables that will allow us to connect to the Twitter API
#Thus allowing access to the tools and features mentioned previously.
#Consumer key and secret are kind of like a (Twitter handle's) ID key and Password key
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
#Log in to Tweepy using your ID key and Password key
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


# All actions will now be based off of your Twitter ID and not someone elses.
#special access ID and Password given by dev.Twitter.com that allows us to connect to the API
access_token = 'token'
access_token_secret = 'token_secret'
#Take the 2 keys given by dev.Twitter.com and combine them with your "username and password keys"
auth.set_access_token(access_token, access_token_secret)
#Establish access to the Twitter API via using all four keys.
api = tweepy.API(auth)

# main menu
def main_menu():
    menuError = True
    while menuError == True:
        print("Main Menu\n")                                                            #Print "Main Menu" and skip to the next line
                                                                                        #Ask the user for an input ("1"-"5") and store their response into response_main_menu
        response_main_menu = input(
            "1) Post a tweet (press 1)\n2) Get user information (press 2)\n3) Display Tweets based on keyword (press 3)\n4) Display Worldwide trends (press 4)\n5) Display most recent Timeline (press 5)\n")
#1 Post a tweet
        if response_main_menu == "1":
            tweet = input('What would you like to post?')                               #Ask the user what they want to post and store it into a variable
            api.update_status(tweet)                                                    #This line communicates with the API to send your tweet
            print("You tweeted: " + tweet)                                              #Just confirmation that the tweet went through
            menuError = False
#2 Get user information
        elif response_main_menu == "2":
            nameError = True                                                            #Boolean that controls the loop.
                                                                                        #I chose nameError because an error can occur if you don't type a real Twitter username that exists
            while nameError == True:
                try:
                    twitter_username = input('Type in a Twitter username\n')            #Ask the user for an input and store it into a variable
                    user = api.get_user(twitter_username)                               #Take that input from the user to lookup various traits the user can have. Store it into a variable. #Error?
                    screen_name = user.screen_name
                    location = user.location
                    user_id = user.id
                    description = user.description
                    print(
                        f"\nThe user's screen name is {screen_name}.\nThe id is {user_id}.\nThe description of the user is {description}.\nThe location of the user is {location}.") #Print various traits
                    nameError = False
                except Exception:                                                       #If there is an error, the loop jumps straight to here
                    print('Invalid Twitter username. Please try again. \n')             #Prompt the user that he/she messed up
                    nameError = True                                                    #Force us back into the loop until a valid username is entered.
            menuError = False
#3 Display Tweets based on keyword
        elif response_main_menu == "3":
            keyword = input('What keyword would you like to search?\n')                 #Ask the user for an input and store it into a variable
            n = 0                                                                       #Placeholder for "count"
            for tweet in api.search(q = keyword, lang = "en", rpp = 10):                #Loop that chooses a keyword and displays the latest tweets that use that same keyword
                n+=1                                                                    #Increase count by 1
                print(str(n) + ") " + tweet.text)                                       #Print count followed by the tweet
            menuError = False
#4 Display trends
        elif response_main_menu == "4":
            print('Now displaying Worldwide trends from Twitter.com\n')                 #Letting the user know he chose selection #4
            trend_results = api.trends_place(1)                                         #api.trens_place(1) is a HUGE JSON string
            n = 0
            for trend in trend_results[0]['trends']:                                    #For each trend in trends, go thru the trend_results(JSON String) and pull out ONLY the data we need
                n+=1
                print(str(n) + ") " + trend['name'] + "\t \t \t \t \t \t \t \t"  + trend['url'])    #Prints the name of trend and its URL
            menuError = False
#5 Display timeline
        elif response_main_menu == "5":
            timeline = api.home_timeline()                                              #api.home_timeline() is also a HUGE JSON string that displays everything on your timeline
            print("Now displaying your timeline.")
            n = 0
            for tweet in timeline:                                                      #Now for each tweet in the timeline, we are going to only pull out 2 things. The tweet + the author.
                n+=1
                print("\n" + str(n) + ") " + tweet.text + "\n@" + tweet.user.screen_name + "\n")    #Prints the count, followed by the tweet, followed by the username.
            menuError = False
        else:
            print("\n*****Invalid response. Please try again.*****\n")
            menuError = True
main_menu()
