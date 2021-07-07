import os

try:
    from fdfs_client.client import *
    from fdfs_client.exceptions import *
except ImportError:
    import_path = os.path.abspath('../')
    sys.path.append(import_path)
    from fdfs_client.client import *
    from fdfs_client.exceptions import *

root_path = 'D:\\dennis\\work\\github\\python\\fastDFS'

def main():
    conf_file = '%s/client.conf'%root_path
    print(conf_file)
    tracker_path = get_tracker_conf(conf_file)
    client = Fdfs_client(tracker_path)
    file_name = '%s/onepiece.jpg'%root_path
    print(file_name)
    ret = client.upload_by_filename(file_name)
    print(ret)

if __name__ == "__main__":
    print("main enter.")
    main()
    print("main exit.")