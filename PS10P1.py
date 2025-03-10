import random
import time

class MentalHealthAI:
    """
    A prototype mental health AI service.
    This is a simplified example and should not be used for actual mental health diagnosis or treatment.
    """

    def __init__(self):
        self.user_name = None
        self.mood_history = {}  # Store mood scores over time.
        self.topics = {
            "stress": ["What's causing you stress?", "How are you coping with stress?", "Let's explore some stress-reduction techniques."],
            "anxiety": ["What are you feeling anxious about?", "How intense is your anxiety on a scale of 1-10?", "Have you tried any grounding exercises?"],
            "low mood": ["How long have you been feeling this way?", "What activities usually lift your mood?", "Let's try to identify some positive aspects of your day."],
            "general": ["How are you feeling today?", "What's on your mind?", "Is there anything you'd like to talk about?"]
        }
        self.responses = {
            "positive": ["That's great to hear!", "Wonderful!", "Keep up the good work!"],
            "neutral": ["I understand.", "Okay.", "I'm listening."],
            "negative": ["I'm sorry to hear that.", "That sounds difficult.", "It's okay to feel this way."]
        }
        self.affirmations = [
            "You are strong.",
            "You are capable.",
            "You are worthy of happiness.",
            "Your feelings are valid.",
            "You are not alone."
        ]

    def greet(self):
        self.user_name = input("Hello! What's your name? ")
        print(f"Hi, {self.user_name}! How can I help you today?")

    def get_mood(self):
        while True:
            try:
                mood = int(input("On a scale of 1-10 (1 being very low, 10 being very high), how would you rate your mood? "))
                if 1 <= mood <= 10:
                    self.mood_history[time.time()] = mood
                    return mood
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_topic(self):
        print("What would you like to talk about? (stress, anxiety, low mood, general)")
        while True:
            topic = input("Enter topic: ").lower()
            if topic in self.topics:
                return topic
            else:
                print("Invalid topic. Please choose from stress, anxiety, low mood, or general.")

    def generate_response(self, topic):
        questions = self.topics[topic]
        for question in questions:
            print(question)
            input("> ")  # User input
            print(random.choice(self.responses["neutral"])) #Provide a basic response.

    def provide_affirmation(self):
        print(random.choice(self.affirmations))

    def run(self):
        self.greet()
        mood = self.get_mood()
        if mood < 4:
            print(random.choice(self.responses["negative"]))
        elif mood > 7:
            print(random.choice(self.responses["positive"]))
        else:
            print(random.choice(self.responses["neutral"]))

        topic = self.choose_topic()
        self.generate_response(topic)
        self.provide_affirmation()
        print("Thank you for talking. Remember, I'm here if you need me.")

if __name__ == "__main__":
    ai = MentalHealthAI()
    ai.run()
