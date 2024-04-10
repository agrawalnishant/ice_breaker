from dotenv import load_dotenv
import os
if __name__ == '__main__':
    load_dotenv()
    print(os.environ['SOME_KEY'])
    print('Ice Breaker')