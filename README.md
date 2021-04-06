# Shark Attack

This project had two main objectives:
* Clean up the data to make it usable.
* Find useful information within said clean data.

## Getting Started


The initial database had a few big problems and a lot of small ones, the most notable being that over 65% of the rows were filled with NaN rows that were useless for the database and had no meaning. 

### The cleanup

Getting that cleaned and ready to go sent us looking at the columns, there were several that were either repeated or just obsolete data. Fixed column names that had extra characters in it, like the ‘Sex’ column that had an extra space after it.

We also transformed all the dates to datetime64 format and converted it to numbers to make comparisons easier, to finish we ordered all the attacks listed based on the column ‘Date’.

### The data to use.

Having dropped all those rows and columns we finally had useful data to start our analysis. You can compare both the initial database and the sanitized one in the folder data, the initial database is in the “attacks.csv” file and the cleaned up version is in the “shark_attack_clean.csv” file.

## The Shark Stats

With the clean data we finally could start taking a peek at it and what conclusions we could reach with it.

### The gender disparity, are sharks sexist? 

Right off the bat we took a look at the amount of attacks by gender and instantly look at the absurd disparity between the genders with Male victims representing over 88% of all victims and Female victims coming in just short of 12%.

So are sharks inclined to attacking male humans only or is there something more to it? Not really as we’ll see.

### What were the victims of the attacks doing?

After wondering a bit as to why sharks were disproportionally attacking Males we took a brief look at the top ten activities being done when the attack happened:

```
Surfing         20.37%
Swimming        15.44%
Fishing         06.49%
Spearfishing    05.53%
Wading          02.77%
Bathing         02.30%
Standing        01.95%
Snorkeling      01.72%
Diving          01.57%
Scuba diving    01.45%
```

These 10 activities represent 59.60% of all activities being performed in the data, as we can see most are activities that attract a disproportionally high number of males compared to females, when we look at Surfing, the top activity on the list we can see that according to this [Surfer Today article](https://www.surfertoday.com/surfing/how-many-surfers-are-there-in-the-world), Men represent about 81% of the surfers worldwide, a number quite close to the proportion of attacks, if we include the third activity, Fishing, one that attracts an even bigger number of Males to Females participants, we can start to understand why sharks tend to get a taste of men and not so much women, the key reason being opportunity.

## Why are sharking getting more aggressive as the years go by?

As can easily be seem on the data, the number of yearly Shark Attacks registered has risen by an absurd amount and a plethora of reasons such as the exponential growth of the human population in the last 100 years, humans starting to expose themselves more to these attacks by performing high risk activities, the overfishing of the seas depleting the sharks food supply making sharks take more risks to eat, among many other imaginary reasons this study has finally found an answer.

### Correlation vs Causation

As anyone who has ever read a single page of an Statistics book (and not a single page more) might be able to tell you that correlation does imply causation in every single case. There's a lot of cases that prove such a statement, one of the most famous being that the serious decline in the number of pirates has directly led to Global Warming, another is the direct correlation between the drop in Internet Explorers market share and US Murder Rates, as such we can conclude that if no one used Internet Explorer again, there wouldn't be any more murders.

Utilizing this cutting edge methodology we were able to find the culprit behind all these Shark getting more aggressive as the years go by.

### The Band AC/DC

We clearly identified two important things the band AC/DC as one of the main causes of rising Shark Attacks and that Sharks have great taste in music. When we look at every single studio album that AC/DC released and look at the 12 months prior
