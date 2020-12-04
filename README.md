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
2. Include limitations of the current data set
    * It would be good to have the control group stats to verify the mean and standard deviations line up with our test group
    * Small error in the dataset key. 'Purchase Product' 1-4 says null if > x products purchased. It should say < x
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