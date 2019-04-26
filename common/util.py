"""
@author: v_shxliu
"""
import datetime
import uuid


def standard_xml_time():
    xml_time = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')
    return xml_time


def save_file(info):
    file_name = input('Saving file...\nInput File Name:')
    with open(r"../src/{}".format(file_name), 'w') as fp:
        fp.write(info)
        fp.close()


if __name__ == '__main__':
    print(standard_xml_time())
    print(uuid.uuid1())
    print(uuid.uuid1())
    print(uuid.uuid1())
