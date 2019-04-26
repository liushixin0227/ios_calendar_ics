# coding:utf8

"""
@author: v_shxliu
"""
import uuid
from common import util


class CreatIcs(object):
    def __init__(self, input_title_name):
        # ICS file title
        self.title_name = input_title_name
        # definition ICS file header
        self.ics_header_string = "BEGIN:VCALENDAR\n" \
                                 "METHOD:PUBLISH\n" \
                                 "VERSION:2.0\n" \
                                 "X-WR-CALNAME:{title_name}\n" \
                                 "PRODID:-//Apple Inc.//Mac OS X 10.12//EN\n" \
                                 "X-APPLE-CALENDAR-COLOR:#FC4208\n" \
                                 "X-WR-TIMEZONE:Asia/Shanghai\n" \
                                 "CALSCALE:GREGORIAN\n" \
                                 "BEGIN:VTIMEZONE\n" \
                                 "TZID:Asia/Shanghai\n" \
                                 "BEGIN:STANDARD\n" \
                                 "TZOFFSETFROM:+0900\n" \
                                 "RRULE:FREQ=YEARLY;UNTIL=19910914T150000Z;BYMONTH=9;BYDAY=3SU\n" \
                                 "DTSTART:19890917T000000\n" \
                                 "TZNAME:GMT+8\n" \
                                 "TZOFFSETTO:+0800\n" \
                                 "END:STANDARD\n" \
                                 "BEGIN:DAYLIGHT\n" \
                                 "TZOFFSETFROM:+0800\n" \
                                 "DTSTART:19910414T000000\n" \
                                 "TZNAME:GMT+8\n" \
                                 "TZOFFSETTO:+0900\n" \
                                 "RDATE:19910414T000000\n" \
                                 "END:DAYLIGHT\n" \
                                 "END:VTIMEZONE\n" \
                                 "{eventinfo}\n" \
                                 "END:VCALENDAR"

    def process(self, data_dict_list):
        """

        :param data_dict_list: 需要格式化的数据,数据格式为字典元组,例:
        ({"date":"",
        "title":"",
        "start_time":"",
        "end_time:""
        },)
        :return: None
        """
        ics_info = self.format_ics_info(data_dict_list)
        print(ics_info)
        return ics_info

    def format_ics_info(self, data_dict_list):
        """

        :param data_dict_list: 从上层process透传的待处理数据
        :return: ics_info 返回标准ics格式的字符串
        """
        eventString = ""
        create_time = util.standard_xml_time()
        for data_dict in data_dict_list:
            eventString += "BEGIN:VEVENT\nCREATED:" + create_time
            eventString += "\nUID:" + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'VEVENT'))
            # eventString += "\nDTEND;TZID=Asia/Shanghai:" + data_dict['date'] + "T" + data_dict['end_time']
            eventString += "00\nTRANSP:OPAQUE\nX-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC\nSUMMARY:" + data_dict[
                'title']
            eventString += "\nDTSTART;TZID=Asia/Shanghai:" + data_dict['date'] + "T" + data_dict['start_time'] + "00"
            eventString += "\nDTSTAMP:" + create_time
            eventString += "\nSEQUENCE:0\nBEGIN:VALARM\nX-WR-ALARMUID:" + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'ALARM'))
            eventString += "\nUID:" + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'VALARM'))
            eventString += "\nTRIGGER:" + "-P1D"
            #todo:增加观赛地址和观赛链接:
            # eventString += "\nLOCATION:" + {Address}
            # eventString += "\nURL;VALUE=URI:" + {URL}
            eventString += "\nDESCRIPTION:事件提醒\nACTION:DISPLAY\nEND:VALARM\nEND:VEVENT"

        ics_info = self.ics_header_string.format(title_name=self.title_name, eventinfo=eventString)
        return ics_info
