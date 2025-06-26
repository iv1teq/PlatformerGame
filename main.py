from modules import run

def main():
    try:
        run()
    except Exception as error:
        print(f"Помилка під час запуску проекту: {error}")
        
if __name__ == "__main__": 
    main()
