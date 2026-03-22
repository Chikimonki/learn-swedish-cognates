import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Add your existing tutor logic as API endpoints 
class CognaticSwedishTutor:
    def __init__(self):
        self.cognates = {
            'perfect': {
                'arm': {'english': 'arm', 'meaning': 'arm', 'example': 'Min arm är stark.', 'example_english': 'My arm is strong.'},
                'bank': {'english': 'bank', 'meaning': 'bank', 'example': 'Jag går till banken.', 'example_english': 'I go to the bank.'},
                'film': {'english': 'film', 'meaning': 'film', 'example': 'Vi tittar på en film.', 'example_english': 'We are watching a film.'},
                'hotell': {'english': 'hotel', 'meaning': 'hotel', 'example': 'Hotellrummet är stort.', 'example_english': 'The hotel room is large.'},
                'problem': {'english': 'problem', 'meaning': 'problem', 'example': 'Vi har ett problem.', 'example_english': 'We have a problem.'},
                'system': {'english': 'system', 'meaning': 'system', 'example': 'Systemet fungerar bra.', 'example_english': 'The system works well.'},
                'student': {'english': 'student', 'meaning': 'student', 'example': 'Hon är student.', 'example_english': 'She is a student.'},
                'universitet': {'english': 'university', 'meaning': 'university', 'example': 'Stockholms universitet är stort.', 'example_english': 'Stockholm University is large.'},
                'akt': {'english': 'act', 'meaning': 'act', 'example': 'Det var en vänlig akt.', 'example_english': 'It was a friendly act.'},
                'aktiv': {'english': 'active', 'meaning': 'active', 'example': 'Han är mycket aktiv.', 'example_english': 'He is very active.'},
                'adress': {'english': 'address', 'meaning': 'address', 'example': 'Skriv din adress här.', 'example_english': 'Write your address here.'},
                'agent': {'english': 'agent', 'meaning': 'agent', 'example': 'Han är en hemlig agent.', 'example_english': 'He is a secret agent.'},
                'alkohol': {'english': 'alcohol', 'meaning': 'alcohol', 'example': 'Alkohol är farligt.', 'example_english': 'Alcohol is dangerous.'},
                'allergisk': {'english': 'allergic', 'meaning': 'allergic', 'example': 'Jag är allergisk mot nötter.', 'example_english': 'I am allergic to nuts.'},
                'apartment': {'english': 'apartment', 'meaning': 'apartment', 'example': 'Mitt apartment är litet.', 'example_english': 'My apartment is small.'},
                'attack': {'english': 'attack', 'meaning': 'attack', 'example': 'Attacken var plötslig.', 'example_english': 'The attack was sudden.'},
                'augusti': {'english': 'august', 'meaning': 'august', 'example': 'I augusti åker vi på semester.', 'example_english': 'In August we go on vacation.'},
                'badrum': {'english': 'bathroom', 'meaning': 'bathroom', 'example': 'Badrummet är rent.', 'example_english': 'The bathroom is clean.'},
                'balkong': {'english': 'balcony', 'meaning': 'balcony', 'example': 'Vi sitter på balkongen.', 'example_english': 'We sit on the balcony.'},
                'banana': {'english': 'banana', 'meaning': 'banana', 'example': 'Jag äter en banana.', 'example_english': 'I eat a banana.'},
                'cement': {'english': 'cement', 'meaning': 'cement', 'example': 'Cementen hårdnar.', 'example_english': 'The cement is hardening.'},
                'central': {'english': 'central', 'meaning': 'central', 'example': 'Stationen är central.', 'example_english': 'The station is central.'},
                'chans': {'english': 'chance', 'meaning': 'chance', 'example': 'Ge mig en chans!', 'example_english': 'Give me a chance!'},
                'choklad': {'english': 'chocolate', 'meaning': 'chocolate', 'example': 'Jag älskar choklad.', 'example_english': 'I love chocolate.'},
                'cirkel': {'english': 'circle', 'meaning': 'circle', 'example': 'Rita en cirkel.', 'example_english': 'Draw a circle.'},
                'citron': {'english': 'lemon', 'meaning': 'lemon', 'example': 'Citronen är sur.', 'example_english': 'The lemon is sour.'},
                'dans': {'english': 'dance', 'meaning': 'dance', 'example': 'Dans är roligt.', 'example_english': 'Dance is fun.'},
                'debatt': {'english': 'debate', 'meaning': 'debate', 'example': 'Debatten var intensiv.', 'example_english': 'The debate was intense.'},
                'december': {'english': 'december', 'meaning': 'december', 'example': 'I december är det jul.', 'example_english': 'In December it is Christmas.'},
                'demokrati': {'english': 'democracy', 'meaning': 'democracy', 'example': 'Demokrati är viktigt.', 'example_english': 'Democracy is important.'},
                'design': {'english': 'design', 'meaning': 'design', 'example': 'Designen är modern.', 'example_english': 'The design is modern.'},
                'diamant': {'english': 'diamond', 'meaning': 'diamond', 'example': 'Diamanten är vacker.', 'example_english': 'The diamond is beautiful.'},
                'digital': {'english': 'digital', 'meaning': 'digital', 'example': 'Världen blir digital.', 'example_english': 'The world is becoming digital.'},
                'direkt': {'english': 'direct', 'meaning': 'direct', 'example': 'Ge mig ett direkt svar.', 'example_english': 'Give me a direct answer.'},
                'elefant': {'english': 'elephant', 'meaning': 'elephant', 'example': 'Elefanten är stor.', 'example_english': 'The elephant is large.'},
                'energi': {'english': 'energy', 'meaning': 'energy', 'example': 'Jag har ingen energi.', 'example_english': 'I have no energy.'},
                'entré': {'english': 'entrance', 'meaning': 'entrance', 'example': 'Entrén är där.', 'example_english': 'The entrance is there.'},
                'exakt': {'english': 'exact', 'meaning': 'exact', 'example': 'Det är exakt rätt.', 'example_english': 'It is exactly right.'},
                'fabrik': {'english': 'factory', 'meaning': 'factory', 'example': 'Fabriken är stor.', 'example_english': 'The factory is large.'},
                'familj': {'english': 'family', 'meaning': 'family', 'example': 'Min familj är här.', 'example_english': 'My family is here.'},
                'fantastisk': {'english': 'fantastic', 'meaning': 'fantastic', 'example': 'Det är fantastiskt!', 'example_english': 'It is fantastic!'},
                'festival': {'english': 'festival', 'meaning': 'festival', 'example': 'Festivalen var rolig.', 'example_english': 'The festival was fun.'},
                'foto': {'english': 'photo', 'meaning': 'photo', 'example': 'Ta ett foto.', 'example_english': 'Take a photo.'},
                'garage': {'english': 'garage', 'meaning': 'garage', 'example': 'Bilen står i garaget.', 'example_english': 'The car is in the garage.'},
                'global': {'english': 'global', 'meaning': 'global', 'example': 'Det är ett globalt problem.', 'example_english': 'It is a global problem.'},
                'gratis': {'english': 'free', 'meaning': 'free of charge', 'example': 'Det är gratis.', 'example_english': 'It is free.'},
            },
            'near': {
                'äpple': {'english': 'apple', 'meaning': 'apple', 'example': 'Ett rött äpple.', 'example_english': 'A red apple.'},
                'bok': {'english': 'book', 'meaning': 'book', 'example': 'Jag läser en bok.', 'example_english': 'I am reading a book.'},
                'fisk': {'english': 'fish', 'meaning': 'fish', 'example': 'Fiskar simmar i havet.', 'example_english': 'Fish swim in the sea.'},
                'hus': {'english': 'house', 'meaning': 'house', 'example': 'Vårt hus är rött.', 'example_english': 'Our house is red.'},
                'hand': {'english': 'hand', 'meaning': 'hand', 'example': 'Min höger hand.', 'example_english': 'My right hand.'},
                'mamma': {'english': 'mama', 'meaning': 'mother', 'example': 'Min mamma lagar mat.', 'example_english': 'My mother cooks food.'},
                'pappa': {'english': 'papa', 'meaning': 'father', 'example': 'Min pappa arbetar.', 'example_english': 'My father works.'},
                'skola': {'english': 'school', 'meaning': 'school', 'example': 'Barnen går i skolan.', 'example_english': 'The children go to school.'},
                'aktuell': {'english': 'current', 'meaning': 'current/topical', 'example': 'Det är en aktuell fråga.', 'example_english': 'It is a current issue.'},
                'apelsin': {'english': 'orange', 'meaning': 'orange fruit', 'example': 'Apelsinen är söt.', 'example_english': 'The orange is sweet.'},
                'arbete': {'english': 'work/job', 'meaning': 'work/job', 'example': 'Arbetet är slut för idag.', 'example_english': 'Work is finished for today.'},
                'ben': {'english': 'leg/bone', 'meaning': 'leg or bone', 'example': 'Mitt ben gör ont.', 'example_english': 'My leg hurts.'},
                'bil': {'english': 'car', 'meaning': 'car', 'example': 'Bilen är blå.', 'example_english': 'The car is blue.'},
                'bild': {'english': 'picture/image', 'meaning': 'picture/image', 'example': 'Bilden är vacker.', 'example_english': 'The picture is beautiful.'},
                'bli': {'english': 'to become/get', 'meaning': 'to become/get', 'example': 'Jag vill bli läkare.', 'example_english': 'I want to become a doctor.'},
                'blomma': {'english': 'flower', 'meaning': 'flower', 'example': 'Blomman doftar.', 'example_english': 'The flower smells.'},
                'bord': {'english': 'table', 'meaning': 'table', 'example': 'Bordet är dukat.', 'example_english': 'The table is set.'},
                'dricka': {'english': 'to drink', 'meaning': 'to drink', 'example': 'Jag vill dricka vatten.', 'example_english': 'I want to drink water.'},
                'fotboll': {'english': 'football/soccer', 'meaning': 'football/soccer', 'example': 'Fotboll är populärt.', 'example_english': 'Football is popular.'},
                'fråga': {'english': 'question', 'meaning': 'question', 'example': 'Jag har en fråga.', 'example_english': 'I have a question.'},
                'färdig': {'english': 'ready/finished', 'meaning': 'ready/finished', 'example': 'Är du färdig?', 'example_english': 'Are you ready?'},
                'förstå': {'english': 'to understand', 'meaning': 'to understand', 'example': 'Jag förstår inte.', 'example_english': 'I don\'t understand.'},
                'granne': {'english': 'neighbor', 'meaning': 'neighbor', 'example': 'Min granne är trevlig.', 'example_english': 'My neighbor is nice.'},
            },
            'false_friends': {
                'bra': {'english': 'bra', 'meaning': 'good (not underwear)', 'example': 'Det är bra väder idag.', 'example_english': 'The weather is good today.'},
                'glass': {'english': 'glass', 'meaning': 'ice cream (not glass)', 'example': 'Jag älskar glass.', 'example_english': 'I love ice cream.'},
                'kock': {'english': 'cook', 'meaning': 'cook', 'example': 'Kocken lagar mat.', 'example_english': 'The cook prepares food.'},
                'semester': {'english': 'semester', 'meaning': 'vacation (not academic term)', 'example': 'Vi åker på semester.', 'example_english': 'We go on vacation.'},
                'fart': {'english': 'fart', 'meaning': 'speed (not flatulence)', 'example': 'Bilens fart är hög.', 'example_english': 'The car\'s speed is high.'},
                'kiss': {'english': 'kiss', 'meaning': 'pee (not affectionate gesture)', 'example': 'Hunden kissar på trädet.', 'example_english': 'The dog pees on the tree.'},
                'puss': {'english': 'kiss', 'meaning': 'kiss', 'example': 'Ge mig en puss.', 'example_english': 'Give me a kiss.'},
                'rock': {'english': 'rock', 'meaning': 'skirt (not stone)', 'example': 'Hon köpte en ny rock.', 'example_english': 'She bought a new skirt.'},
                'gift': {'english': 'gift', 'meaning': 'married/poison (not present)', 'example': 'Han är gift med henne.', 'example_english': 'He is married to her.'},
            }
        }

    def get_cognate_type(self, swedish_word):
        for category, words in self.cognates.items():
            if swedish_word in words:
                return category
        return None

    def generate_flashcards(self, count=5):
        print("\n" + "="*60)
        print("🇸🇪 SWEDISH COGNATE FLASHCARDS")
        print("="*60)
        
        all_words = []
        for category, words in self.cognates.items():
            for swedish, data in words.items():
                all_words.append((swedish, data, category))
        
        selected = random.sample(all_words, min(count, len(all_words)))
        
        for i, (swedish, data, category) in enumerate(selected, 1):
            type_display = {
                'perfect': '🔹 PERFECT FRIEND',
                'near': '🔸 NEAR FRIEND', 
                'false_friends': '⚠️ FALSE FRIEND'
            }
            
            print(f"\n🎴 Card {i}: {type_display.get(category, 'Unknown')}")
            print(f"🇸🇪 Swedish: {swedish}")
            input("Press Enter to reveal...")
            
            print(f"🇺🇸 English: {data['english']}")
            print(f"📖 Meaning: {data['meaning']}")
            print(f"💬 Example SV: {data['example']}")
            print(f"💬 Example EN: {data['example_english']}")
            
            print("\n🧠 COGNATE INSIGHT:")
            if category == 'perfect':
                print("   ✅ Same meaning and similar spelling!")
                print("   💡 These are your fastest vocabulary builders!")
            elif category == 'near':
                print("   🔸 Similar but watch for spelling/meaning nuances!")
                print("   💡 Pay attention to the subtle differences!")
            elif category == 'false_friends':
                print("   ⚠️ DANGER! Similar appearance but different meaning!")
                print("   💡 Memorize these to avoid embarrassing mistakes!")
            
            print("-" * 60)

    def cognate_quiz(self):
        print("\n" + "="*60)
        print("🇸🇪 SWEDISH COGNATE QUIZ")
        print("="*60)
        
        score = 0
        all_cognates = []
        for category, words in self.cognates.items():
            for swedish, data in words.items():
                all_cognates.append((swedish, data, category))
        
        quiz_words = random.sample(all_cognates, min(8, len(all_cognates)))
        
        for i, (swedish, data, category) in enumerate(quiz_words, 1):
            print(f"\n❓ Question {i}/{len(quiz_words)}:")
            
            other_answers = [item[1]['english'] for item in all_cognates if item[1]['english'] != data['english']]
            wrong_options = random.sample(other_answers, 3)
            options = wrong_options + [data['english']]
            random.shuffle(options)
            
            print(f"What does '{swedish}' mean?")
            for idx, option in enumerate(options, 1):
                print(f"  {idx}. {option}")
            
            try:
                answer = int(input("Your choice (1-4): ")) - 1
                if 0 <= answer < 4 and options[answer] == data['english']:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong!")
                
                print(f"\n🎯 Correct answer: {data['english']}")
                print(f"📖 Meaning: {data['meaning']}")
                print(f"💬 Example SV: {data['example']}")
                print(f"💬 Example EN: {data['example_english']}")
                
                print("\n🧠 COGNATE ANALYSIS:")
                if category == 'perfect':
                    print("   🔹 PERFECT FRIEND - Safe to use!")
                    print(f"   '{swedish}' ≈ '{data['english']}' (same meaning)")
                elif category == 'near':
                    print("   🔸 NEAR FRIEND - Use with caution!")
                    print(f"   '{swedish}' ~ '{data['english']}' (similar but not identical)")
                elif category == 'false_friends':
                    print("   ⚠️ FALSE FRIEND - Dangerous trap!")
                    print(f"   '{swedish}' ≠ '{data['english']}' (different meaning!)")
                
                print("-" * 60)
                
            except:
                print(f"❌ Invalid input. The correct answer is: {data['english']}")
                print("-" * 60)
        
        percentage = (score / len(quiz_words)) * 100
        print(f"\n🎯 FINAL SCORE: {score}/{len(quiz_words)} ({percentage:.1f}%)")
        
        if percentage >= 80:
            print("🏆 Excellent! Du är fantastisk!")
        elif percentage >= 60:
            print("👍 Bra jobbat! Fortsätt så!")
        else:
            print("💪 Keep learning! Focus on the false friends!")

    def sentence_builder(self):
        print("\n" + "="*60)
        print("🇸🇪 SWEDISH SENTENCE BUILDER")
        print("="*60)
        
        templates = [
            "{noun} är väldigt {adjective}.",
            "Jag har en {noun} med min {family}.",
            "{noun} i detta {place} är {adjective}.",
            "Mitt {noun} har ett {object}.",
            "Vi går till {place} för {activity}."
        ]
        
        word_bank = {
            'nouns': ['film', 'hotell', 'problem', 'bil', 'bok', 'student'],
            'adjectives': ['bra', 'fantastisk', 'aktiv', 'global'],
            'family': ['familj', 'mamma', 'pappa'],
            'places': ['skola', 'universitet', 'bank', 'badrum'],
            'objects': ['problem', 'system', 'foto'],
            'activities': ['semester', 'festival', 'dans']
        }
        
        for i in range(3):
            template = random.choice(templates)
            swedish_sentence = template
            english_sentence = template
            
            placeholders = ['{noun}', '{adjective}', '{family}', '{place}', '{object}', '{activity}']
            for placeholder in placeholders:
                if placeholder in swedish_sentence:
                    category = placeholder[1:-1]
                    if category in word_bank:
                        word = random.choice(word_bank[category])
                        swedish_sentence = swedish_sentence.replace(placeholder, word, 1)
                        eng_word = self.get_english_translation(word)
                        english_sentence = english_sentence.replace(placeholder, eng_word, 1)
            
            print(f"\n🔨 Generated Sentence {i+1}:")
            print(f"🇸🇪 Swedish:  {swedish_sentence}")
            print(f"🇺🇸 English: {english_sentence}")
            
            print("\n🧠 Cognate Analysis:")
            words_in_sentence = swedish_sentence.split()
            for word in words_in_sentence:
                clean_word = word.strip('.,').lower()
                cognate_type = self.get_cognate_type(clean_word)
                if cognate_type:
                    eng_trans = self.get_english_translation(clean_word)
                    if cognate_type == 'perfect':
                        print(f"   • {word}: {eng_trans} 🔹 PERFECT")
                    elif cognate_type == 'near':
                        print(f"   • {word}: {eng_trans} 🔸 NEAR")
                    elif cognate_type == 'false_friends':
                        print(f"   • {word}: {eng_trans} ⚠️ FALSE FRIEND")
            
            print("-" * 60)

    def get_english_translation(self, swedish_word):
        for category, words in self.cognates.items():
            if swedish_word in words:
                return words[swedish_word]['english']
        return swedish_word

    def show_cognate_rules(self):
        print("\n" + "="*60)
        print("🧠 SWEDISH-ENGLISH COGNATE PATTERNS")
        print("="*60)
        
        patterns = {
            "🔹 PERFECT FRIENDS": {
                "description": "Identical or nearly identical in both languages",
                "examples": ["arm → arm", "bank → bank", "film → film", "hotell → hotel"],
                "strategy": "Learn these first - instant vocabulary!"
            },
            "🔸 NEAR FRIENDS": {
                "description": "Similar with predictable spelling changes",
                "examples": ["äpple → apple", "bok → book", "fisk → fish", "hus → house"],
                "strategy": "Learn the patterns: -tion → -tion, -ell → -el, etc."
            },
            "⚠️ FALSE FRIENDS": {
                "description": "Look identical but have different meanings",
                "examples": ["bra → good (not bra)", "glass → ice cream (not glass)", "kock → cook (not cock)"],
                "strategy": "MEMORIZE these - they're the most important!"
            }
        }
        
        for pattern_type, info in patterns.items():
            print(f"\n{pattern_type}")
            print(f"📝 {info['description']}")
            print(f"🎯 Strategy: {info['strategy']}")
            print("   Examples:")
            for example in info['examples']:
                print(f"     • {example}")
        
        print("\n" + "="*60)
        print("💡 SWEDISH LEARNING TIPS:")
        print("   1. Swedish and English share 80% of vocabulary!")
        print("   2. Focus on pronunciation differences")
        print("   3. Learn the Swedish melody (pitch accent)")
        print("   4. Practice the vowels: å, ä, ö")
        print("   5. Use cognates to build quick fluency!")

    def cognate_phrases_explainer(self):
        print("\n" + "="*60)
        print("💬 SWEDISH COGNATE PHRASES EXPLAINER")
        print("="*60)
        
        cognate_phrases = {
            "Jag har ett problem": {
                "word_by_word": "I have a problem",
                "cognate_analysis": {
                    "problem": "problem (🔹 perfect)"
                },
                "full_translation": "I have a problem",
                "explanation": "🎉 Perfect cognate! 'Problem' works exactly the same in both languages!"
            },
            "Vi tittar på en film": {
                "word_by_word": "We look at a film", 
                "cognate_analysis": {
                    "film": "film (🔹 perfect)"
                },
                "full_translation": "We are watching a film",
                "explanation": "Another perfect cognate! 'Film' is identical in both languages."
            },
            "Det är bra väder": {
                "word_by_word": "It is good weather",
                "cognate_analysis": {
                    "bra": "good (⚠️ false friend - not 'bra')"
                },
                "full_translation": "The weather is good",
                "explanation": "🚨 FALSE FRIEND ALERT! 'Bra' means 'good' in Swedish, not underwear!"
            },
            "Jag älskar glass": {
                "word_by_word": "I love ice cream",
                "cognate_analysis": {
                    "glass": "ice cream (⚠️ false friend - not 'glass')"
                },
                "full_translation": "I love ice cream", 
                "explanation": "🍦 Another funny false friend! 'Glass' means ice cream in Swedish!"
            }
        }
        
        for swedish_phrase, analysis in cognate_phrases.items():
            print(f"\n🔹 Swedish: {swedish_phrase}")
            print(f"📖 Literal: {analysis['word_by_word']}")
            print("🧠 Cognate Breakdown:")
            for word, cognate_info in analysis['cognate_analysis'].items():
                print(f"   • {word}: {cognate_info}")
            print(f"🎯 Translation: {analysis['full_translation']}")
            print(f"💡 Insight: {analysis['explanation']}")
            print("-" * 60)

    def word_search(self):
        print("\n" + "="*60)
        print("🔍 SWEDISH WORD SEARCH")
        print("="*60)
        
        while True:
            search_term = input("\nEnter a Swedish word to search (or 'quit' to return): ").strip()
            
            if search_term.lower() == 'quit':
                break
                
            found = False
            for category, words in self.cognates.items():
                if search_term in words:
                    data = words[search_term]
                    category_display = {
                        'perfect': '🔹 PERFECT FRIEND',
                        'near': '🔸 NEAR FRIEND',
                        'false_friends': '⚠️ FALSE FRIEND'
                    }
                    
                    print(f"\n🎯 Found: {search_term}")
                    print(f"📋 Type: {category_display[category]}")
                    print(f"🇺🇸 English: {data['english']}")
                    print(f"📖 Meaning: {data['meaning']}")
                    print(f"💬 Example SV: {data['example']}")
                    print(f"💬 Example EN: {data['example_english']}")
                    
                    if category == 'perfect':
                        print("💡 This is a safe cognate to use!")
                    elif category == 'near':
                        print("💡 Be careful with the subtle differences!")
                    elif category == 'false_friends':
                        print("🚨 WARNING: This is a classic false friend!")
                    
                    found = True
                    break
            
            if not found:
                print(f"❌ '{search_term}' not found in the cognate database.")
                print("💡 Try another word or check the spelling.")

def main():
    tutor = CognaticSwedishTutor()
    
    while True:
        print("\n" + "="*60)
        print("🇸🇪 COGNATIC SWEDISH TUTOR 🇺🇸")
        print("="*60)
        print("1. 📚 Swedish Flashcards")
        print("2. 🎯 Swedish Quiz") 
        print("3. 🔨 Sentence Builder")
        print("4. 🧠 Cognate Patterns")
        print("5. 💬 Phrases Explainer")
        print("6. 🔍 Word Search")
        print("7. 🚪 Exit")
        
        choice = input("\nChoose an exercise (1-7): ").strip()
        
        if choice == '1':
            tutor.generate_flashcards()
        elif choice == '2':
            tutor.cognate_quiz()
        elif choice == '3':
            tutor.sentence_builder()
        elif choice == '4':
            tutor.show_cognate_rules()
        elif choice == '5':
            tutor.cognate_phrases_explainer()
        elif choice == '6':
            tutor.word_search()
        elif choice == '7':
            print("\nHej då! Lycka till med din svenska! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()