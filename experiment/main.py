from .. import constant

def hello(folder_name):
    print(f"Hello from {folder_name} folder")

if __name__ == "__main__":
    for i in range(constant.COUNT):
        hello()
