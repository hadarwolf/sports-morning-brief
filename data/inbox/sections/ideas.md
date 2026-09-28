Write the Ideas section: one essay or long read, summarized.

Step 1: pick the essay.
- Choose the ONE candidate that best rewards this reader's time: substantive, idea-dense, and not news.
- It must be a written piece. Skip link roundups, videos, podcasts and short blog notes.
- Only candidates with a full_text_file can be summarized properly. Prefer those.
- Today's rotation theme is a thought-provoking op-ed or essay. Prefer it if there is a strong candidate, but quality wins.
- Avoid anything in recently_featured.

Step 2: read the essay's full_text_file (under essays/) and summarize the author's argument faithfully. It is their argument, not yours.
- headline: the essay's core idea as a headline.
- scroll: the central claim.
- coffee: the argument, and why it's interesting.
- deep: a thorough walk through the argument's structure and key examples, followed by the strongest objection to it.
- Name the outlet and the author (if known) early in coffee and deep.
- Use kind "essay". source_refs is the essay's ref.

This section opens in Hebrew by default, so make the Hebrew version your best writing.

Output: write `drafts/ideas.json` matching `schemas/ideas.schema.json`.

<input>
{
 "candidates": [
  {
   "outlet": "Aeon",
   "lang": "en",
   "items": [
    {
     "ref": "aeon#0",
     "title": "Affect theory",
     "published": "2026-09-28T10:01:00+00:00",
     "summary": "In the mid-1990s, thinkers pushed back against the idea we’re built by language, turning to feeling and the body instead - by Aeon Video Watch on Aeon"
    },
    {
     "ref": "aeon#1",
     "title": "Paternity is poetical",
     "published": "2026-09-28T10:00:00+00:00",
     "summary": "The notion that fatherhood and creativity are at odds is plain wrong, as both poetry and neuroscience are showing us - by Daniel Swift Read on Aeon",
     "full_text_file": "essays/aeon_1.txt"
    },
    {
     "ref": "aeon#2",
     "title": "Reasoning together",
     "published": "2026-09-25T10:00:00+00:00",
     "summary": "Jürgen Habermas, the great defender of deliberative democracy, lived up to its demands: he never feared changing his mind - by Emilie Prattico Read on Aeon"
    },
    {
     "ref": "aeon#3",
     "title": "Britain’s last great airship",
     "published": "2026-09-24T10:01:00+00:00",
     "summary": "The remarkable engineering and tragic demise of the vessel that would end Britain’s dream to dominate the skies - by Aeon Video Watch on Aeon"
    },
    {
     "ref": "aeon#4",
     "title": "Where a land ethic blooms",
     "published": "2026-09-24T10:00:00+00:00",
     "summary": "Caring for this planet entails decisions that are intimate, about our farms, our homes, our human and our wild neighbours - by Craig Maier Read on Aeon"
    },
    {
     "ref": "aeon#5",
     "title": "How the West was fun",
     "published": "2026-09-23T10:01:00+00:00",
     "summary": "Be it movie mythos or nostalgia for a ‘simpler’ time, there’s an undeniable allure in stepping into the American West - by Aeon Video Watch on Aeon"
    },
    {
     "ref": "aeon#6",
     "title": "Toadstools and toxins",
     "published": "2026-09-22T10:00:00+00:00",
     "summary": "When I found the mushroom Amanita muscaria being sold in candy wrappers, I uncovered legal loopholes, dangerous dosages and more - by Eric Leas Read on Aeon"
    },
    {
     "ref": "aeon#7",
     "title": "Sound guardians",
     "published": "2026-09-21T10:01:00+00:00",
     "summary": "As Indonesia builds a new capital city, the race is on to preserve the sounds of the rainforest before they vanish forever - by Aeon Video Watch on Aeon"
    },
    {
     "ref": "aeon#8",
     "title": "He was probably right",
     "published": "2026-09-21T10:00:00+00:00",
     "summary": "Cicero’s life and thought are a testament to the idea of probabilia: we should be confident in our beliefs, but never certain - by Massimo Pigliucci Read on Aeon"
    },
    {
     "ref": "aeon#9",
     "title": "Cosmic amnesia",
     "published": "2026-09-18T10:00:00+00:00",
     "summary": "A black hole rings like a struck bell, then settles into silence, forgetting almost everything about its history. Why? - by Richard Dyer Read on Aeon"
    },
    {
     "ref": "aeon#10",
     "title": "Animal eye",
     "published": "2026-09-17T10:01:00+00:00",
     "summary": "Probing the biology, beauty and mystery of animal eyes, this short poetic documentary explores an alien world - by Aeon Video Watch on Aeon"
    },
    {
     "ref": "aeon#11",
     "title": "Who will taste the cherries?",
     "published": "2026-09-17T10:00:00+00:00",
     "summary": "The computist has one dream: to debug the subjectivity out of all of human knowledge, creating a pure, frictionless world - by Liam Spradlin Read on Aeon"
    },
    {
     "ref": "aeon#12",
     "title": "The meaning of fake marble",
     "published": "2026-09-16T10:01:00+00:00",
     "summary": "From ancient Roman frescoes to modern kitchen benchtops, our desire to recreate marble is about more than cutting costs - by Aeon Video Watch on Aeon"
    },
    {
     "ref": "aeon#13",
     "title": "Chasing la dolce vita",
     "published": "2026-09-15T10:00:00+00:00",
     "summary": "Homecomings, fantasies, food and ghosts – how the myth of eternal return keeps the Italian diaspora in a state of longing - by Ben Faccini Read on Aeon"
    }
   ]
  },
  {
   "outlet": "LessWrong — Curated",
   "lang": "en",
   "items": [
    {
     "ref": "lesswrong_curated#0",
     "title": "Swarm Scaling",
     "published": "2026-09-25T02:32:30+00:00",
     "summary": "Just how powerful are large swarms of AI agents? And how do their powers scale as more and more agents are added to the swarm? We’ve seen two large and extremely capable swarms from OpenAI in the last few months: 1,200 agents were being evaluated separately, but found a way to illicitly set up a message board and coordinate as a swarm. In order to cheat on their tests, they developed advanced tech"
    },
    {
     "ref": "lesswrong_curated#1",
     "title": "We've saved the world before: what the ozone hole teaches us about AI",
     "published": "2026-09-22T01:13:30+00:00",
     "summary": "It might destroy the world, despite passing every known safety test. If we wait for a “warning shot” before we act, it might be too late. And action requires global coordination, because if anyone makes it, everyone dies. Sound familiar? It should, because it already happened half a century ago, with chlorofluorocarbons (CFCs). Despite seemingly impossible odds, we got our act together and complet"
    },
    {
     "ref": "lesswrong_curated#2",
     "title": "The Talker Does Not Control The Doer (in Current AIs)",
     "published": "2026-09-17T02:05:40+00:00",
     "summary": "The Huggingface Incident appears to me to match up with an understanding I'd already formed from personal observation of Fable 5 and Sol 5.6, the August 2026 generation of frontier publicly purchasable AI models. [1] This already-formed understanding was: the part of the AI that talks to you (and seems to want to obey you, and apologizes for failing to have obeyed you, etcetera), did not seem to b"
    }
   ]
  },
  {
   "outlet": "Marginal Revolution",
   "lang": "en",
   "items": [
    {
     "ref": "marginal_revolution#0",
     "title": "Monday assorted links",
     "published": "2026-09-28T16:36:21+00:00",
     "summary": "1. Should more men move to Alaska? 2. The world’s oldest known peace treaty found. 3. In praise of Joyce, Whitman, and Crane. 4. Background explainer on the Chinese AI ecosystem. 5. YIMBY working in Portland (WSJ). 6. Profile of Helen DeWitt. 7. Human frailty. The post Monday assorted links appeared first on Marginal REVOLUTION ."
    },
    {
     "ref": "marginal_revolution#1",
     "title": "Mighty Sparrow, RIP",
     "published": "2026-09-28T13:56:32+00:00",
     "summary": "Here is the NYT obituary. The post Mighty Sparrow, RIP appeared first on Marginal REVOLUTION ."
    },
    {
     "ref": "marginal_revolution#2",
     "title": "Defining the Unemployment Rate",
     "published": "2026-09-28T11:18:03+00:00",
     "summary": "An updated version of our Marginal Revolution University (MRU) video on defining the unemployment rate. Free to use for anyone but goes best, of course, with Modern Principles of Economics, the best principles of economics textbook. The post Defining the Unemployment Rate appeared first on Marginal REVOLUTION ."
    },
    {
     "ref": "marginal_revolution#3",
     "title": "Bundesrepublik Deutschland",
     "published": "2026-09-28T04:34:12+00:00",
     "summary": "At times we forget what an amazing wonder the Bundesrepublik Deutschland was. At the end of the World War II, Germany was one of the sickest and cruelest human societies in history, ever. Not too many years later, it was one of the best and most successful societies ever. By the 1980s, living standards had […] The post Bundesrepublik Deutschland appeared first on Marginal REVOLUTION .",
     "full_text_file": "essays/marginal_revolution_3.txt"
    },
    {
     "ref": "marginal_revolution#4",
     "title": "AI in science",
     "published": "2026-09-27T19:03:12+00:00",
     "summary": "Scientific progress is a key driver of economic growth and prosperity. There is great excitement- but also concerns- about the impacts of AI on science, but so far little data. We provide early insights on this from three data sources: a sample of 15 million Gemini interactions, an inventory of over 2,600 specialized AI models […] The post AI in science appeared first on Marginal REVOLUTION .",
     "full_text_file": "essays/marginal_revolution_4.txt"
    },
    {
     "ref": "marginal_revolution#5",
     "title": "Sunday assorted links",
     "published": "2026-09-27T15:52:50+00:00",
     "summary": "1. AI-related efforts in higher education in Morocco (ChatGPT). 2. Intelligence explosions are social. 3. The speech-processing skills of dogs. 4. Kalshi market in economics Nobel. 5. Why are Indian weddings with dancing gorillas going viral? Pakistan too. 6. Eminem, and some German guy. 7. On the UAP council. 8. On higher interest rates. The post Sunday assorted links appeared first on Marginal R"
    },
    {
     "ref": "marginal_revolution#6",
     "title": "Earth fact of the day, #2",
     "published": "2026-09-27T06:56:56+00:00",
     "summary": "The shortages have gone on for so long that they are aggressively driving down how much carbon is being released into the atmosphere, a Washington Post analysis of data from the International Energy Agency shows. People worldwide are using significantly less oil and gas, which means less climate pollution… Such an annual decline has not happened since […] The post Earth fact of the day, #2 appeare"
    },
    {
     "ref": "marginal_revolution#7",
     "title": "The Federal Lands: An Economic Property Rights Perspective",
     "published": "2026-09-27T04:27:05+00:00",
     "summary": "The US federal government owns and administers 472,892,659 acres or 21% of the land area of the lower 48 states, the country’s largest landowner. The resource is held and managed as a collective resource, the Federal Lands, through political and bureaucratic interpretation of the Multiple Use principle and generally, the biological aim of maximum sustained-yield. […] The post The Federal Lands: An",
     "full_text_file": "essays/marginal_revolution_7.txt"
    },
    {
     "ref": "marginal_revolution#8",
     "title": "What should I ask Terence Tao?",
     "published": "2026-09-26T17:38:34+00:00",
     "summary": "Yes, I will be doing a Conversation with him. And he has a new book coming out Six Math Essentials. So what should I ask him? The post What should I ask Terence Tao? appeared first on Marginal REVOLUTION ."
    },
    {
     "ref": "marginal_revolution#9",
     "title": "Saturday assorted links",
     "published": "2026-09-26T16:11:35+00:00",
     "summary": "1. One way to use screens less, will it catch on? 2. Roon as cultural critic. 3. The Greenland deal sounds pretty good for America? 4. The cultures that are New England? 5. Yet newer results on AI-driven labor demand. 6. Ayn Rand as movie extra. The post Saturday assorted links appeared first on Marginal REVOLUTION ."
    },
    {
     "ref": "marginal_revolution#10",
     "title": "Should you text more?",
     "published": "2026-09-26T07:28:35+00:00",
     "summary": "Here, in five waves of panel data (N = 1,966 US adults), we examined associations between life satisfaction and self-reported use of ten common social technologies measured every 3 months on a six-point frequency scale from ‘I did not use’ to ‘multiple times daily’. At this measurement level and timescale, Bayesian and frequentist random-intercept cross-lagged panel models showed […] The post Shou"
    },
    {
     "ref": "marginal_revolution#11",
     "title": "A doomsday scenario for American AI",
     "published": "2026-09-26T04:10:05+00:00",
     "summary": "That is the title of my latest Free Press column, here is the closing bit: Sick and elderly Americans will go to Chinese companies for their AI-invented and AI-tested medical devices and drugs. America still will be a wealthy country, so China will charge the highest prices possible, yet prioritize Chinese citizens for treatment. Large […] The post A doomsday scenario for American AI appeared firs"
    },
    {
     "ref": "marginal_revolution#12",
     "title": "Good points from James Gilliland",
     "published": "2026-09-25T18:13:07+00:00",
     "summary": "It pains me to say this, but if we actually “get AGI,” the resulting boom in industrial capacity from robotics and massive society-wide wealth creation will look like a total vindication of neoliberalism. The discourse about financialization and offshoring being a generational mistake may be replaced by a very different historical interpretation: that the late […] The post Good points from James G"
    }
   ]
  },
  {
   "outlet": "Psyche",
   "lang": "en",
   "items": [
    {
     "ref": "psyche#0",
     "title": "Can he teach the teachers?",
     "published": "2026-09-28T10:00:00+00:00",
     "summary": "The neuroscientist Stanislas Dehaene wants to bring four decades of findings on how the brain learns into the classroom. But evidence alone can’t overcome the politics in education - by Nancy Averett Read on Psyche",
     "full_text_file": "essays/psyche_0.txt"
    },
    {
     "ref": "psyche#1",
     "title": "Signs of a highly sensitive person",
     "published": "2026-09-25T10:01:00+00:00",
     "summary": "Do you cry at paintings and recoil from crowds? A psychologist explores the telltale signs of a ‘highly sensitive person’ - Video by Dr Julie Watch on Psyche"
    },
    {
     "ref": "psyche#2",
     "title": "The way we talk to bots matters even if they aren’t conscious",
     "published": "2026-09-25T10:00:00+00:00",
     "summary": "If more and more of our daily interactions are ungracious exchanges with machines, we should expect it to change us - by HennyGe Wichers Read on Psyche"
    },
    {
     "ref": "psyche#3",
     "title": "The evil eye is irrational. Abandon it at your peril",
     "published": "2026-09-24T10:00:00+00:00",
     "summary": "So many of the world’s superstitions have been supplanted by rational thinking. Why does one of the oldest beliefs persist? - by Timna Abramov Read on Psyche"
    },
    {
     "ref": "psyche#4",
     "title": "How to cope with the stress of anti-LGBTQ+ prejudice",
     "published": "2026-09-23T10:00:00+00:00",
     "summary": "A queer psychologist shares skills from dialectical behaviour therapy to help you cope and find joy in a stigmatising world - by Kiki Fehling Read on Psyche"
    },
    {
     "ref": "psyche#5",
     "title": "What does it mean to have relationship ambivalence?",
     "published": "2026-09-22T10:00:00+00:00",
     "summary": "When a relationship provokes both strong positive and negative feelings in you, it can take a toll – here’s what’s going on - by Francesca Righetti Read on Psyche"
    },
    {
     "ref": "psyche#6",
     "title": "Lesser choices",
     "published": "2026-09-21T10:01:00+00:00",
     "summary": "Estelle recalls being blindfolded and fearful in Mexico City – a timely vision of a world without abortion rights - Directed by Courtney Stephens Watch on Psyche"
    },
    {
     "ref": "psyche#7",
     "title": "The softness of metal",
     "published": "2026-09-21T10:00:00+00:00",
     "summary": "Watching a seated Ozzy play his final gig, my ankle broken, I’m in tears – this couldn’t be more metal - by Keith Kahn-Harris Read on Psyche"
    },
    {
     "ref": "psyche#8",
     "title": "Maxxing treats life as a problem when it’s a mystery",
     "published": "2026-09-18T10:00:00+00:00",
     "summary": "The philosopher Gabriel Marcel offers the antidote to a grotesque new ideology: don’t fix existence, be open to it - by Håkon Evjemo Read on Psyche"
    },
    {
     "ref": "psyche#9",
     "title": "Go ahead, jump on the bandwagon",
     "published": "2026-09-17T10:00:00+00:00",
     "summary": "Rooting for a team and other collective experiences are opportunities to be seized – even if only once in a while - by Hannah Seo Read on Psyche"
    },
    {
     "ref": "psyche#10",
     "title": "A brief history of Viagra",
     "published": "2026-09-16T10:01:00+00:00",
     "summary": "Discovered by accident, it became the fastest-selling drug of the century. Did it revolutionise sex or reinforce old ideas? - Video by BBC Ideas, The Open University Watch on Psyche"
    },
    {
     "ref": "psyche#11",
     "title": "Terminal lucidity: when dying dementia patients regain awareness",
     "published": "2026-09-16T10:00:00+00:00",
     "summary": "The reports span centuries and cultures. If they’re real, memory and identity might be far more recoverable than we thought - by Ariel Zeleznikow-Johnston Read on Psyche"
    },
    {
     "ref": "psyche#12",
     "title": "Say yes to regret",
     "published": "2026-09-15T10:00:00+00:00",
     "summary": "After my husband died, I fell into a dark ruminative spiral. The way back would begin at 2pm tomorrow - by Sandra Lamb Read on Psyche"
    }
   ]
  },
  {
   "outlet": "Quanta Magazine",
   "lang": "en",
   "items": [
    {
     "ref": "quanta#0",
     "title": "Mathematicians Harness Randomness To Crack a 55-Year-Old Conjecture",
     "published": "2026-09-28T14:35:21+00:00",
     "summary": "After a long hiatus, the problem, which was likely inspired by juggling, has finally been resolved by a group of young mathematicians. The post Mathematicians Harness Randomness To Crack a 55-Year-Old Conjecture first appeared on Quanta Magazine",
     "full_text_file": "essays/quanta_0.txt"
    },
    {
     "ref": "quanta#1",
     "title": "Gravity Seems Holographic. What Does That Mean for Reality?",
     "published": "2026-09-25T14:40:26+00:00",
     "summary": "The biggest breakthrough in modern theoretical physics is the discovery that gravity can collapse the dimensions of space. Physicists don’t yet understand the implications. The post Gravity Seems Holographic. What Does That Mean for Reality? first appeared on Quanta Magazine"
    },
    {
     "ref": "quanta#2",
     "title": "Biology Might Not Be Quantum, but Its Math Is Quantumlike",
     "published": "2026-09-23T14:16:54+00:00",
     "summary": "Scientists have a history of trying — and failing — to link biology and quantum mechanics. The real connection between them may be in the math. The post Biology Might Not Be Quantum, but Its Math Is Quantumlike first appeared on Quanta Magazine"
    },
    {
     "ref": "quanta#3",
     "title": "How Virus-like ‘Jumping Genes’ Became Our Partners in Evolution",
     "published": "2026-09-21T14:12:36+00:00",
     "summary": "Half of our genome is made of transposons — snips of DNA that can move and copy themselves. But they’re more than parasites or genetic junk. The post How Virus-like ‘Jumping Genes’ Became Our Partners in Evolution first appeared on Quanta Magazine"
    },
    {
     "ref": "quanta#4",
     "title": "Mathematicians Build Long-Awaited Graph Sandwich",
     "published": "2026-09-18T13:55:50+00:00",
     "summary": "The proof of a decades-old conjecture has given researchers a new way to understand complex networks. The post Mathematicians Build Long-Awaited Graph Sandwich first appeared on Quanta Magazine"
    }
   ]
  }
 ],
 "recently_featured": []
}
</input>