from os import name
import string

class Social_media:
    def __init__(self,name:string):
        self._name=name

    @property   
    def getName(self):
        return self._name
     
 
         
class Instagram(Social_media):
    def __init__(self, name:string,language:string,post_list ):
        super().__init__(name)
        self._language=language
        self.post_list=[] 

    def getPost(self):
        return self.post_list

    def PublishNewPost(self):
        postIn=input("please enter your post\n")
        print("\n")
        print("your post is:")
        print(postIn)
        if len(postIn) < 2200:
            self.post_list.append(postIn)
        else:
            print("Post Can't Be Inserted")
            print("Please Reduce The Number Of Characters")    

 
   
class Twitter(Social_media):
    def __init__(self, name:string,langu:string,tweets_list):
        super().__init__(name)
        self._langu=langu
        self.tweets_list=[]

    def getTweeter(self):
        return self.tweets_list

    def CreatNewTweeter(self):
        tweet=input("please enter your tweet\n")
        print("\n")
        print("your tweet is:")
        print(tweet)
        if len(tweet) < 280:
            self.tweets_list.append(tweet)

        else:
            print("Tweet Can't Be Inserted")
            print("Please Reduce The Number Of Characters") 
            
 

t1=Twitter("tw1","Persian",[])
t1.CreatNewTweeter()  
print(t1.getTweeter())

i1=Instagram("in1","English",[])
i1.PublishNewPost()
print(i1.getPost()) 