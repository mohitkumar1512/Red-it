from openai import OpenAI

def generate_summary(data):
    client = OpenAI(api_key='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')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant skilled in summarizing texts, making complex information concise and straightforward."},
            {"role": "user", "content": f"Summarize this text: {data}"}
        ]
    )
    summary = response.choices[0].message.content
    summary = summary.strip()
    return summary
    
def remove_special_characters(string):
    string = string.replace('*', '')
    string = string.replace('-', '')
    return string

def generate_flashcard(data): # Function to generate flashcards from the input data. It retunrs a list of parsed flashcards
    client = OpenAI(api_key='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')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant skilled in generating flashcards from texts. Create flashcards that identify key points and their explanations."},
            {"role": "user", "content": f"Generate flashcards from this text: {data} Each flashcard must start with a number (e.g., '1.') and contain key points only, formatted in a single paragraph.Generate a maximum of 10 flashcards."}
        ]
    )
    flashcards = response.choices[0].message.content
    flashcards = flashcards.strip()
    flashcards = flashcards.split("\n")
    parsed_flashcards = []
    for key_point in flashcards:
        if len(key_point) > 3:
            splitted_key_point = key_point.split(" ")
            if len(splitted_key_point) > 1:
                parsed_flashcards.append(" ".join(splitted_key_point[1:]))
    return parsed_flashcards

def generate_powerpoint(data):
    # Implementing a logic similar to generate_summary for PowerPoint content
    client = OpenAI(api_key='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')
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in generating presentation content from texts."},
                {"role": "user", "content": f"Produce presentation slides from the following text: {data}. For each slide, craft content that highlights key points along with their explanations. Begin every slide with a numeral (e.g., '1.'), followed by a slide title, and then the slide's content, all formatted within a single paragraph.  Generate a maximum of 10 slides."}
            ]
        )
    presentation = response.choices[0].message.content
    presentation = presentation.strip()
    slides = presentation.split("\n")
    parsed_slides = []
    for each_slide in slides:
        if len(each_slide) > 3:
            splitted_slide = each_slide.split(" ")
            if len(splitted_slide) > 1:
                parsed_slides.append(" ".join(splitted_slide[1:]))
    length = len(parsed_slides)
    if length > 10 and length%2 ==0:
        updated_slides = []
        for i in range(0, length, 2):
            updated_slides.append(remove_special_characters(parsed_slides[i]) + ": " + parsed_slides[i+1])
        return updated_slides
    return parsed_slides

def generate_context_query(webpage_data, highlighted_text):
    # Combine the webpage data and highlighted query with a suitable prompt
    client = OpenAI(api_key='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')
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in interpreting and explaining texts."},
                {"role": "user", "content": f"Given the following text: {webpage_data}. Please explain the meaning of '{highlighted_text}' in the context of the entire data. Provide your explanation in a single paragraph format, without using any headings or titles. Keep it short and generate 1-2 sentence(s) only. Don't mention the highlighted query in your response."}
            ],
            max_tokens=60 

        )
    explanation = response.choices[0].message.content
    explanation = explanation.strip()
    return explanation

# testing each function on random input data



#data scraped from the webpage
# webpage_data = "Astronomy is a natural science that studies celestial objects and the phenomena that occur in the cosmos. It uses mathematics, physics, and chemistry in order to explain their origin and their overall evolution. Objects of interest include planets, moons, stars, nebulae, galaxies, meteoroids, asteroids, and comets. Relevant phenomena include supernova explosions, gamma ray bursts, quasars, blazars, pulsars, and cosmic microwave background radiation. More generally, astronomy studies everything that originates beyond Earth's atmosphere. Cosmology is a branch of astronomy that studies the universe as a whole.  Astronomy is one of the oldest natural sciences. The early civilizations in recorded history made methodical observations of the night sky. These include the Egyptians, Babylonians, Greeks, Indians, Chinese, Maya, and many ancient indigenous peoples of the Americas. In the past, astronomy included disciplines as diverse as astrometry, celestial navigation, observational astronomy, and the making of calendars. Professional astronomy is split into observational and theoretical branches. Observational astronomy is focused on acquiring data from observations of astronomical objects. This data is then analyzed using basic principles of physics. Theoretical astronomy is oriented toward the development of computer or analytical models to describe astronomical objects and phenomena. These two fields complement each other. Theoretical astronomy seeks to explain observational results and observations are used to confirm theoretical results. Astronomy is one of the few sciences in which amateurs play an active role. This is especially true for the discovery and observation of transient events. Amateur astronomers have helped with many important discoveries, such as finding new comets." 
# highlighted_query = " astronomy studies everything that originates beyond Earth's atmosphere"
# summary_results = generate_context_query(webpage_data, highlighted_query)
# print(summary_results)

# romans_history1 = "The Romans (Latin: Rōmānī; Ancient Greek: Ῥωμαῖοι, romanized: Rhōmaîoi; Greek: Ρωμαίος, romanized: Romaíos)[a] were a cultural group, variously referred to as an ethnicity[2][3][b] or a nationality,[4][5] that in classical antiquity, from the 2nd century BC to the 5th century AD, came to rule large parts of Europe, the Near East and North Africa through conquests made during the Roman Republic and the later Roman Empire. Originally only referring to the Italic Latin citizens of Rome itself, the meaning of \"Roman\" underwent considerable changes throughout the long history of Roman civilisation as the borders of the Roman state expanded and contracted. At times, different groups within Roman society also had different ideas as to what it meant to be Roman. Aspects such as geography, language, and ethnicity could be seen as important by some, whereas others saw Roman citizenship and culture or behaviour as more important.[6][7][8][9] At the height of the Roman Empire, Roman identity was a collective geopolitical identity, extended to nearly all subjects of the Roman emperors and encompassing vast regional and ethnic diversity."
# romans_history2 ="As the land under Roman rule increased from the 4th century BC onwards, Roman citizenship was gradually extended to the various peoples under Roman dominion. Citizenship grants, demographic growth, and settler and military colonies rapidly increased the number of Roman citizens. The increase achieved its peak with Emperor Caracalla's AD 212 Antonine Constitution, which extended citizenship rights to all free inhabitants of the empire. It is for the most part not clear to what extent the majority of Roman citizens in antiquity regarded themselves as being Roman. Most likely, local identities were prominent throughout the Roman Empire due to its vast geographical extent, but Roman identity provided a larger sense of common identity and became important when distinguishing from non-Romans, such as barbarian settlers and invaders.[11][12] Roman culture was far from homogeneous; though there was a predominant Hellenistic-inspired cultural idiom, one of the strengths of the Roman Empire was also its ability to incorporate traditions from other cultures. Rome's cultural flexibility precluded the development of a strong Roman 'core identity' in Italy, but also contributed to the empire's longevity."
# romans_history3 ="Border changes of the Roman state from 6th century BC to 15th century AD"
# romans_history4="The Roman Empire affected the personal identities of its subject peoples to a considerable extent and Roman identity lasted throughout the lands of the empire until long after the Roman Empire itself had faded away. The collapse of the Western Roman Empire in the 5th century ended the political domination of the Roman Empire in Western Europe, but Roman identity survived in the west as an important political resource. Through the failures of the surviving Eastern Roman Empire, also called the Byzantine Empire, of reconquering and keeping control of the west and suppression from the new Germanic kingdoms, Roman identity faded away in the west, more or less disappearing in the 8th and 9th centuries. Increasingly, Western Europeans only began applying the designation of Roman to the citizens of the city of Rome itself. In the Greek-speaking east, still under imperial control, Roman identity survived until the fall of the Byzantine Empire in 1453 and beyond, though it increasingly transformed into an ethnic identity, marked by Greek language and adherence to Orthodox Christianity, a precursor to modern Greek ethnic identity. The two major groups still clinging to Roman identity throughout the Middle Ages—the Byzantine Greeks of the eastern empire and the citizens of Rome itself—drifted apart linguistically and religiously and eventually ceased to recognise each other as Roman."
# romans_history5="Whereas Roman identity faded away in most of the lands where it was once prominent, for some regions and peoples it proved considerably more tenacious. In Italy, Romans (Romani in Latin and Italian) has continuously and uninterruptedly been the demonym of the citizens of Rome (Roma in Latin and Italian) from the foundation of the city to the present-day. During the Eastern Roman Empire and for some time after its fall, Greeks identified as Romioi, or related names, though the earlier concept of Hellenes eventually returned supreme. In the Alps, Roman identity survived uninterrupted, despite Frankish efforts at suppression, in the names of two groups in Switzerland that still evokes their descent from these populations: the Romands and the Romansh people. Several ethnonyms of the Eastern Romance peoples, whose descent in most cases is unclear, evoke Roman identity. Several names derive from the Latin Romani (such as the Romanians, Aromanians and Istro-Romanians), or from the Germanic walhaz (a term originally referring to the Romans; adopted in the form Vlach as the self-designation of the Megleno-Romanians)."

# ppt = generate_powerpoint(romans_history1+romans_history2+romans_history3+romans_history4+romans_history5)
# print(ppt)
