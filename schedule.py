from datetime import datetime

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), "w") as myfile:
    myfile.write(f"Hi there! {datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}")
