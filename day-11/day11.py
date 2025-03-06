import re

emoji_mood = {
    "😊": "Happy Mood!", "😃": "Happy Mood!", "😍": "Happy Mood!",
    "😢": "Sad Mood!", "😭": "Sad Mood!", "🙁": "Sad Mood!",
    "😡": "Angry Mood!", "🤬": "Angry Mood!", "😠": "Angry Mood!",
    "😐": "Neutral Mood!", "😶": "Neutral Mood!", "🤔": "Neutral Mood!"
}

def detect_mood(text):
    emoji_pattern = re.findall(r'[\U0001F600-\U0001F64F]', text) 

    if not emoji_pattern:
        return "No emoji found, can't detect mood! 🤷‍♂"

    for emoji in emoji_pattern:
        if emoji in emoji_mood:
            return f"Detected Mood: {emoji_mood[emoji]} {emoji}"
    
    return "Emoji found, but mood not recognized! 🤔"

user_text = input("Enter your message: ")
print(detect_mood(user_text))