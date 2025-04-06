import simpy
import random


# Importing the helper functions
from helpers import write_to_file
# Import the agent classes
from agents import DomainExpertA, DomainExpertB, StudentA, StudentB, ParentA, ParentB, Moderator



class TalkShowEnvironment:
    def __init__(self, file_path):
        self.env = simpy.Environment()
        self.conversation_history = []
        self.agents = []
        self.current_topic = None
        self.file_path = file_path

    def add_agent(self, agent):
        self.agents.append(agent)

    def add_to_history(self, speaker, message):
        self.conversation_history.append((speaker, message))
        if len(self.conversation_history) > 3:
            self.conversation_history.pop(0)

    def write_to_file(self, content):
        write_to_file(self.file_path, content)

    # def log_conversation(self):
    #     self.write_to_file("\n\nConversation History:")
    #     for speaker, message in self.conversation_history:
    #         self.write_to_file(f"{speaker}: {message}\n\n")


def discussion_controller(env):
    moderator = next(a for a in env.agents if isinstance(a, Moderator))
    active_participants = [a for a in env.agents if not isinstance(a, Moderator)]
    
    # Start the discussion
    env.current_topic = "Two Sides of Education: Improvement or Deterioration?"
    env.write_to_file(f"Topic: {env.current_topic}")
    env.write_to_file("Moderator's Initial Response:")
    moderator_response = moderator.generate_response(env.current_topic)
    env.write_to_file(f"Moderator: {moderator_response}")
    
    start_time = env.env.now
    
    while env.env.now < 50:
        # Randomly select next speaker
        next_speaker = random.choice(active_participants)
        
        # Get last relevant message as trigger
        if env.conversation_history:
            last_message = env.conversation_history[-1][1]
            question = f"Respond to: {last_message}"
        else:
            question = env.current_topic
        
        # Generate response and add to history
        response = next_speaker.generate_response(question)
        env.add_to_history(next_speaker.__class__.__name__, response)
        env.write_to_file(f"{next_speaker.__class__.__name__}: {response}")
        
        # Log conversation history
        # env.log_conversation()
        
        # Simulate delay between turns
        yield env.env.timeout(random.uniform(1.0, 3.0))
    
    # Moderator concludes the discussion
    env.write_to_file("Moderator's Conclusion:")
    conclusion_prompt = env.current_topic + " Conclusion"
    conclusion_response = moderator.generate_response(conclusion_prompt)
    env.write_to_file(f"Moderator: {conclusion_response}")


# Run the simulation
def run_simulation():
    env = TalkShowEnvironment("./talk_show_simulation.txt")
    
    # Initialize agents
    DomainExpertA_instance = DomainExpertA()
    DomainExpertB_instance = DomainExpertB()
    StudentA_instance = StudentA()
    StudentB_instance = StudentB()
    ParentA_instance = ParentA()
    ParentB_instance = ParentB()
    moderator = Moderator()
    
    # Add agents to the environment
    env.add_agent(DomainExpertA_instance)
    env.add_agent(DomainExpertB_instance)
    env.add_agent(StudentA_instance)
    env.add_agent(StudentB_instance)
    env.add_agent(ParentA_instance)
    env.add_agent(ParentB_instance)
    env.add_agent(moderator)
    
    # Start the discussion
    env.env.process(discussion_controller(env))
    env.env.run(until=40)  

# Execute the simulation
run_simulation()
