import os
from gensim.summarization.summarizer import summarize

conversation = [
    {
        'userID': 0,
        'messageID': 0,
        'body': "What's your favourite programming language? ",
        'timestamp': 1545730073
    },
    {
        'userID': 0,
        'messageID': 1,
        'body': "My preferred language is C#. Strongly typed, beautifully designed, has nearly every major language feature you could ever want, great framework, cross platform, fast, and can be used for damn near anything. It can even be run in the browser now.",
        'timestamp': 1545730073
    },
    {
        'userID': 1,
        'messageID': 2,
        'body': "Did I miss something? C# is the primary language I work with, and I thought I stayed on top of all the news for it, but I haven't heard of this. I have to agree with your praise of the language. I've used it professionally since .NET 2.0, and I've seen this language evolve from a basic Java clone to be one of the best languages to work with. That being said, I'm starting to get bored with it. I've been spending some time learning Kotlin for native Android development, and I have to say, Microsoft should start borrowing features from that language. So much of that language is just little quality-of-life features. For example, in Kotlin, if you have a lambda that takes one parameter, you don't have to specify it, it has a keyword (it): Also note that since the lambda is the last parameter the method expects, it does not need to be contained in parenthesis (and since it's the only parameter expected, you can omit the parenthesis. Just lots of little things like that that make the language simpler for the developer to write is what's making me love it.",
        'timestamp': 1545730123
    },
    {
        'userID': 0,
        'messageID': 3,
        'body': "Python! I learned a little of it in highschool but Microsoft had it's clutches around the school so I got to learn C# instead. Got a job right out of highschool fixing devices for schools. Quickly(ish) worked my way up to working in spreadsheets and sometimes the database. In the past 3 months I've gotten back into it and with it and I've automated a lot of stuff for my job I've reduced 1-3 hours of daily work to ~10 minutes and (hopefully) within the week I'll be doing the same for a co-worker. I've made far more useful programs in my short time with Python than I did with 2+ years with C#. Though the exact moment when I fell in love with Python was when I was having a bad day and something reminded me of the Python xkcd. I almost made a squeak in the completely silent office when I imported antigravity and it opened the xkcd page. Probably the happiest I've ever been.",
        'timestamp': 1545730224
    }, 
    {
        'userID': 0,
        'messageID': 4,
        'body': "I would love to see the stuff you have automated, just to get an idea of the capabilities of python. mind sharing? Thanks",
        'timestamp': 1545730325
    }
]

# gets every line of conversation in order it was sent 
sentences = [sentence['body'] for sentence in (sorted(conversation, key=lambda x: x['timestamp']))]

summary = summarize(". ".join(sentences), word_count=30)
print(summary)


