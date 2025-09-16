class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact
    
    def introduce(self):
        print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
    
    def show_stack(self):
        print(f"{self.name}'s Tech Stack:")
        for i, tech in enumerate(self.tech_stack, 1):
            print(f"{i}. {tech}")
    
    def github_link(self):
        return f"https://github.com/{self.github_username}"

my_profile = Profile(
    name="Okello Emmanuel",
    favorite_language="Python",
    hobby="coding and hiking",
    tech_stack=["Python", "Django", "Flask", "Git", "JavaScript", "React", "PostgreSQL"],
    github_username="mremma256",
    fun_fact="I can solve a Rubik's cube in under 2 minutes!"
)

print("*** Introduction ***")
my_profile.introduce()

print("\n*** Tech Stack ***")
my_profile.show_stack()

print("\n*** GitHub Link ***")
print(f"GitHub: {my_profile.github_link()}")

print("\n*** Fun Fact ***")
print(f"Fun fact: {my_profile.fun_fact}")