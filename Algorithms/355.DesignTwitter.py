class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = {}
        self.tweets = {}
        self.index = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId in self.tweets:
            self.tweets[userId].add((self.index, tweetId))
        else:
            self.tweets[userId] = {(self.index, tweetId)}
        self.index += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        users = {userId}
        if userId in self.following:
            users.update(self.following[userId])
        tweets = []
        for user in users:
            if user in self.tweets:
                tweets += list(self.tweets[user])
        tweets.sort(reverse=True)
        tweets = tweets[:min(len(tweets), 10)]
        return [tweetId for i, tweetId in tweets]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
