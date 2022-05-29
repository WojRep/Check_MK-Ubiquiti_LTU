#!/usr/bin/python

register_check_parameters(
    subgroup_networking,
        'ubnt_LTU_stats',
        _('UBNT LTU Network Stats'),
        Transform(
         Dictionary(
            title = _('UBNT LTU Network Stats Params'),
            elements = [
                 ('rxbyte', Tuple(
                     title=_('LTU Rx Mb/s'),
                     elements = [
                        Float(title=_('Warning at'),unit='Mb/s',default_value='80.0',allow_empty = False),
                        Float(title=_('Critical at'),unit='Mb/s',default_value='100.0',allow_empty = False),
                        ] ) ),
                 ('rxpps', Tuple(
                     title=_('LTU Rx PPS'),
                     elements = [
                        Float(title=_('Warning at'),unit='pps',default_value='8000',allow_empty = False),
                        Float(title=_('Critical at'),unit='pps',default_value='10000',allow_empty = False),
                        ] ) ),
                 ('txbyte', Tuple(
                     title=_('LTU Tx Mb/s'),
                     elements = [
                        Float(title=_('Warning at'),unit='Mb/s',default_value='80.0',allow_empty = False),
                        Float(title=_('Critical at'),unit='Mb/s',default_value='100.0',allow_empty = False),
                        ] ) ),
                 ('txpps', Tuple(
                     title=_('LTU Tx PPS'),
                     elements = [
                        Float(title=_('Warning at'),unit='pps',default_value='8000',allow_empty = False),
                        Float(title=_('Critical at'),unit='pps',default_value='10000',allow_empty = False),
                        ] ) ),
           ], allow_empty = False, 
         ),
        ),
        TextAscii(
            title = _("UBNT LTU Network Stats"),
            allow_empty = False,
            ),
       match_type = 'dict',
)
