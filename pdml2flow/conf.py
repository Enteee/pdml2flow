#!/usr/bin/env python3
# vim: set fenc=utf8 ts=4 sw=4 et :

class Conf():

    @staticmethod
    def get_real_paths(paths, nestchar):
        return [ path.split(nestchar) + ['raw'] for path in paths ]

    FLOW_DEF_NESTCHAR = '.'
    FLOW_DEF_STR = [
                'vlan{}id'.format(FLOW_DEF_NESTCHAR),
                'ip{}src'.format(FLOW_DEF_NESTCHAR),
                'ip{}dst'.format(FLOW_DEF_NESTCHAR),
                'ipv6{}src'.format(FLOW_DEF_NESTCHAR),
                'ipv6{}dst'.format(FLOW_DEF_NESTCHAR),
                'udp{}stream'.format(FLOW_DEF_NESTCHAR),
                'tcp{}stream'.format(FLOW_DEF_NESTCHAR),
    ]
    FLOW_DEF = get_real_paths.__func__(FLOW_DEF_STR, FLOW_DEF_NESTCHAR)
    DATA_MAXLEN = 200
    DATA_TOO_LONG = 'Data too long'
    PDML_NESTCHAR = '.'
    FLOW_BUFFER_TIME = 180
    EXTRACT_SHOW = False
    STANDALONE = False
    XML_OUTPUT = False
    COMPRESS_DATA = False
    FRAMES_ARRAY = False
    DEBUG = False
    METADATA = False

    """
    Applies a configuration to the global config object
    """
    @staticmethod
    def set(conf):
        for name, value in conf.items():
            setattr(Conf, name.upper(), value)
