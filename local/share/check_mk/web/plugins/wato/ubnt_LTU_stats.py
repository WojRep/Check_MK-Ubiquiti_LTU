#!/usr/bin/env python3

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
                        Float(title=_('Warning at'),unit='Mb/s',default_value='80.0'),
                        Float(title=_('Critical at'),unit='Mb/s',default_value='100.0'),
                        ] ) ),
                 ('rxpps', Tuple(
                     title=_('LTU Rx PPS'),
                     elements = [
                        Float(title=_('Warning at'),unit='pps',default_value='8000'),
                        Float(title=_('Critical at'),unit='pps',default_value='10000'),
                        ] ) ),
                 ('txbyte', Tuple(
                     title=_('LTU Tx Mb/s'),
                     elements = [
                        Float(title=_('Warning at'),unit='Mb/s',default_value='80.0'),
                        Float(title=_('Critical at'),unit='Mb/s',default_value='100.0'),
                        ] ) ),
                 ('txpps', Tuple(
                     title=_('LTU Tx PPS'),
                     elements = [
                        Float(title=_('Warning at'),unit='pps',default_value='8000'),
                        Float(title=_('Critical at'),unit='pps',default_value='10000'),
                        ] ) ),
           ],  
         ),
        ),
        TextAscii(
            title = _("UBNT LTU Network Stats"),
            
            ),
       match_type = 'dict',
)
