"""
@author: v_shxliu
"""
from common.util import save_file
from src.create_ics import CreatIcs

if __name__ == '__main__':
    data_dict_tuple = ({"date": "20190429",
                        "title": "大连一方 VS 北京中赫国安",
                        "start_time": "193000"
                        },
                       {"date": "20190425",
                        "title": "大连一方 VS 重庆思斯威",
                        "start_time": "153000"
                        })
    calendar_title = input('Inputtes Calendar Title:')
    ci = CreatIcs(calendar_title)
    ics_info = ci.process(data_dict_tuple)
    save_file(ics_info)
