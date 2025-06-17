import os
from datetime import datetime, timedelta

# Folder where posts will be saved
POSTS_DIR = "posts"

# Define the rotating themes and sample content
theme_samples = [
    ("🎧 Track Tuesday", "# 🎧 Track Tuesday: \"The Only One I Know\" – The Charlatans (1990)\n\nBaggy jeans. Long sleeves under T-shirts. And that signature swirling Hammond organ.\n\nThis was the track that made you feel cool just walking to the corner shop. The Charlatans' breakout tune felt like Madchester swagger in a bottle. If you were lucky, this would come on just before kick-off at a Uni bar, setting the tone for the whole night.\n\nThe pitch might’ve been muddy, but the vibes were always immaculate.\n\n> “The only one I know has come to take me away…”\n\n#90sIndie #TheCharlatans #Madchester"),

    ("👟 Boots, Beers & Britpop", "# 👟 Boots, Beers & Britpop: Adidas Predators & Pub Quizzes\n\nNothing screamed football dominance in the mid-90s quite like a pair of Adidas Predators. You weren’t just turning up to play — you were *turning up to dominate*.\n\nPair that with a Britpop-heavy pub quiz soundtrack — maybe a pint of John Smith’s and a dodgy Oasis B-side playing over the PA — and you’ve got a Wednesday night in heaven.\n\nPreds on the pitch. Parka off the stool. Always ready.\n\n#AdidasPredators #BritpopCulture #90sFootball"),

    ("📅 On This Day", "# 📅 On This Day: June 19, 1996 – England 4–1 Netherlands\n\nGazza ran the midfield. Shearer netted two. Wembley *roared*.\n\nOn this very day in ‘96, England demolished the Dutch with the kind of fluid football that had every lad thinking we might actually win something. In the background? “Don’t Look Back in Anger” and “Three Lions” blasting from car stereos.\n\nThe summer of sun, hope, and waistcoats.\n\n> “Football’s coming home” wasn’t just a lyric — it was *the vibe*.\n\n#Euro96 #ThreeLions #BritpopEra"),

    ("🧢 Friday Five-A-Side", "# 🧢 Friday Five-A-Side: 5 Things Every 90s Lads Team Had\n\n1. One lad in *full* Umbro gear — always took warm-ups too seriously\n2. Someone rocking a Kappa jacket on the sidelines\n3. Ciggy break before *and* after the game\n4. Oasis blasting from someone’s Peugeot 205\n5. At least one goal scored with a no-look toe-poke and celebrated like Baggio\n\nAnd of course, someone always forgot the ball.\n\n#5aside #90sVibes #PubLeagueLegends"),

    ("🏟 Stadium Sounds", "# 🏟 Stadium Sounds: \"Live Forever\" – Oasis\n\nSome songs just belong on the terraces.\n\n“Live Forever” wasn’t about football, but try telling that to 30,000 fans belting it after a last-minute winner. It was the 90s anthem that said, “we’re untouchable.”\n\nUnited, Newcastle, even Spurs — it didn't matter who you supported. Everyone had that mate who thought they *were* Liam Gallagher.\n\n> “You and I are gonna live forever…”\n\n#StadiumAnthem #Oasis #90sFootball"),

    ("📻 Mixtape Sunday", "# 📻 Mixtape Sunday: The Chill Side of Britpop\n\nSundays in the 90s weren’t complete without mixtapes full of mellow gems:\n\n- “Dry the Rain” – The Beta Band\n- “Road to Nowhere” – Talking Heads\n- “Sing” – Travis\n- “Northern Sky” – Nick Drake\n- “Let Down” – Radiohead\n\nFeet up. Tea brewed. Highlights on later. Bliss.\n\n#MixtapeSunday #90sChill #FootyRecovery"),

    ("⚽ Matchday Memories", "# ⚽ Matchday Memories: Arsenal vs Man Utd – Highbury, 1999\n\nThe buildup felt electric — Bergkamp vs. Keane, Wenger vs. Fergie. A clash that *defined* the era.\n\nRain-soaked stands. Raucous chants. Sol Campbell on a rampage. And if you had the telly on loud enough, you’d swear the Blur CD in the kitchen was syncing perfectly with the Sky Sports intro.\n\nTurf, tracksuits, and tension.\n\n#HighburyNights #90sFootball #MatchdayFeels")
]


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def generate_posts(start_date, days=7):
    ensure_dir(POSTS_DIR)
    for i in range(days):
        date = start_date + timedelta(days=i)
        theme_index = i % len(theme_samples)
        theme, content = theme_samples[theme_index]
        filename = os.path.join(POSTS_DIR, f"{date.strftime('%Y-%m-%d')}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {filename}")


if __name__ == "__main__":
    today = datetime.today()
    generate_posts(today, 7)
