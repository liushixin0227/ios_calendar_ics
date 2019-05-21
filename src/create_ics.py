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
                                 "VERSION:2.0\n" \
                                 "X-WR-CALNAME:{title_name}\n" \
                                 "X-APPLE-CALENDAR-COLOR:#1BADF8\n" \
                                 "X-WR-CALDESC:\n" \
                                 "BEGIN:VTIMEZONE\n" \
                                 "TZID:Asia/Shanghai\n" \
                                 "X-LIC-LOCATION:Asia/Shanghai\n" \
                                 "BEGIN:STANDARD\n" \
                                 "DTSTART:19010101T000000\n" \
                                 "RDATE:19010101T000000\n" \
                                 "TZNAME:CST\n" \
                                 "TZOFFSETFROM:+080543\n" \
                                 "TZOFFSETTO:+0800\n" \
                                 "END:STANDARD\n" \
                                 "BEGIN:DAYLIGHT\n" \
                                 "DTSTART:19400601T000000\n" \
                                 "RDATE:19400601T000000\n" \
                                 "RDATE:19410315T000000\n" \
                                 "RDATE:19420131T000000\n" \
                                 "RDATE:19460515T000000\n" \
                                 "RDATE:19470415T000000\n" \
                                 "RDATE:19860504T020000\n" \
                                 "TZNAME:CDT\n" \
                                 "TZOFFSETFROM:+0800\n" \
                                 "TZOFFSETTO:+0900\n" \
                                 "END:DAYLIGHT\n" \
                                 "BEGIN:STANDARD\n" \
                                 "DTSTART:19401012T235959\n" \
                                 "RDATE:19401012T235959\n" \
                                 "RDATE:19411101T235959\n" \
                                 "RDATE:19450901T235959\n" \
                                 "RDATE:19460930T235959\n" \
                                 "RDATE:19471031T235959\n" \
                                 "RDATE:19480930T235959\n" \
                                 "RDATE:19490528T000000\n" \
                                 "TZNAME:CST\n" \
                                 "TZOFFSETFROM:+0900\n" \
                                 "TZOFFSETTO:+0800\n" \
                                 "END:STANDARD\n" \
                                 "BEGIN:DAYLIGHT\n" \
                                 "DTSTART:19480501T000000\n" \
                                 "RRULE:FREQ=YEARLY;UNTIL=19490430T160000Z;BYMONTH=5\n" \
                                 "TZNAME:CDT\n" \
                                 "TZOFFSETFROM:+0800\n" \
                                 "TZOFFSETTO:+0900\n" \
                                 "END:DAYLIGHT\n" \
                                 "BEGIN:STANDARD\n" \
                                 "DTSTART:19860914T020000\n" \
                                 "RRULE:FREQ=YEARLY;UNTIL=19910914T170000Z;BYMONTH=9;BYMONTHDAY=11,12,13,14\n " \
                                 ",15,16,17;BYDAY=SU\n" \
                                 "TZNAME:CST\n" \
                                 "TZOFFSETFROM:+0900\n" \
                                 "TZOFFSETTO:+0800\n" \
                                 "END:STANDARD\n" \
                                 "BEGIN:DAYLIGHT\n" \
                                 "DTSTART:19870412T020000\n" \
                                 "RRULE:FREQ=YEARLY;UNTIL=19910413T180000Z;BYMONTH=4;BYMONTHDAY=11,12,13,14\n " \
                                 ",15,16,17;BYDAY=SU\n" \
                                 "TZNAME:CDT\n" \
                                 "TZOFFSETFROM:+0800\n" \
                                 "TZOFFSETTO:+0900\n" \
                                 "END:DAYLIGHT\n" \
                                 "END:VTIMEZONE\n" \
                                 "{eventinfo}\n" \
                                 "END:VCALENDAR\n"

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
            # todo:增加观赛地址和观赛链接:
            # eventString += "\nLOCATION:" + {Address}
            # eventString += "\nURL;VALUE=URI:" + {URL}
            eventString += "\nDESCRIPTION:事件提醒\nACTION:DISPLAY\nEND:VALARM\nEND:VEVENT"

        ics_info = self.ics_header_string.format(title_name=self.title_name, eventinfo=eventString)
        return ics_info
