import psutil

def get_ram_info():
    mem = psutil.virtual_memory()
    
    print("=== RAM Information ===")
    print(f"Total RAM     : {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM : {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM      : {mem.used / (1024 ** 3):.2f} GB")
    print(f"Free RAM      : {mem.free / (1024 ** 3):.2f} GB")
    print(f"RAM Usage     : {mem.percent} %")

get_ram_info()
