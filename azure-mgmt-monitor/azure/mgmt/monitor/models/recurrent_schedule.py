# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RecurrentSchedule(Model):
    """The scheduling constraints for when the profile begins.

    :param time_zone: the timezone for the hours of the profile. Some examples
     of valid timezones are: Dateline Standard Time, UTC-11, Hawaiian Standard
     Time, Alaskan Standard Time, Pacific Standard Time (Mexico), Pacific
     Standard Time, US Mountain Standard Time, Mountain Standard Time (Mexico),
     Mountain Standard Time, Central America Standard Time, Central Standard
     Time, Central Standard Time (Mexico), Canada Central Standard Time, SA
     Pacific Standard Time, Eastern Standard Time, US Eastern Standard Time,
     Venezuela Standard Time, Paraguay Standard Time, Atlantic Standard Time,
     Central Brazilian Standard Time, SA Western Standard Time, Pacific SA
     Standard Time, Newfoundland Standard Time, E. South America Standard Time,
     Argentina Standard Time, SA Eastern Standard Time, Greenland Standard
     Time, Montevideo Standard Time, Bahia Standard Time, UTC-02, Mid-Atlantic
     Standard Time, Azores Standard Time, Cape Verde Standard Time, Morocco
     Standard Time, UTC, GMT Standard Time, Greenwich Standard Time, W. Europe
     Standard Time, Central Europe Standard Time, Romance Standard Time,
     Central European Standard Time, W. Central Africa Standard Time, Namibia
     Standard Time, Jordan Standard Time, GTB Standard Time, Middle East
     Standard Time, Egypt Standard Time, Syria Standard Time, E. Europe
     Standard Time, South Africa Standard Time, FLE Standard Time, Turkey
     Standard Time, Israel Standard Time, Kaliningrad Standard Time, Libya
     Standard Time, Arabic Standard Time, Arab Standard Time, Belarus Standard
     Time, Russian Standard Time, E. Africa Standard Time, Iran Standard Time,
     Arabian Standard Time, Azerbaijan Standard Time, Russia Time Zone 3,
     Mauritius Standard Time, Georgian Standard Time, Caucasus Standard Time,
     Afghanistan Standard Time, West Asia Standard Time, Ekaterinburg Standard
     Time, Pakistan Standard Time, India Standard Time, Sri Lanka Standard
     Time, Nepal Standard Time, Central Asia Standard Time, Bangladesh Standard
     Time, N. Central Asia Standard Time, Myanmar Standard Time, SE Asia
     Standard Time, North Asia Standard Time, China Standard Time, North Asia
     East Standard Time, Singapore Standard Time, W. Australia Standard Time,
     Taipei Standard Time, Ulaanbaatar Standard Time, Tokyo Standard Time,
     Korea Standard Time, Yakutsk Standard Time, Cen. Australia Standard Time,
     AUS Central Standard Time, E. Australia Standard Time, AUS Eastern
     Standard Time, West Pacific Standard Time, Tasmania Standard Time, Magadan
     Standard Time, Vladivostok Standard Time, Russia Time Zone 10, Central
     Pacific Standard Time, Russia Time Zone 11, New Zealand Standard Time,
     UTC+12, Fiji Standard Time, Kamchatka Standard Time, Tonga Standard Time,
     Samoa Standard Time, Line Islands Standard Time
    :type time_zone: str
    :param days: the collection of days that the profile takes effect on.
     Possible values are Sunday through Saturday.
    :type days: list[str]
    :param hours: A collection of hours that the profile takes effect on.
     Values supported are 0 to 23 on the 24-hour clock (AM/PM times are not
     supported).
    :type hours: list[int]
    :param minutes: A collection of minutes at which the profile takes effect
     at.
    :type minutes: list[int]
    """

    _validation = {
        'time_zone': {'required': True},
        'days': {'required': True},
        'hours': {'required': True},
        'minutes': {'required': True},
    }

    _attribute_map = {
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'days': {'key': 'days', 'type': '[str]'},
        'hours': {'key': 'hours', 'type': '[int]'},
        'minutes': {'key': 'minutes', 'type': '[int]'},
    }

    def __init__(self, time_zone, days, hours, minutes):
        self.time_zone = time_zone
        self.days = days
        self.hours = hours
        self.minutes = minutes
