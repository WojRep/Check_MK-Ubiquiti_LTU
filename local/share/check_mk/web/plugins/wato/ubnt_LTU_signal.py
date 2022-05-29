#!/usr/bin/python

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
                        Float(title=_('Warning at'),unit='dBm',default_value='-68',allow_empty = False),
                        Float(title=_('Critical at'),unit='dBm',default_value='-76',allow_empty = False),
                        ] ) ),
                 ('tx', Tuple(
                     title=_('LTU Tx Signal'),
                     elements = [
                        Float(title=_('Warning at'),unit='dBm',default_value='-68',allow_empty = False),
                        Float(title=_('Critical at'),unit='dBm',default_value='-76',allow_empty = False),
                        ] ) ),
                ('ondisconnect', ListChoice(
                    title=_('Notify disconnect LTU Station'),
                    choices = [
                        ( False, _("No")),
                        ( True, _("Yes")),
                    ],
                    default = False,
                    ) ),
               ('username', TextAscii(
                   title=_("Username"),
                   default_value = "ubnt",
                   allow_empty = False,
                   ) ),
               ('passwd', Password(
                   title=_("Password"),
                   allow_empty = False,
                   ) ),
                ('sshport', Integer(
                    title=_("SSH port"),
                    default_value = 22,
                    allow_empty = False,
                    ) ),
           ], allow_empty = False, 
         ),
        ),
        TextAscii(
            title = _("UBNT LTU Signal"),
            allow_empty = False,
            ),
       match_type = 'dict',
)
