
from helpers import read_persona_prompts, query_gpt4

class DomainExpertA:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/domain_expert_a.txt")
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)

class DomainExpertB:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/domain_expert_b.txt")
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)

class StudentA:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/student_a.txt")
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)

class StudentB:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/student_b.txt")
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)

class ParentA:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/parent_a.txt")
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)

class ParentB:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/parent_b.txt")
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)

class Moderator:
    def generate_response(self, question):
        persona_prompt = read_persona_prompts("persona/moderator.txt")
        print("Moderator persona prompt:", persona_prompt)
        print("Question:", question)
        prompt = persona_prompt + f"\nQuestion: {question}\nAnswer:"
        return query_gpt4(persona_prompt, prompt)
