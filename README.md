# outdoor_AB
Evaluate an AB test for an outdoor retailer

# Remove later
Evolytics is working with an online retailer who specializes in outdoor gear. The retailer already has an A/B testing team
and a strong culture of optimization. They engaged with Evolytics to help create a more structured strategy for testing and
augment the team by providing post-test analysis.
The test you’re analyzing was created to drive sales of premium hiking products; it suggested a product upgrade
whenever a customer added hiking gear to their cart. Two things happened:
1. The premier-line product owners deemed the test a success because the upgrade message (Recipe B) drove
incremental premier-line sales.
2. Overall the test experience conversion (orders/unique visitors) indexed below the control experience (80 index) as
did overall revenue (95 index), and the hiking product owner deemed the test a failure.
“I hate calling this test a failure because we exceeded our goal on premier-line products,” the hiking product owner said to
you during a post-test analysis meeting. “How can we iterate this test to continue beating our premier-line product goals
without harming conversion in the overall hiking category? If we wanted to personalize the experience in the next iteration,
what would you recommend?”
The client has sent you a data set from those customers who were in Recipe B, “The Upgrade Experience” to answer
these questions.
Deliverables
1. Create a 15-minute insights & recommendations presentation that you will present to the client team
    * I believe the obstrusiveness of the popup is what is driving away 20% of conversions. I would recommend a less in-your-face 
    suggestion such as displaying it alongside cart information instead of a dedicated popup that needs to be addressed.
    * * if we take a look at how REI does it here, we can see they take every opportunity to display their recommender system (bottom of shop, cart add, cart itself)
    ![C:\Users\jonma\Programming\outdoor_AB\img\REI-upsell-12-5_Trim.gif]
    You might be targeting just the premier line right now, but if we tailor it based on the customer, you'll see sales respond.
    For this you can use:
    Collaborative filtering
        for collab based filtering, I consulted on a project that used AWS ElasticSearch to great results
        ![https://towardsdatascience.com/how-to-build-a-recommendation-engine-quick-and-simple-aec8c71a823e]
    Content-Based Filtering
    A mix of the two

    If you want assistance with design, here at Evolytics we can leverage our experience from our big name clients and their successes...

    Now if you do just want to target the premier line only, we can weight the premier line to show up more often in the recommended, or we can make a model to predict users that are more likely to take the upsell. To do that, effectively we need more data, let's take a look at the limitations of the current dataset....
2. Include limitations of the current data set
    * It would be good to have the control group stats to verify the mean and standard deviations line up with our test group. make sure done randomly
    * Small error in the dataset key. 'Purchase Product' 1-4 says null if > x products purchased. It should say < x
    * Data is only from a couple months in two years, can't see seasonality well
    * Need all user data and product meta data to build the most efficient model for recommendations and everything else, whether this user would respond to coupons

    with that though here's what I found: vis, models not great but can produce the users with the highest probs. If you wanted to lessen the blow to conversions, you could send the message to only those who are more likely to respond favorably--this is a balancing act and will require you to choose a threshold. Again, with better data I could make a more competent model but here's the process.

    I heard that you often use Alteryx in your business so I picked it up and made a prototype app that you can play with.

    Summary: Reduce obtrusiveness of message. Investigate more comprehensive recommendation system. Expand data management/engineering. Profit!
3. Include an appendix with assumptions, methods and relevant statistical output
    * SEM is paid ad search result, SEO is organic search result

## Plan

1. brush up on A/B Testing
2. exploratory analysis with perhaps visualization
    i. convert start time and end time to visit time
    conversion (orders/unique visitors) is the goal so 
3. answer prompts
    * cluster customers that responded well to the msg and those who didn't
    * * Actually it seems like a much simpler classification problem. Classify users as one who would click yes vs those who would not
    * make custom outputs for those conditions
    * * careful what you may be able to predict on, you can't decide to administer the B-test after using factors from your B-test
4. potential alteryx, app
5. work on presentation

Project setup at start, eexplain target. This is what i would do in that situation, what skills you used to be positive. Result focused structure.
Deep dive in job description for behavior questions. take initiative to say hi

These are the things that would make this an easy yes. Since i'm not in missouri, is there an option to stay remote, maybe travel once a month. One bucket, not constantly.

have questions prepared. Blog . why do you want to work here