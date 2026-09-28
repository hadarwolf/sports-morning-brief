Write the Learn Something Small section: exactly 2 short stories.

1. Word or concept of the day (kind "word"). Today's rotation: philosophy term.
   - Choose something genuinely useful that isn't too basic for this reader. Don't repeat anything in recent_words_and_concepts.
   - headline: the term. For vocabulary, give the English word and its Hebrew equivalent.
   - scroll: a crisp definition.
   - coffee: an explanation with an example.
   - deep: 250-400 words (shorter than usual), covering origin or etymology, nuances, common confusions and usage examples.
   - source_refs: [].
2. On this day (kind "on_this_day").
   - Pick the most consequential or fascinating event from on_this_day_candidates.
   - The headline starts with the year.
   - coffee explains the context and why it mattered. deep is 250-400 words.
   - source_refs: the event's ref.

This section opens in English by default, so make the English version your best writing.

Output: write `drafts/learn.json` matching `schemas/learn.schema.json`.

<input>
{
 "on_this_day_candidates": [
  {
   "ref": "wikipedia#0",
   "year": 2023,
   "text": "The Sycamore Gap tree (pictured) in Northumberland, England, was illegally felled.",
   "context": [
    "The Sycamore Gap tree, also known as the Robin Hood tree, is a 150-year-old sycamore tree next to Hadrian's Wall near Crag Lough in Northumberland, England. It was illegally felled in 2023 by Daniel Graham and Adam Carruthers, but has since sprouted a thick ring of shoots from the stump. Standing in a dip in the landscape created by glacial meltwater, it was one of the country's most photographed trees and an emblem for the North East of England. Its alternative name is derived from featuring in a scene in the 1991 film Robin Hood: Prince of Thieves. The tree won the Woodland Trust 2016 England Tree of the Year award, receiving a £1,000 care grant funded by the People's Postcode Lottery."
   ]
  },
  {
   "ref": "wikipedia#1",
   "year": 2012,
   "text": "War in Somalia: Somali National Army forces and their AMISOM and Raskamboni allies launched an offensive against Al-Shabaab in the latter's last major stronghold of Kismayo.",
   "context": [
    "The ongoing phase of the Somali Civil War began in 2009 and is concentrated in southern and central Somalia, primarily between the forces of the Federal Government of Somalia (FGS), assisted by African Union peacekeeping forces, and the Islamist militant group al-Shabaab, which pledged allegiance to al-Qaeda in 2012."
   ]
  },
  {
   "ref": "wikipedia#2",
   "year": 2009,
   "text": "A protest held by 50,000 people in Conakry, Guinea, was forcefully disrupted by the military junta, resulting in at least 157 deaths and over 1,200 injuries.",
   "context": [
    "The 2009 Guinean protests were an opposition rally in Conakry, Guinea on 28 September 2009, with about 50,000 participants demonstrating against the junta government that came to power after the 2008 Guinean coup d'état in December. The protest march was fueled by the indication of junta leader Captain Moussa Dadis Camara that he would break his pledge to not run in the next presidential vote, due in January 2010. The government had already banned any form of protests until 2 October. When the demonstrators gathered in a large stadium, the security forces opened fire on them. At least 157 demonstrators were killed, 1,253 were injured, and 30—including Cellou Dalein Diallo, the leader of the opposition Union of Democratic Forces of Guinea (UDFG)—were arrested and taken away in lorries."
   ]
  },
  {
   "ref": "wikipedia#3",
   "year": 2006,
   "text": "Typhoon Xangsane passed Manila on its way to causing more than 300 deaths, mostly in the Phillippines and Vietnam.",
   "context": [
    "Typhoon Xangsane, known in the Philippines as Typhoon Milenyo, was a strong and deadly typhoon that affected the Philippines, and Indochina during the 2006 Pacific typhoon season."
   ]
  },
  {
   "ref": "wikipedia#4",
   "year": 1978,
   "text": "Pope John Paul I died only 33 days after his papal election due to an apparent myocardial infarction, resulting in the first year of three popes since 1605.",
   "context": [
    "Pope John Paul I was head of the Catholic Church and sovereign of Vatican City from 26 August 1978 until his death 33 days later. His reign is among the shortest in papal history, giving rise to the first year of three popes since 1605. John Paul I remains the most recent Italian-born pope, the last in a succession of such popes that started with Clement VII in 1523. He was the first pope to have been born in the 20th century, as well as the last pope to die in it."
   ]
  },
  {
   "ref": "wikipedia#5",
   "year": 1975,
   "text": "An attempted robbery of Spaghetti House, a restaurant in Knightsbridge, London, turned into a six-day hostage situation.",
   "context": [
    "Knightsbridge is a residential and retail district in central London, south of Hyde Park. It is identified in the London Plan as one of two international retail centres in London, alongside the West End. Knightsbridge is also the name of the roadway which runs near the south side of Hyde Park from Hyde Park Corner."
   ]
  },
  {
   "ref": "wikipedia#6",
   "year": 1972,
   "text": "Against the backdrop of the Cold War, the Canadian ice hockey team defeated the Soviet team in the Summit Series.",
   "context": [
    "The Cold War was a period of international geopolitical rivalry between the United States (US) and the Soviet Union (USSR) and their respective allies, the capitalist Western Bloc and communist Eastern Bloc. It began in the aftermath of the Second World War and ended with the dissolution of the Soviet Union in 1991. The term cold war is used because there was no direct fighting between the two superpowers, though each supported opposing sides in regional conflicts known as proxy wars. In addition to the struggle for ideological and economic influence and an arms race in both conventional and nuclear weapons, the Cold War was expressed through technological rivalries such as the Space Race, espionage, propaganda campaigns, embargoes, and sports diplomacy."
   ]
  },
  {
   "ref": "wikipedia#7",
   "year": 1963,
   "text": "Whaam!, now considered one of Roy Lichtenstein's most important works, debuted at an exhibition held at the Leo Castelli Gallery, New York City.",
   "context": [
    "Whaam! is a 1963 diptych painting by the American artist Roy Lichtenstein. It is one of the best-known works of pop art, and among Lichtenstein's most important paintings. Whaam! was first exhibited at the Leo Castelli Gallery in New York City in 1963, and purchased by the Tate Gallery, London, in 1966. It has been on permanent display at Tate Modern since 2006."
   ]
  },
  {
   "ref": "wikipedia#8",
   "year": 1958,
   "text": "Fernando Rios, a Mexican tour guide in New Orleans, was killed in an instance of gay bashing.",
   "context": [
    "New Orleans is a consolidated city-parish located along the Mississippi River in the U.S. state of Louisiana. With a population of 383,997 at the 2020 census, New Orleans is the most populous city in Louisiana, the second-most populous in the Deep South, and the twelfth-most populous in the Southeastern United States; the New Orleans metropolitan area, with about 1 million residents, is the 59th-most populous metropolitan area in the United States. New Orleans serves as a major port and commercial hub for the broader Gulf Coast region. The city is coextensive with Orleans Parish."
   ]
  },
  {
   "ref": "wikipedia#9",
   "year": 1928,
   "text": "Scottish biologist and pharmacologist Alexander Fleming (pictured) discovered penicillin when he noticed a bacteria-killing mould growing in his laboratory.",
   "context": [
    "Sir Alexander Fleming was a Scottish physician and microbiologist. He shared the 1945 Nobel Prize in Physiology or Medicine with Howard Florey and Ernst Chain \"for the discovery of penicillin and its curative effect in various infectious diseases\".\nThis was the first antibiotic substance discovered. His discovery in 1928 of what was later named benzylpenicillin from the mould Penicillium rubens has been described as the \"single greatest victory ever achieved over disease\"."
   ]
  },
  {
   "ref": "wikipedia#10",
   "year": 1924,
   "text": "A team of U.S. Army Air Service aviators landed in Seattle, Washington, to complete the first aerial circumnavigation of the world.",
   "context": [
    "The United States Army Air Service (USAAS) was the aerial warfare service component of the United States Army between 1918 and 1926 and a forerunner of the United States Air Force. It was established as an independent but temporary branch of the U.S. War Department during World War I by two executive orders of President Woodrow Wilson: on May 24, 1918, replacing the Aviation Section, Signal Corps as the nation's air force; and March 19, 1919, establishing a military Director of Air Service to control all aviation activities. Its life was extended for another year in July 1919, during which time Congress passed the legislation necessary to make it a permanent establishment. The National Defense Act of 1920 assigned the Air Service the status of \"combatant arm of the line\" of the United States Army with a major general in command."
   ]
  },
  {
   "ref": "wikipedia#11",
   "year": 1901,
   "text": "Philippine–American War: Filipino guerrillas killed more than forty American soldiers in a surprise attack on the town of Balangiga on the island of Samar.",
   "context": [
    "The Philippine–American War, known alternatively as the Filipino–American War, Philippine Insurrection, or Tagalog Insurgency, emerged in early 1899 following the United States' annexation of the former Spanish colony of the Philippine Islands under the terms of the December 1898 Treaty of Paris following the Spanish–American War. Philippine nationalists had proclaimed independence in June 1898 and constituted the First Philippine Republic in January 1899. The United States did not recognize either event as legitimate, and tensions escalated until fighting commenced on February 4, 1899, in the Battle of Manila."
   ]
  },
  {
   "ref": "wikipedia#12",
   "year": 1821,
   "text": "The Declaration of Independence of the Mexican Empire from Spain was drafted in the National Palace in Mexico City.",
   "context": [
    "The Declaration of Independence of the Mexican Empire is the document by which Mexico declared independence from the Spanish Empire. This founding document of the Mexican nation was drafted in the National Palace in Mexico City on 28 September 1821, by Juan José Espinosa de los Monteros, secretary of the Provisional Governmental Board."
   ]
  },
  {
   "ref": "wikipedia#13",
   "year": 1106,
   "text": "In the Battle of Tinchebray in Normandy, the invading King Henry I of England captured his brother Robert Curthose.",
   "context": [
    "The Battle of Tinchebray took place on 28 September 1106, in Tinchebray, Normandy, between an invading force led by King Henry I of England, and the Norman army of his elder brother Robert Curthose, the Duke of Normandy. Henry's knights won a decisive victory: they captured Robert, and Henry imprisoned him in England and then in Wales until Robert's death in 1134."
   ]
  },
  {
   "ref": "wikipedia#14",
   "year": 1066,
   "text": "William the Conqueror and his fleet of around 600 ships landed at Pevensey, Sussex, beginning the Norman conquest of England.",
   "context": [
    "William the Conqueror, sometimes called William the Bastard, was the first Norman king of England, reigning from 1066 until his death. A descendant of Rollo, he was Duke of Normandy from 1035 onward. By 1060, following a long struggle, his hold on Normandy was secure. In 1066, following the death of Edward the Confessor, William invaded England, leading a Franco-Norman army to victory over the Anglo-Saxon forces of Harold Godwinson at the Battle of Hastings. He suppressed subsequent English revolts in what has become known as the Norman Conquest. The rest of his life was marked by struggles to consolidate his hold over England and his continental lands, and by difficulties with his eldest son, Robert Curthose."
   ]
  },
  {
   "ref": "wikipedia#15",
   "year": 351,
   "text": "The Eastern Roman armies under Constantius II defeated those of the usurper Magnentius at the Battle of Mursa Major.",
   "context": [
    "Constantius II was Roman emperor from 337 to 361. His reign saw constant warfare on the borders against the Sasanian Empire and Germanic peoples, while internally the Roman Empire went through repeated civil wars, court intrigues, and usurpations. His religious policies inflamed domestic conflicts that would continue after his death."
   ]
  },
  {
   "ref": "wikipedia#16",
   "year": 235,
   "text": "Pope Pontian resigned after being exiled to Sardinia, becoming the first pope to relinquish the position.",
   "context": [
    "Pope Pontian was the bishop of Rome from 21 July 230 to 28 September 235. In 235, during the persecution of Christians in the reign of the Emperor Maximinus Thrax, Pontian was arrested and sent to the island of Sardinia."
   ]
  },
  {
   "ref": "wikipedia#17",
   "year": -48,
   "text": "Pompey was killed by Lucius Septimius at Pelusium in Egypt.",
   "context": [
    "Gnaeus Pompeius Magnus, known in English as Pompey or Pompey the Great, was a Roman general and statesman who was prominent in the final decades of the Roman Republic. As a young man, he was a partisan and protégé of the dictator Sulla, after whose death he achieved significant military and political success."
   ]
  }
 ],
 "recent_words_and_concepts": []
}
</input>