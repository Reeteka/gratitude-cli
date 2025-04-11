import random

def splash_screen():
    print(r"""
  ____                 _ _ _             _       
 |  __|___ ___ ___ ___| | | |_ _ _ ___ _| |___   
 |  __| .'|   | . |  _| | | . | | |  _| . | -_|  
 |____|__,|_|_|___|_| |_|_|___|___|_| |___|___|  
                                               
✨ Welcome to the Gratitude CLI Journal! ✨
""")


def show_tip_of_the_day():
    tips = [
        "💡 Even rough days have tiny good moments. Spot them 🌱",
        "💡 Write what you’re grateful for, not what you think you *should* be grateful for.",
        "💡 Repetition is fine — it helps reinforce what matters.",
        "💡 No entry is too small. ‘Nice weather’ counts!",
        "💡 Gratitude helps your brain rewire for joy. Keep going!"
    ]
    print("\n" + random.choice(tips) + "\n")
