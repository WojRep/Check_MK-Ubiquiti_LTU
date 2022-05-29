#!/usr/bin/env python3

register_check_parameters(
    subgroup_networking,
        'ubnt_LTU_signal',
        _('UBNT LTU signal'),
        Transform(
         Dictionary(
            title = _('UBNT LTU Signal Params'),
            elements = [
                 ('rx', Tuple(
                     title=_('LTU Rx Signal'),
                     elements = [
                        Float(title=_('Warning at'),unit='dBm',default_value='-68'),
                        Float(title=_('Critical at'),unit='dBm',default_value='-76'),
                        ] ) ),
                 ('tx', Tuple(
                     title=_('LTU Tx Signal'),
                     elements = [
                        Float(title=_('Warning at'),unit='dBm',default_value='-68'),
                        Float(title=_('Critical at'),unit='dBm',default_value='-76'),
                        ] ) ),
                ('ondisconnect', ListChoice(
                    title=_('Notify disconnect LTU Station'),
                    choices = [
                        ( False, _("No")),
                        ( True, _("Yes")),
                    ],
                    default_value = False,
                    ) ),
               ('username', TextAscii(
                   title=_("Username"),
                   default_value = "ubnt",
                   
                   ) ),
               ('passwd', Password(
                   title=_("Password"),
                   
                   ) ),
                ('sshport', Integer(
                    title=_("SSH port"),
                    default_value = 22,
                    
                    ) ),
                ('httpsport', Integer(
                    title=_("HTTPS port"),
                    default_value = 443,
                    
                    ) ),
           ],  
         ),
        ),
        TextAscii(
            title = _("UBNT LTU Signal"),
            
            ),
       match_type = 'dict',
)
