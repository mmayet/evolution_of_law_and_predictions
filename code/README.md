# The Process

## 0. The Questions: 
1. Which words and phrases are the most specific to each school? (i.e., do *Ḥanafī* works often cite *“qiyās”* far more than *Ḥanbalī* works do?)
2. How do those school-specific words and phrases change from century to century? (i.e., do the earlier works predominantly quote *Qurʾān* and *Aḥādīth*, while later works simply reference back to the opinions of previous scholars?)
3. Can I provide valuable book recommendations that would leave the reader satisfied with the suggested texts?
4. [*To be addressed in future iterations*] Can these keywords and phrases be used to accurately predict with which *madhhab* an author affiliates? (i.e., do the *ḥadīth* commentaries of Mullā ʿAlī al-Qārī [rḥA] and Imām al-Nawawī [rḥA] clearly mark them as *“Ḥanafī”* and *“Shāfiʿī”* respectively?)
5. [*To be addressed in future iterations*] Can I provide a summary of the texts in a manner that is both inclusive and exclusive, but still staying true to the original intent of the author?
*The full statement can be found in the [directory above](../)*

## 1. Getting The Data: [01_data_collection](01_data_collection)
1. Gather all relevant links, site trees, and tags.
2. Scrape all relevant pages, and books.
3. Clean book files, and fill in any missing data.

## 2. Exploring The Data: [02_eda](02_eda)
1. Check data, and books
2. Visualize distribution of authors, words, books, schools to be able to understand how the relate to one another, and how this will possibly effect the models that will come from this data.

## 3. Model The Data: [03_key_phrases_and_time](03_key_phrases_and_time) & [04_recommendations](04_recommendations)
There are two places wherein the data are modeled. 
1. To answer **Question 1 & Question 2**, the modeling process takes place [03_key_phrases_and_time](03_key_phrases_and_time).
	- This is where the data are split up into categories to answer **Question 1**
	- This is where the data are split up by time to answer **Question 2**
	- This is where the data are combined to answer **Question 4** [*To be addressed in future iterations*]
2. To answer **Question 3**,, the modeling process takes place [04_recommendations](04_recommendations).
	- This is where the data are converted into vectors with quantitative distances.

## 4. Evaluating The Model: [03_key_phrases_and_time](03_key_phrases_and_time) & [04_recommendations](04_recommendations)
There are two places wherein the data are modeled. 
1. To test the models built for **Question 1 & Question 2**, the evaluation process takes place [03_key_phrases_and_time](03_key_phrases_and_time).
	- This is where the model is tuned to provide the best most coherent results to **Question 1 & Question 2**
	- This multi-class classification model will be evaluated to answer **Question 4** [*To be addressed in future iterations*]
2. To test the models built for **Question 3**, the evaluation process takes place [04_recommendations](04_recommendations).
	- This is where the the recommendations are checked.

## 5. Answering The Questions
***The answer to each of the questions can be found within the folder/notebooks specified above. Below is a brief summary.***

#### Question 1:
- It's very shocking to see that `Abū Ḥanīfah` and `Shāfi'ʿī` are referenced so often. It's bizarre that they have a `TFIDF` of 3.5-4, whereas `Mālik` is at 0.2.
- `Ḥanbalīs` and `Shāfiʿīs` tend to quote a lot of narrations.
- `Shāfiʿīs` particularly rely heavily on Bukhārī and Bayhaqī
- `Ḥanbalīs` use most books, but are rare to use Bukhārī, Abū Dāwūd, and Muwaṭṭāʾ
- `Mālikīs` heavily use Muslim, Muwaṭṭāʾ (written by Mālik himself), and Abū Dāwūd.
- `Ḥanafīs` tend to use Abū Dāwūd and Darquṭnī.
|  Ḥanafī  |   Mālikī   |   Shāfiʿī  | Ḥanbali  |
|:--------:|:----------:|:----------:|----------|
|  Fatāwa  | Mukhālafah |   Ijtihād  | Khawf    |
|   Qiyās  |   Fitnah   |    Balwā   | Ijtihād  |
| Istiḥsān |    Khawf   |    ʿUrf    | Ijmāʿ    |
| Mursalah |            |  Maṣlaḥah  | Maṣlaḥah |
|   Farḍ   |            | Mukhālafah | Fitnah   |
|  Iḥtiyāṭ |            |            |          |

#### Question 2:
***In regards to codifiers***
Here we see some trends that are expected, and others that aren't.
Expected:
- Heavy reference to `Mālik` by early Malikīs.
- Heavy reference to `Aḥmad` in the first generation of `Ḥanbalīs`. This is most likely due to the first 4-6 works in that era being of the type "The Opinions of Imām Aḥmad by *such and such* student".

Somewhat Expected:
- Heavy reference to `Abū Ḥanīfah` by not only mid-generation Ḥanafīs but also Shāfiʿīs. This is expected, but the fact that the references sky rocket during the 700's in an interesting thing to note.

Unexpected:
- Extremely high amount of references to `Aḥmad` in moden times by Ḥanbalīs.
- `Shāfiʿī` being referenced a lot throughout the generations. Especially the huge spike in the first generation of Mālikīs.

Overall Insights:
`Abū Ḥanīfah` and `Shāfiʿī` are referenced often by all 4 schools, and this has been a continuous trend over the centuries.

***In regards to legal terms***
`Qiyās` [Analogical Reasoning] is something that `Ḥanafīs` are known for. Although they are the most consistently dominant users of that phrase, there is an add jump with medieval `Mālikīs` who heavily used that phrase. This is probably a result of heavy Mālikī influence and control in Muslim Spain, and when faced with many new issues — while being the primary law makers of that era — turned to `Qiyās` [Analogical Reasoning] to formulate law in a suitable manner.

`Istiḥsān` [Preferring a less common source of law over analogy] is a method of law used almost exclusively by the `Ḥanafīs` and that is quite clear.

`Ijmāʿ` [Scholarly Agreement] is used by all the schools, however we see that over time, especially at the turn of the lunar millennium, there was a huge use of `Ijmāʿ`. This could be a result of many new ideas being incorporated into the religion as a result of colonialism and European powers brainwashing the masses, and the scholars reacting with a concept of "this has always been in Islam."

Interesting, since *`balwā`* is often thought to be a *`Ḥanafī`* phrase.

`ʿUrf` [Societal Norms] are, in books, seen as a back and forth issue, but we can see that, aside from a drop in its use by the medieval `Mālikīs`, it's become a more common place legal term. Another thing to note, which is extremely surprising, is that, medieval `Mālikīs` heavily referenced `Qiyās` but used very little `ʿUrf`.

In the context of `al-Maṣlaḥah al-Mursalah` [Common Good] isn't used often, but the `Ḥanafīs` did make a strong use of it in the 900s. Probably as a result of government power involving `Ḥanafī` judges.

`Ḥanafīs` used increasingly more `Iḥtiyāṭ` [Caution] over the years, with a heavy drip in recent years.

`Ḥanbalīs` have seen a huge influx in `Fitnah` [Societal Issues] arise in the last generation.

***In regards to source narration***
Overall, when it comes to using `Ḥadīth` as a source, there has been an increase. Most schools have had an era of heavy ḥadīth usage, and that is probably in part by the schools starting to refute other opinions within their texts, and using narrations as a backup proof.
