import time
from selenium import webdriver
import cookies

quotes = [
    "Supervised learning refers to a type of machine learning where the algorithm is trained on a labeled dataset, with the goal of predicting an output for new, unseen data. Unsupervised learning, on the other hand, refers to a type of machine learning where the algorithm is trained on an unlabeled dataset, with the goal of finding patterns and structures in the data.",
    "Neural networks are often used in machine learning due to their ability to learn complex patterns and relationships in the data. Some advantages of using neural networks include their ability to handle large amounts of data and their ability to perform well on complex tasks such as image recognition or natural language processing. However, some disadvantages of using neural networks include their computational complexity, their tendency to overfit the data, and their lack of interpretability.",
    "Bias and variance are common sources of error in machine learning models. Bias refers to the error that occurs when a model is too simple and unable to capture the true relationship between the input and output. Variance refers to the error that occurs when a model is too complex and overfits the training data. To avoid bias and variance, techniques such as cross-validation, regularization, and ensembling can be used.",
    "Natural language processing (NLP) has numerous applications, including language translation, sentiment analysis, text classification, chatbots, and more. Some challenges of NLP include the ambiguity of language, the complexity of natural language, and the need for large amounts of annotated data.",
    "Ethical and social implications of artificial intelligence (AI) include issues such as bias, privacy, safety, and job displacement. For example, AI systems may exhibit biases based on the data they were trained on, which can result in discrimination against certain groups. Privacy concerns arise when AI systems are used to collect and analyze personal data. Safety concerns arise when AI systems are used in critical applications such as self-driving cars or medical diagnosis.",
    "Fairness, transparency, and accountability can be ensured in AI systems by using techniques such as algorithmic auditing, explainability, and interpretability. Algorithmic auditing involves regularly monitoring and testing the AI system for bias and other ethical issues. Explainability and interpretability refer to the ability to understand how the AI system makes its decisions and to ensure that these decisions are consistent with ethical and legal standards.",
    "Reinforcement learning is a type of machine learning where the algorithm learns by receiving feedback from its environment in the form of rewards or penalties. Benefits of reinforcement learning include its ability to learn complex behaviors and its ability to adapt to changing environments. Drawbacks include the need for a large amount of data and the potential for the agent to become stuck in a suboptimal policy.",
    "Deep learning is often used in image, video, and audio processing due to its ability to learn complex features in the data. Convolutional neural networks (CNNs) are commonly used in image processing, while recurrent neural networks (RNNs) are used in speech recognition and language modeling. Preprocessing techniques such as data augmentation and normalization can also improve the performance of deep learning models.",
]

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
