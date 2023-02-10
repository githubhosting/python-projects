import time
from selenium import webdriver
import cookies

quotes = [
    "AI beats human champions: AI has made remarkable progress in recent years, with algorithms beating human champions at complex games like chess and Go. This achievement is a testament to the ability of AI systems to analyze and understand complex patterns and make decisions based on that analysis. It has also provided new insights into the limits of human intelligence and has opened up new areas of research in the field of AI. #AIChallenger #IntelligentMachines #GameChanger",
    "Generative art and media: Deep learning algorithms have been used to generate realistic images and videos, as well as to generate new forms of music and art. These generative models use deep neural networks to learn patterns from existing data, and then use that knowledge to generate new, original content. The results are often stunning and have the potential to revolutionize the way we create and experience art and media. #GenerativeArt #ArtificialCreativity #DigitalRevolution",
    "GPT-3: OpenAI's GPT-3 is the largest AI language model to date, and has been trained on a massive amount of text data. This model can generate coherent and convincing text on a wide range of topics, from answering questions to writing articles and even coding. GPT-3 represents a major breakthrough in AI language generation, and has the potential to change the way we interact with technology and information. #GPT3 #AIlanguage #NLPrevolution",
    "AI in space exploration: AI has been used to discover new planets and to identify possible signs of life on other worlds. This has opened up new possibilities for space exploration and scientific discovery, as AI algorithms can analyze vast amounts of data much faster and more effectively than humans. AI is helping us to better understand the universe and our place in it. #AIspace #ExtraterrestrialLife #CosmicDiscovery",
    "Emotion recognition: Some AI systems have been developed that can understand and respond to human emotions. These systems use computer vision and machine learning algorithms to analyze facial expressions, voice tone, and other cues to identify and respond to human emotions. These systems have the potential to revolutionize areas like customer service, marketing, and mental health, by providing more personalized and human-like interactions. #EmotionDetection #HumanEmotionAnalysis",
    "AI and ML are transforming industries such as healthcare, finance, and e-commerce. In healthcare, AI is used for disease diagnosis, treatment options, and outbreak prediction. In finance, ML is used for fraud detection, portfolio optimization, and risk management. E-commerce companies are using AI and ML to personalize shopping experiences and product recommendations. #AIMLImpact #Healthcare #Finance #Ecommerce #BusinessTransformation",
    "Smart technologies: AI and computer vision technologies are driving the development of smart technologies like self-driving cars and smart homes. Self-driving cars use computer vision and deep learning algorithms to interpret and respond to their surroundings, while smart homes use AI to automate and control various appliances and systems. #SmartTech #SelfDrivingCars #SmartHomes #ComputerVision",
    "AI ethics: As AI becomes more widespread, there are growing concerns about its impact on society, including the potential for biased algorithms that unfairly target certain groups. To address these concerns, researchers and industry leaders are exploring new approaches to AI ethics, including the development of fair, transparent, and accountable algorithms. #AIethics #BiasInAlgorithms #SocietalImpact #FairAI",
    "Quantum computing: Quantum computing has the potential to revolutionize AI and machine learning by providing much more powerful processing capabilities. Quantum algorithms can perform certain types of computations much faster than classical computers, enabling more advanced AI and ML applications. #QuantumComputing #RevolutionizeAI #MorePowerfulProcessing",
    "AI-powered virtual assistants: AI-powered virtual assistants like ChatGPT are becoming increasingly sophisticated and widely used. These systems leverage large language models trained on vast amounts of text data to understand and respond to user requests in natural language. As AI-powered virtual assistants continue to improve, they are likely to play an increasingly important role in our daily lives. #AIPoweredVirtualAssistants #ChatGPT #LanguageModels #DailyLives",
    "Generative models: Generative models are a subset of AI and machine learning that are designed to generate new data, such as images, music, and text, based on patterns learned from existing data. These models have the potential to revolutionize creative industries and enable the development of new forms of art and media. #GenerativeModels #NewData #CreativeIndustries #ArtAndMedia",
    "Reinforcement learning: Reinforcement learning is a type of machine learning that trains AI systems to make decisions by learning from rewards and punishments. Reinforcement learning is being applied in areas like gaming, robotics, and autonomous systems to improve decision-making and control. #ReinforcementLearning #DecisionMaking #Gaming #Robotic",
    "Natural language processing: Natural language processing (NLP) is a subfield of AI and machine learning that focuses on teaching computers to understand and respond to human language. NLP has numerous applications in areas like chatbots, machine translation, and sentiment analysis, and is playing an increasingly important role in areas like customer service and marketing. #NLP #UnderstandHumanLanguage #Chatbots #MachineTranslation",
    "Transfer learning: Transfer learning is a technique in machine learning where a model trained on one task can be adapted and fine-tuned for another task, using the knowledge gained from the first task. Transfer learning enables the development of more efficient and effective AI systems and has numerous applications in areas like computer vision and natural language processing. #TransferLearning #MoreEfficientAI #ComputerVision #NLP",
    "Explainable AI: Explainable AI (XAI) is an emerging field of AI that aims to make AI systems more transparent and understandable so that their decisions and predictions can be explained and justified. XAI is becoming increasingly important as AI systems are being used in sensitive and high-stakes applications, such as healthcare and finance. #ExplainableAI #TransparentAI #UnderstandableAI #HighStakesApplications."]

URL = "https://www.kooapp.com"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)
cookies.load(driver, URL)
print("Logged in")

for quote in quotes:
    print("Posting: ", end="")
    driver.get(f"{URL}/create")
    text_input = driver.find_element_by_id("koo-create-editable-en")
    for ch in quote:
        text_input.send_keys(ch)
        print(ch, end="")
        time.sleep(.1)
    post_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div/div[1]/div[2]/button')
    post_btn.click()
    print("Posted")
    print("Waiting for 5sec")
    time.sleep(5)
