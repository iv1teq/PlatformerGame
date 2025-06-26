import os


def create_path(path: str) -> str:
    try:
        path_elements_list = path.split("/")

        base_path = os.path.abspath(os.path.join(__file__, "..", ".."))
        
        for path_element in path_elements_list:
            base_path = os.path.join(base_path, path_element)
        
        path_file = os.path.abspath(base_path)

        return path_file
    except Exception as error:
        print(f"Помилка під час створення абсолютного шляху до зображення: {error}")