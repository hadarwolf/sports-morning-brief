Write the Sports section: 3-5 stories.

- Draw on European soccer (big-5 leagues, Champions League), Inter Miami / MLS, international soccer and the NBA.
- Arsenal and Barcelona always get a story if they played yesterday, play today or tomorrow, or have real news. Even on a quiet day, one story can cover where they stand: table, form and next fixture.
- Other clubs and leagues earn a slot only when their storyline is genuinely big.
- Include an NBA story only if there is meaningful NBA news. It may be the offseason.
- Results, fixtures and tables come from the structured data. Storylines come from the news feeds. Cite "football_data", "balldontlie" or "thesportsdb" as a source_ref when you use their data.
- No favorite team plays today.
- Fill israeli_players with one entry per player listed in nba_data.israeli_players, giving their latest game or news. If the input has nothing new on a player, say so plainly. Never invent stats. Box scores are often unavailable.
- Use kind "news" for everything in this section.

This section opens in English by default, so make the English version your best writing.

Output: write `drafts/sports.json` matching `schemas/sports.schema.json`.

<input>
{
 "european_soccer_data": {
  "matches": {
   "yesterday": [],
   "today": [],
   "tomorrow": []
  },
  "standings_top6_plus_favorites": {
   "Premier League": [
    {
     "pos": 1,
     "team": "Man City",
     "played": 5,
     "pts": 15,
     "gd": 8
    },
    {
     "pos": 2,
     "team": "Arsenal",
     "played": 5,
     "pts": 12,
     "gd": 4
    },
    {
     "pos": 3,
     "team": "Brighton Hove",
     "played": 5,
     "pts": 10,
     "gd": 11
    },
    {
     "pos": 4,
     "team": "Brentford",
     "played": 5,
     "pts": 9,
     "gd": 6
    },
    {
     "pos": 5,
     "team": "Leeds United",
     "played": 5,
     "pts": 9,
     "gd": 4
    },
    {
     "pos": 6,
     "team": "Liverpool",
     "played": 5,
     "pts": 9,
     "gd": 3
    }
   ],
   "Primera Division": [
    {
     "pos": 1,
     "team": "Barça",
     "played": 7,
     "pts": 21,
     "gd": 24
    },
    {
     "pos": 2,
     "team": "Atleti",
     "played": 7,
     "pts": 16,
     "gd": 9
    },
    {
     "pos": 3,
     "team": "Real Betis",
     "played": 7,
     "pts": 16,
     "gd": 2
    },
    {
     "pos": 4,
     "team": "Real Madrid",
     "played": 7,
     "pts": 15,
     "gd": 10
    },
    {
     "pos": 5,
     "team": "Sevilla FC",
     "played": 7,
     "pts": 13,
     "gd": 1
    },
    {
     "pos": 6,
     "team": "Alavés",
     "played": 7,
     "pts": 11,
     "gd": 5
    }
   ],
   "Bundesliga": [
    {
     "pos": 1,
     "team": "Dortmund",
     "played": 4,
     "pts": 12,
     "gd": 7
    },
    {
     "pos": 2,
     "team": "Bayern",
     "played": 4,
     "pts": 10,
     "gd": 12
    },
    {
     "pos": 3,
     "team": "Freiburg",
     "played": 4,
     "pts": 10,
     "gd": 9
    },
    {
     "pos": 4,
     "team": "Augsburg",
     "played": 4,
     "pts": 7,
     "gd": 5
    },
    {
     "pos": 5,
     "team": "Leverkusen",
     "played": 4,
     "pts": 7,
     "gd": 5
    },
    {
     "pos": 6,
     "team": "Mainz",
     "played": 4,
     "pts": 7,
     "gd": 4
    }
   ],
   "Serie A": [
    {
     "pos": 1,
     "team": "Roma",
     "played": 5,
     "pts": 13,
     "gd": 11
    },
    {
     "pos": 2,
     "team": "Inter",
     "played": 5,
     "pts": 13,
     "gd": 7
    },
    {
     "pos": 3,
     "team": "Lazio",
     "played": 5,
     "pts": 13,
     "gd": 5
    },
    {
     "pos": 4,
     "team": "Cagliari",
     "played": 5,
     "pts": 12,
     "gd": 3
    },
    {
     "pos": 5,
     "team": "Milan",
     "played": 5,
     "pts": 11,
     "gd": 6
    },
    {
     "pos": 6,
     "team": "Frosinone",
     "played": 5,
     "pts": 10,
     "gd": 5
    }
   ],
   "Ligue 1": [
    {
     "pos": 1,
     "team": "Monaco",
     "played": 5,
     "pts": 13,
     "gd": 5
    },
    {
     "pos": 2,
     "team": "Olympique Lyon",
     "played": 5,
     "pts": 11,
     "gd": 8
    },
    {
     "pos": 3,
     "team": "Paris FC",
     "played": 5,
     "pts": 11,
     "gd": 5
    },
    {
     "pos": 4,
     "team": "Lille",
     "played": 5,
     "pts": 10,
     "gd": 4
    },
    {
     "pos": 5,
     "team": "Stade Rennais",
     "played": 5,
     "pts": 10,
     "gd": -1
    },
    {
     "pos": 6,
     "team": "PSG",
     "played": 5,
     "pts": 8,
     "gd": 1
    }
   ]
  },
  "favorite_teams": {
   "arsenal": {
    "recent": [
     {
      "competition": "Premier League",
      "kickoff_utc": "2026-09-19T14:00:00Z",
      "home": "Brighton Hove",
      "away": "Arsenal",
      "status": "FINISHED",
      "score": "3-0"
     }
    ],
    "upcoming": [
     {
      "competition": "Premier League",
      "kickoff_utc": "2026-10-10T11:30:00Z",
      "home": "Arsenal",
      "away": "Leeds United",
      "status": "TIMED",
      "score": null
     }
    ]
   },
   "barcelona": {
    "recent": [
     {
      "competition": "Primera Division",
      "kickoff_utc": "2026-09-16T19:30:00Z",
      "home": "Barça",
      "away": "Santander",
      "status": "FINISHED",
      "score": "7-2"
     },
     {
      "competition": "Primera Division",
      "kickoff_utc": "2026-09-19T19:00:00Z",
      "home": "Sevilla FC",
      "away": "Barça",
      "status": "FINISHED",
      "score": "1-3"
     }
    ],
    "upcoming": [
     {
      "competition": "Primera Division",
      "kickoff_utc": "2026-10-10T16:30:00Z",
      "home": "Barça",
      "away": "Getafe",
      "status": "TIMED",
      "score": null
     }
    ]
   }
  }
 },
 "nba_data": {
  "games_last_night": [],
  "games_today": [],
  "israeli_players": {
   "Deni Avdija": {
    "team": "Portland Trail Blazers",
    "position": "F"
   },
   "Ben Saraf": {
    "team": "Brooklyn Nets",
    "position": "G"
   }
  },
  "israeli_player_box_scores": null
 },
 "inter_miami_and_israel_national_team": {
  "inter_miami": {
   "recent": [
    {
     "competition": "American Major League Soccer",
     "kickoff_utc": "2026-09-20T23:00:00",
     "home": "Inter Miami",
     "away": "San Diego FC",
     "score": "2-2"
    }
   ],
   "upcoming": [
    {
     "competition": "American Major League Soccer",
     "kickoff_utc": "2026-10-10T23:30:00",
     "home": "Inter Miami",
     "away": "DC United",
     "score": null
    }
   ]
  },
  "israel_national_team": {
   "recent": [
    {
     "competition": "UEFA Nations League",
     "kickoff_utc": "2026-09-27T18:45:00",
     "home": "Israel",
     "away": "Ireland",
     "score": "0-3"
    }
   ],
   "upcoming": [
    {
     "competition": "UEFA Nations League",
     "kickoff_utc": "2026-10-01T18:45:00",
     "home": "Israel",
     "away": "Kosovo",
     "score": null
    }
   ]
  }
 },
 "news_feeds": [
  {
   "outlet": "BBC Sport — Football",
   "lang": "en",
   "items": [
    {
     "ref": "bbc_football#0",
     "title": "Ferguson retains Rangers dream but Bologna exit never close",
     "published": "2026-09-28T15:27:38+00:00",
     "summary": "Lewis Ferguson reveals \"nothing was ever that close\" on a move away from Bologna this summer amid reports of interest from Rangers but he does harbour ambitions of a return to his boyhood club."
    },
    {
     "ref": "bbc_football#1",
     "title": "Ferguson retains Rangers dream but Bologna exit was not 'close'",
     "published": "2026-09-28T15:27:38+00:00",
     "summary": "Lewis Ferguson reveals \"nothing was ever that close\" on a move away from Bologna this summer amid reports of interest from Rangers but he does harbour ambitions of a return to his boyhood club."
    },
    {
     "ref": "bbc_football#2",
     "title": "How does Cas work and why can't Man City appeal to it?",
     "published": "2026-09-28T14:43:05+00:00",
     "summary": "The Court of Arbitration for Sport (CAS) regulates legal disputes across the world of sport"
    },
    {
     "ref": "bbc_football#3",
     "title": "Forest Green allow Savage to talk to another club",
     "published": "2026-09-28T13:37:08+00:00",
     "summary": "Forest Green give manager Robbie Savage permission to speak to another club, amid speculation linking him to Peterborough United."
    },
    {
     "ref": "bbc_football#4",
     "title": "Could Potter be England's next breakthrough star?",
     "published": "2026-09-28T13:33:23+00:00",
     "summary": "With Sarina Wiegman set to name her latest England squad on Tuesday, there is one name everyone is talking about - Lexi Potter. Here is why."
    },
    {
     "ref": "bbc_football#5",
     "title": "Could Potter be England's next breakthrough star?",
     "published": "2026-09-28T13:33:23+00:00",
     "summary": "With Sarina Wiegman set to name her latest England squad on Tuesday, there is one name everyone is talking about - Lexi Potter. Here is why."
    },
    {
     "ref": "bbc_football#6",
     "title": "Konsa and O'Reilly doubts to face Czech Republic",
     "published": "2026-09-28T13:20:44+00:00",
     "summary": "Ezri Konsa and Nico O'Reilly are both doubts to play in England's Nations League match against the Czech Republic on Tuesday night."
    },
    {
     "ref": "bbc_football#7",
     "title": "'I've lost my peace' - Cape Verde hero Vozinha on newfound fame",
     "published": "2026-09-28T12:59:30+00:00",
     "summary": "Cape Verde's World Cup hero Vozinha says he craves the \"peace and tranquillity\" of the life he led before he shot to fame."
    },
    {
     "ref": "bbc_football#8",
     "title": "FAI investigates alleged racist abuse of Idah",
     "published": "2026-09-28T12:17:49+00:00",
     "summary": "The FAI is amassing high-quality footage of the alleged incident with the aim of presenting evidence to Uefa."
    },
    {
     "ref": "bbc_football#9",
     "title": "Bellamy sure Wales belong as Haaland threat looms",
     "published": "2026-09-28T12:08:16+00:00",
     "summary": "Craig Bellamy expects Norway to be a force for years, but insists Wales have earned the right to be in Nations League A."
    },
    {
     "ref": "bbc_football#10",
     "title": "Preston appoint Bradford boss Alexander",
     "published": "2026-09-28T10:31:06+00:00",
     "summary": "Preston North End appoint Bradford City boss Graham Alexander as their new manager."
    },
    {
     "ref": "bbc_football#11",
     "title": "Preston appoint former Scotland player Alexander",
     "published": "2026-09-28T10:31:06+00:00",
     "summary": "Preston North End appoint Bradford City boss Graham Alexander as their new manager."
    },
    {
     "ref": "bbc_football#12",
     "title": "Two players sent off for pulling rival's dreadlocks",
     "published": "2026-09-28T10:21:43+00:00",
     "summary": "Antigua and Barbuda players are red-carded for pulling Anguilla player Aedan Scipio's dreadlocks in a Concacaf Nations League game."
    },
    {
     "ref": "bbc_football#13",
     "title": "Man City rule breaches not my concern - Mancini",
     "published": "2026-09-28T09:42:03+00:00",
     "summary": "Roberto Mancini says an alleged \"double contract\" during his time as Manchester City manager is \"not my concern\"."
    },
    {
     "ref": "bbc_football#14",
     "title": "FAI unclear over possible sanctions if game not played",
     "published": "2026-09-28T09:37:09+00:00",
     "summary": "Republic of Ireland could have faced \"undetermined\" sanctions had they not played their Nations League match against Israel on Sunday, according to FAI president Paul Cooke."
    },
    {
     "ref": "bbc_football#15",
     "title": "The four 'what next?' scenarios for Premier League after Man City ruling",
     "published": "2026-09-28T08:28:30+00:00",
     "summary": "It has taken more than two years, but a judgement finally appears to have been made on the 115 charges levelled against Manchester City. Here's what it means."
    },
    {
     "ref": "bbc_football#16",
     "title": "Award-winner to fourth choice - what has gone wrong for Ramsdale?",
     "published": "2026-09-28T08:10:08+00:00",
     "summary": "From challenging for the Premier League with Arsenal and playing for England, Aaron Ramsdale is now Southampton's fourth-choice goalkeeper."
    },
    {
     "ref": "bbc_football#17",
     "title": "All the goals from the Women's Super League - matchweek four",
     "published": "2026-09-28T07:58:53+00:00",
     "summary": "Watch every goal from matchweek four of the Women's Super League 2026-27 season."
    },
    {
     "ref": "bbc_football#18",
     "title": "A 31-year wait for success - but can Everton fans still celebrate?",
     "published": "2026-09-28T07:56:56+00:00",
     "summary": "Is supporting Everton a life of misery, or are there still reasons to celebrate? Chief football writer Phil McNulty seeks the answer."
    },
    {
     "ref": "bbc_football#19",
     "title": "You are the Scotland boss - what would you change for Switzerland?",
     "published": "2026-09-28T07:46:12+00:00",
     "summary": "Put yourself in the shoes of the new Scotland head coach Sebastien Pocognoli as he picks his first home XI to face Switzerland."
    },
    {
     "ref": "bbc_football#20",
     "title": "NI players relish Windsor return against Hungary",
     "published": "2026-09-28T07:09:26+00:00",
     "summary": "Northern Ireland's hosting of Hungary in the Uefa Nations League will be their first game in Belfast for 315 days."
    },
    {
     "ref": "bbc_football#21",
     "title": "Is Premier League possession football on the way out?",
     "published": "2026-09-28T06:10:34+00:00",
     "summary": "Only 36% of teams with more than 60% possession have won this season in the Premier League. BBC Sport looks at why?"
    },
    {
     "ref": "bbc_football#22",
     "title": "Flex your football brain with our daily quizzes",
     "published": "2026-09-28T06:06:48+00:00",
     "summary": "Test your ball knowledge with today's Who Am I?, Five in Five and Brainteaser."
    },
    {
     "ref": "bbc_football#23",
     "title": "Republic of Ireland 'raised awareness worldwide' in Israel game",
     "published": "2026-09-27T22:20:17+00:00",
     "summary": "Republic of Ireland head coach Heimir Hallgrimsson says his players \"raised awareness worldwide\" after they chose not to engage in pre-match formalities with Israel."
    },
    {
     "ref": "bbc_football#24",
     "title": "Seventeen titles in five years - why Spain are a dominant force",
     "published": "2026-09-27T22:13:19+00:00",
     "summary": "We look at what's behind Spain's dominance of football with 17 titles in five years across all age groups and in the men's and women's game."
    }
   ]
  },
  {
   "outlet": "ESPN NBA",
   "lang": "en",
   "items": [
    {
     "ref": "espn_nba#0",
     "title": "Sources: Duren not at Pistons' media day, camp amid contract standoff",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "Pistons All-Star center Jalen Duren is not attending the team's media day on Monday or the start of training camp as the contract standoff continues, sources told ESPN's Shams Charania on Monday."
    },
    {
     "ref": "espn_nba#1",
     "title": "Giannis brings heat as Miami era starts: Can still 'dominate the game'",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "Giannis Antetokounmpo has no doubt about his potential as he enters the next stage of his career following a blockbuster trade to the Heat, saying he can still \"dominate the game\" as one of the best players in the world."
    },
    {
     "ref": "espn_nba#2",
     "title": "Porzingis to miss start of Warriors camp with 'health issue'",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "Kristaps Porzingis will miss the start of Warriors training camp because of a health issue."
    },
    {
     "ref": "espn_nba#3",
     "title": "Brunson gets assist from Knicks teammates, shares laughs on 'SNL'",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "Jalen Brunson had four of his Knicks teammates -- Karl-Anthony Towns, Mikal Bridges, OG Anunoby and Josh Hart -- in the audience for his monologue Saturday night, in his role as host of \"SNL.\""
    },
    {
     "ref": "espn_nba#4",
     "title": "Bulls trade Dillingham to Hornets for Hield, cash",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "The Bulls have traded Rob Dillingham to the Hornets for Buddy Hield and cash."
    },
    {
     "ref": "espn_nba#5",
     "title": "Hornets star Knueppel sidelined with hamstring injury",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "The Charlotte Hornets will be without Kon Knueppel for at least the entire preseason due to a left hamstring injury, the team announced Friday."
    },
    {
     "ref": "espn_nba#6",
     "title": "Altman on LeBron's 76ers move: Cavs have 'too much of a good thing' to worry",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "Cavs president of basketball operations Koby Altman said he wasn't fazed when LeBron James chose to sign with the Sixers, saying, \"We're built for a sustainable run here regardless of one outcome.\""
    },
    {
     "ref": "espn_nba#7",
     "title": "LeBron: Maxey friendship, desire to help Embiid drove 76ers decision",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "LeBron James says his long-standing friendship with All-Star Tyrese Maxey and a desire to help Joel Embiid win his first NBA title played significant roles in his decision to sign with the 76ers."
    },
    {
     "ref": "espn_nba#8",
     "title": "💰 Flagg's 1-of-1 rookie debut patch card sells for record $8.04M",
     "published": "2026-09-28T17:02:04+00:00",
     "summary": "The card was sold in early Friday morning at 2 a.m. ET."
    },
    {
     "ref": "espn_nba#9",
     "title": "From 'emo Jimmy' to ombre faux locs: Jimmy Butler's media day looks through the years",
     "published": "2026-09-28T15:08:40+00:00",
     "summary": "Jimmy Butler has made headlines at past media days for his unique looks. Will Butler arrive looking different this year?"
    },
    {
     "ref": "espn_nba#10",
     "title": "Wizards' No. 1 pick AJ Dybantsa named cover athlete of 2026 Topps Flagship Basketball",
     "published": "2026-09-28T15:08:39+00:00",
     "summary": "The Washington Wizards star began collecting cards this year and will be the cover athlete of 2026 Topps Flagship Basketball."
    },
    {
     "ref": "espn_nba#11",
     "title": "10-team roto/category league mock draft: Who went No. 1?",
     "published": "2026-09-28T12:23:23+00:00",
     "summary": "Our 10-team, roto/category fantasy basketball mock draft featured Nikola Jokic and Victor Wembanyama as the first players selected."
    },
    {
     "ref": "espn_nba#12",
     "title": "Sleepers, breakouts and busts for 2026-27",
     "published": "2026-09-28T12:23:23+00:00",
     "summary": "Which fantasy basketball players are going to exceed expectations in 2026-27? Who will disappoint? Who is ready to take things to an elite level? Our experts list their picks."
    },
    {
     "ref": "espn_nba#13",
     "title": "The NBA's 8 most intriguing newcomers, ranked",
     "published": "2026-09-28T12:19:51+00:00",
     "summary": "A full roster's worth of stars changed teams this past summer. The storylines surrounding eight will help define the league's journey to spring."
    },
    {
     "ref": "espn_nba#14",
     "title": "2026-27 NBA regular-season buzz: Latest on trades, news and intel",
     "published": "2026-09-28T12:19:51+00:00",
     "summary": "Here are the deals, trades and buzz across the NBA, including intel from Monday's media days."
    },
    {
     "ref": "espn_nba#15",
     "title": "Grades for every NBA offseason signing: Why Warriors get a B for extending Steph Curry",
     "published": "2026-09-26T17:21:55+00:00",
     "summary": "We're grading the biggest free agent signings and extensions, including Steph's new two-year deal."
    },
    {
     "ref": "espn_nba#16",
     "title": "Grading the Dorian Finney-Smith trade (and more): Which team gets a B-?",
     "published": "2026-09-26T17:21:55+00:00",
     "summary": "We're grading the biggest NBA trades of the offseason, including the Atlanta deal that sent Hield and Nembhard to Charlotte for Finney-Smith."
    }
   ]
  },
  {
   "outlet": "ESPN FC",
   "lang": "en",
   "items": [
    {
     "ref": "espn_soccer#0",
     "title": "Georgia peach and red: NWSL expansion club Atlanta City unveils new colors",
     "published": "2026-09-28T15:44:54+00:00",
     "summary": "Atlanta City FC will be the name of Atlanta's forthcoming NWSL expansion team that will begin play in 2028."
    },
    {
     "ref": "espn_soccer#1",
     "title": "Struggling LAFC fires 1st-year coach Dos Santos",
     "published": "2026-09-28T15:44:54+00:00",
     "summary": "LAFC fired head coach Marc Dos Santos on Sunday night, late in his disappointing first season in charge."
    },
    {
     "ref": "espn_soccer#2",
     "title": "Vozinha on WC fame: 'I'd choose life I had before'",
     "published": "2026-09-28T15:44:54+00:00",
     "summary": "Viral World Cup goalkeeper Vozinha has revealed he is struggling with his newfound fame, saying that he would like to go back to a time before he was so well-known."
    },
    {
     "ref": "espn_soccer#3",
     "title": "Dorgu returns to United after hamstring injury",
     "published": "2026-09-28T15:44:53+00:00",
     "summary": "Patrick Dorgu has returned to Manchester United for assessment after suffering an injury on international duty with Denmark."
    },
    {
     "ref": "espn_soccer#4",
     "title": "Ireland skip handshakes, bow heads before win over Israel",
     "published": "2026-09-28T15:44:53+00:00",
     "summary": "The Republic of Ireland wore black armbands and skipped the typical prematch handshakes before securing a 3-0 victory over Israel in their contentious UEFA Nations League match Sunday."
    },
    {
     "ref": "espn_soccer#5",
     "title": "Yamal reveals what he said to Messi at World Cup",
     "published": "2026-09-28T15:44:53+00:00",
     "summary": "Spain and Barcelona forward Lamine Yamal has said that he thanked Lionel Messi for everything he gave to football when the two embraced at the end of the 2026 World Cup final."
    },
    {
     "ref": "espn_soccer#6",
     "title": "Columbus stuns Miami late after Messi's free-kick golazo",
     "published": "2026-09-28T15:44:53+00:00",
     "summary": "Jamal Thiaré scored in the eighth minute of second-half stoppage time to give the Columbus Crew a stunning 2-1 win over MLS Cup holders Inter Miami on Sunday."
    },
    {
     "ref": "espn_soccer#7",
     "title": "Klopp: Germany's 1st ever loss to Greece 'part of the process'",
     "published": "2026-09-28T15:44:53+00:00",
     "summary": "Jürgen Klopp said his first defeat as Germany boss was \"part of the process\" as he looks to rejuvenate the four-time World Cup winners."
    },
    {
     "ref": "espn_soccer#8",
     "title": "🏆 How would a 64-team World Cup work?",
     "published": "2026-09-28T15:44:53+00:00",
     "summary": "The 2026 World Cup was the first to feature 48 teams, and 2030 could see the field swell to 64, but just how feasible is a tournament that size?"
    },
    {
     "ref": "espn_soccer#9",
     "title": "MLS Power Rankings: No Cavan? No problem for surging Philadelphia",
     "published": "2026-09-28T15:27:42+00:00",
     "summary": "Philadelphia lost three star youngsters to international duty, yet the Union continued their march toward the top of our rankings."
    },
    {
     "ref": "espn_soccer#10",
     "title": "NWSL Power Rankings: Angel City move up ahead of meeting with No. 1 Gotham",
     "published": "2026-09-28T15:27:42+00:00",
     "summary": "Angel City's win over Washington has them surging up our rankings, but can any team catch Gotham?"
    },
    {
     "ref": "espn_soccer#11",
     "title": "Will anyone stop Infantino? FIFA president's confident U20 World Cup cameo says otherwise",
     "published": "2026-09-28T15:10:15+00:00",
     "summary": "Under fire from UEFA, Gianni Infantino is back to business as usual and inching closer to reelection as FIFA president."
    },
    {
     "ref": "espn_soccer#12",
     "title": "Goals galore! Why Barça's start to season is best in Europe's top leagues for almost 100 years",
     "published": "2026-09-28T14:57:57+00:00",
     "summary": "Barcelona have begun the season on fire, scoring 36 goals in their first eight matches. How does that compare to the best starts for all time? (Spoiler: Very well.)"
    },
    {
     "ref": "espn_soccer#13",
     "title": "Who's the striker leading Raphinha, Mbappé, Haaland in race for European Golden Shoe?",
     "published": "2026-09-28T14:57:57+00:00",
     "summary": "Raphinha may have started the season on fire, but there's a little-known striker who is ahead of the Barça star in the race for the European Golden Shoe."
    },
    {
     "ref": "espn_soccer#14",
     "title": "JJ Gabriel and the 'nightmare' battle for Premier League academy talent",
     "published": "2026-09-28T13:27:39+00:00",
     "summary": "In the fiercely competitive race for the best Premier League academy players, JJ Gabriel won't be the last young talent at the center of a transfer tug-of-war."
    },
    {
     "ref": "espn_soccer#15",
     "title": "Transfer rumors, news: Madrid, Barcelona look to Haaland, Sullivan amid Man City uncertainty",
     "published": "2026-09-28T13:27:38+00:00",
     "summary": "Real Madrid and Barcelona are looking at a host of players due to uncertainty created by the case surrounding Man City's financial rule breaches. Transfer Talk has the latest."
    },
    {
     "ref": "espn_soccer#16",
     "title": "Man City vs. Premier League: 115 financial charges explained",
     "published": "2026-09-28T09:00:56+00:00",
     "summary": "The sporting world is waiting for a resolution to the hearings on Man City's charges for allegedly breaching the Premier League's financial rules. Here's what we know, and what might come next."
    },
    {
     "ref": "espn_soccer#17",
     "title": "Man City verdict will leave a stain and stench on a Premier League era",
     "published": "2026-09-28T09:00:55+00:00",
     "summary": "Manchester City are expected to be found guilty of almost all 115 financial charges against them. It means an era of English soccer is now tarnished with multiple asterisks."
    },
    {
     "ref": "espn_soccer#18",
     "title": "There's a palpable sense of excitement surrounding the USMNT's young guns",
     "published": "2026-09-28T03:26:21+00:00",
     "summary": "The 2030 World Cup may be a long way away but, after Mauricio Pochettino handed out 11 debuts on Saturday, the sense of excitement around the USMNT camp is hard to ignore."
    },
    {
     "ref": "espn_soccer#19",
     "title": "USMNT player ratings: Ellis gets 9, Berhalter 10 in Peru rout",
     "published": "2026-09-28T03:26:21+00:00",
     "summary": "Justin Ellis and Sebastian Berhalter shone as Mauricio Pochettino unveiled a new-look USMNT."
    },
    {
     "ref": "espn_soccer#20",
     "title": "From WSL faves to afterthought: Arsenal's season already looks doomed after Chelsea loss",
     "published": "2026-09-27T20:32:13+00:00",
     "summary": "Arsenal were supposed to be frontunners for the WSL title, but their slow start to the season is raising alarms."
    },
    {
     "ref": "espn_soccer#21",
     "title": "Top 50 USMNT players, ranked by club performance: Which Americans are in hot form?",
     "published": "2026-09-27T16:34:32+00:00",
     "summary": "Who are the best Americans as the new World Cup cycle begins? We rank USMNT players on club form: ESPN's Player Performance Index returns."
    }
   ]
  },
  {
   "outlet": "Google News — Inter Miami",
   "lang": "en",
   "items": [
    {
     "ref": "gnews_inter_miami#0",
     "title": "Lionel Messi’s Inter Miami called out by Columbus Crew coach: ‘What they do is bad for the game’ - bolavip.com",
     "published": "2026-09-28T16:20:20+00:00",
     "summary": "Lionel Messi’s Inter Miami called out by Columbus Crew coach: ‘What they do is bad for the game’ bolavip.com"
    },
    {
     "ref": "gnews_inter_miami#1",
     "title": "\"An exceptional explosion with Inter Miami\": Messi two steps away from a historic throne - goal.com",
     "published": "2026-09-28T15:53:06+00:00",
     "summary": "\"An exceptional explosion with Inter Miami\": Messi two steps away from a historic throne goal.com"
    },
    {
     "ref": "gnews_inter_miami#2",
     "title": "Inter Miami: Lionel Messi on the verge of a legendary record - beninwebtv.bj",
     "published": "2026-09-28T15:51:25+00:00",
     "summary": "Inter Miami: Lionel Messi on the verge of a legendary record beninwebtv.bj"
    },
    {
     "ref": "gnews_inter_miami#3",
     "title": "Lionel Messi free-kick goal vs. Columbus: Video from every angle of ridiculous strike by Inter Miami star - sportingnews.com",
     "published": "2026-09-28T14:51:40+00:00",
     "summary": "Lionel Messi free-kick goal vs. Columbus: Video from every angle of ridiculous strike by Inter Miami star sportingnews.com"
    },
    {
     "ref": "gnews_inter_miami#4",
     "title": "Gonzalez fumes at 'refereeing mistakes' in Miami's defeat to Columbus - FotMob",
     "published": "2026-09-28T14:35:14+00:00",
     "summary": "Gonzalez fumes at 'refereeing mistakes' in Miami's defeat to Columbus FotMob"
    },
    {
     "ref": "gnews_inter_miami#5",
     "title": "Gonzalez fumes at 'refereeing mistakes' in Miami's defeat to Columbus - beIN SPORTS",
     "published": "2026-09-28T14:35:14+00:00",
     "summary": "Gonzalez fumes at 'refereeing mistakes' in Miami's defeat to Columbus beIN SPORTS"
    },
    {
     "ref": "gnews_inter_miami#6",
     "title": "Jamal Thiaré scores in 9th minute of stoppage time, Crew beats Inter Miami and Leo Messi 2-1 - Spectrum News",
     "published": "2026-09-28T13:51:00+00:00",
     "summary": "Jamal Thiaré scores in 9th minute of stoppage time, Crew beats Inter Miami and Leo Messi 2-1 Spectrum News"
    },
    {
     "ref": "gnews_inter_miami#7",
     "title": "Columbus Crew fans gather for Messi, Inter Miami match - Spectrum News",
     "published": "2026-09-28T13:37:00+00:00",
     "summary": "Columbus Crew fans gather for Messi, Inter Miami match Spectrum News"
    },
    {
     "ref": "gnews_inter_miami#8",
     "title": "Crew stuns Inter Miami with win in stoppage time - Miami Herald",
     "published": "2026-09-28T12:25:01+00:00",
     "summary": "Crew stuns Inter Miami with win in stoppage time Miami Herald"
    },
    {
     "ref": "gnews_inter_miami#9",
     "title": "Columbus Crew vs Inter Miami: Major League Soccer stats & head-to-head - bbc.com",
     "published": "2026-09-28T12:06:30+00:00",
     "summary": "Columbus Crew vs Inter Miami: Major League Soccer stats & head-to-head bbc.com"
    },
    {
     "ref": "gnews_inter_miami#10",
     "title": "Most famous athlete to play in Columbus still couldn't beat the Crew - The Columbus Dispatch",
     "published": "2026-09-28T10:56:00+00:00",
     "summary": "Most famous athlete to play in Columbus still couldn't beat the Crew The Columbus Dispatch"
    },
    {
     "ref": "gnews_inter_miami#11",
     "title": "WATCH: Lionel Messi stuns with ‘impossible’ free-kick for Inter Miami - Moneycontrol.com",
     "published": "2026-09-28T09:52:40+00:00",
     "summary": "WATCH: Lionel Messi stuns with ‘impossible’ free-kick for Inter Miami Moneycontrol.com"
    },
    {
     "ref": "gnews_inter_miami#12",
     "title": "Messi scores... Columbus Crew snatch a dramatic late win against Inter Miami in MLS (Video) - صوت الإمارات",
     "published": "2026-09-28T09:12:26+00:00",
     "summary": "Messi scores... Columbus Crew snatch a dramatic late win against Inter Miami in MLS (Video) صوت الإمارات"
    },
    {
     "ref": "gnews_inter_miami#13",
     "title": "Inter Miami player ratings vs Columbus Crew: Lionel Messi magic not enough as Santiago Morales red card proves costly - goal.com",
     "published": "2026-09-28T08:16:45+00:00",
     "summary": "Inter Miami player ratings vs Columbus Crew: Lionel Messi magic not enough as Santiago Morales red card proves costly goal.com"
    },
    {
     "ref": "gnews_inter_miami#14",
     "title": "CLBvsMIA 09-27-2026 Match Feed | MLSsoccer.com - MLSsoccer.com",
     "published": "2026-09-28T08:04:35+00:00",
     "summary": "CLBvsMIA 09-27-2026 Match Feed | MLSsoccer.com MLSsoccer.com"
    },
    {
     "ref": "gnews_inter_miami#15",
     "title": "Columbus Crew 2-1 Inter Miami: Messi free-kick not enough to halt winless run - FotMob",
     "published": "2026-09-28T07:43:06+00:00",
     "summary": "Columbus Crew 2-1 Inter Miami: Messi free-kick not enough to halt winless run FotMob"
    },
    {
     "ref": "gnews_inter_miami#16",
     "title": "Columbus Crew stun Inter Miami, Messi in 2-1 thriller decided late - The Columbus Dispatch",
     "published": "2026-09-28T07:04:05+00:00",
     "summary": "Columbus Crew stun Inter Miami, Messi in 2-1 thriller decided late The Columbus Dispatch"
    },
    {
     "ref": "gnews_inter_miami#17",
     "title": "Why does Lionel Messi’s stunning Inter Miami goal bring him closer to historic soccer records before his Argentina farewell? - beIN SPORTS",
     "published": "2026-09-28T06:52:00+00:00",
     "summary": "Why does Lionel Messi’s stunning Inter Miami goal bring him closer to historic soccer records before his Argentina farewell? beIN SPORTS"
    },
    {
     "ref": "gnews_inter_miami#18",
     "title": "Video: A legendary free-kick from Messi as Columbus Crew steal the match in the 98th minute - goal.com",
     "published": "2026-09-28T06:48:38+00:00",
     "summary": "Video: A legendary free-kick from Messi as Columbus Crew steal the match in the 98th minute goal.com"
    },
    {
     "ref": "gnews_inter_miami#19",
     "title": "Messi Leads Inter Miami Against Crew In Pivotal MLS Clash - Evrim Ağacı",
     "published": "2026-09-28T06:00:39+00:00",
     "summary": "Messi Leads Inter Miami Against Crew In Pivotal MLS Clash Evrim Ağacı"
    },
    {
     "ref": "gnews_inter_miami#20",
     "title": "Messi scores on stunning free kick before Argentina farewell, but Miami slips to defeat - The New York Times",
     "published": "2026-09-28T04:57:49+00:00",
     "summary": "Messi scores on stunning free kick before Argentina farewell, but Miami slips to defeat The New York Times"
    },
    {
     "ref": "gnews_inter_miami#21",
     "title": "Last-minute heroics: Columbus Crew stuns Lionel Messi’s Inter Miami to earn late 2-1 victory - Massive Report",
     "published": "2026-09-28T04:18:47+00:00",
     "summary": "Last-minute heroics: Columbus Crew stuns Lionel Messi’s Inter Miami to earn late 2-1 victory Massive Report"
    },
    {
     "ref": "gnews_inter_miami#22",
     "title": "Lionel Messi scores jaw-dropping free-kick goal from an impossible angle for Inter Miami-WATCH - timesofindia.indiatimes.com",
     "published": "2026-09-28T04:08:00+00:00",
     "summary": "Lionel Messi scores jaw-dropping free-kick goal from an impossible angle for Inter Miami-WATCH timesofindia.indiatimes.com"
    },
    {
     "ref": "gnews_inter_miami#23",
     "title": "Columbus Crew vs. Inter Miami CF - WHIO TV",
     "published": "2026-09-28T04:00:00+00:00",
     "summary": "Columbus Crew vs. Inter Miami CF WHIO TV"
    },
    {
     "ref": "gnews_inter_miami#24",
     "title": "Messi goal not enough to end Inter Miami's winless run - Yahoo Sports",
     "published": "2026-09-28T03:48:00+00:00",
     "summary": "Messi goal not enough to end Inter Miami's winless run Yahoo Sports"
    }
   ]
  },
  {
   "outlet": "Google News — Deni Avdija / Ben Saraf",
   "lang": "en",
   "items": [
    {
     "ref": "gnews_israeli_nba#0",
     "title": "NBA star Deni Avdija gets a namesake: a Persian leopard at Ramat Gan Safari - Ynetnews",
     "published": "2026-09-28T10:02:13+00:00",
     "summary": "NBA star Deni Avdija gets a namesake: a Persian leopard at Ramat Gan Safari Ynetnews"
    },
    {
     "ref": "gnews_israeli_nba#1",
     "title": "Safari names new Persian leopard Deni after NBA's Avdija - jfeed.com",
     "published": "2026-09-28T09:35:00+00:00",
     "summary": "Safari names new Persian leopard Deni after NBA's Avdija jfeed.com"
    },
    {
     "ref": "gnews_israeli_nba#2",
     "title": "Trail Blazers Announce 2026-27 Training Camp Roster - blazers.com",
     "published": "2026-09-27T22:06:00+00:00",
     "summary": "Trail Blazers Announce 2026-27 Training Camp Roster blazers.com"
    },
    {
     "ref": "gnews_israeli_nba#3",
     "title": "Breaking down Nets roster: Where every player stands before season - New York Post",
     "published": "2026-09-27T04:12:00+00:00",
     "summary": "Breaking down Nets roster: Where every player stands before season New York Post"
    },
    {
     "ref": "gnews_israeli_nba#4",
     "title": "Bulls aquire Buddy Hield from Hornets in late-offseason twist - New York Post",
     "published": "2026-09-27T01:40:00+00:00",
     "summary": "Bulls aquire Buddy Hield from Hornets in late-offseason twist New York Post"
    },
    {
     "ref": "gnews_israeli_nba#5",
     "title": "What to Expect From Deni Avdija in 2026-2027 - si.com",
     "published": "2026-09-26T19:00:00+00:00",
     "summary": "What to Expect From Deni Avdija in 2026-2027 si.com"
    },
    {
     "ref": "gnews_israeli_nba#6",
     "title": "Deciding The Number One Option For The Blazers - Yahoo Sports",
     "published": "2026-09-26T13:09:00+00:00",
     "summary": "Deciding The Number One Option For The Blazers Yahoo Sports"
    },
    {
     "ref": "gnews_israeli_nba#7",
     "title": "Portland Trail Blazers stock report entering training camp - Rip City Project",
     "published": "2026-09-26T01:45:00+00:00",
     "summary": "Portland Trail Blazers stock report entering training camp Rip City Project"
    },
    {
     "ref": "gnews_israeli_nba#8",
     "title": "Why Ja Morant isn’t the Biggest Issue for the Trail Blazers This Season - Blazer's Edge",
     "published": "2026-09-25T21:07:34+00:00",
     "summary": "Why Ja Morant isn’t the Biggest Issue for the Trail Blazers This Season Blazer's Edge"
    },
    {
     "ref": "gnews_israeli_nba#9",
     "title": "Blazers are still one trade away from finding Deni Avdija's co-star - Rip City Project",
     "published": "2026-09-25T19:42:14+00:00",
     "summary": "Blazers are still one trade away from finding Deni Avdija's co-star Rip City Project"
    },
    {
     "ref": "gnews_israeli_nba#10",
     "title": "Brooklyn Nets Must Try Three Starting Lineups in 2026-27 - theleadsm.com",
     "published": "2026-09-25T19:23:02+00:00",
     "summary": "Brooklyn Nets Must Try Three Starting Lineups in 2026-27 theleadsm.com"
    }
   ]
  }
 ]
}
</input>