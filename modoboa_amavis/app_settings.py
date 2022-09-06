"""Custom settings."""

import collections

from django.utils.translation import ugettext_lazy as _

#Extension settings for api v2
GLOBAL_PARAMETERS_STRUCT = collections.OrderedDict([
    

    ("amavis_settings_sep", {
        "label": _("Amavis settings"),
        "params": collections.OrderedDict([
            ("localpart_is_case_sensitive", {
                "label": _("Local part is case sensitive"),
                "help_text": _("Value should match amavisd.conf variable "
                                "$localpart_is_case_sensitive")
            }),
            ("recipient_delimiter", {
                "label": _("Recipient delimiter"),
                "help_text": _(
                    "Value should match amavisd.conf variable %s"
                                % "$recipient_delimiter"
                ),
            })
        ])
    }),
    ("qsettings_sep", {
        "label": _("Quarantine settings"),
        "params": collections.OrderedDict([
            ("max_message_age", {
                "label": _("Maximum message age"),
                "help_text": _("Quarantine message maximum age (in days) before deletion")
            })
        ])
    }),
    ("spe1", {
        "label": _("Message releasing"),
        "params": collections.OrderedDict([
            ("released_msgs_cleanup", {
                "label": _("Remove released messages"),
                "help_text": _("Remove messages marked as released while cleaning up "
            "the database")
            }),
            ("am_pdp_mode", {
                "label": _("Amavis connection mode"),
                "help_text": _("Mode used to access the PDP server")
            }),
            ("am_pdp_host", {
                "label": _("PDP server address"),
                "display": "am_pdp_mode=inet",
                "help_text": _("PDP server address (if inet mode)")
            }),
            ("am_pdp_port", {
                "label": _("PDP server port"),
                "display": "am_pdp_mode=inet",
                "help_text": _("PDP server port (if inet mode)")
            }),
            ("am_pdp_socket", {
                "label": _("PDP server socket"),
                "display": "am_pdp_mode=unix",
                "help_text": _("Path to the PDP server socket (if unix mode)")
            }),
            ("user_can_release", {
                "label": _("Allow direct release"),
                "help_text": _("Allow users to directly release their message")
            }),
            ("self_service", {
                "label": _("Enable self-service mode"),
                "help_text": _("Activate the 'self-service' mode")
            }),
            ("notification_sender", {
                "label": _("Notification sender"),
                "help_text": _("The e-mail address used to send notitications")
            })     
        ])
    }),
    ("lsep", {
        "label": _("Manual lerning"),
        "params": collections.OrderedDict([
            ("manual_learning", {
                "label": _("Enable manual learning"),
                "help_text": _("Allow super administrators to manually train Spamassassin")
            }),
            ("sa_is_local", {
                "label": _("Is Spamassassin local?"),
                "display":"manual_learning=True",
                "help_text": _("Tell if Spamassassin is running on the same server than modoboa")
            }),
            ("default_user", {
                "label": _("Default user"),
                "display":"manual_learning=True",
                "help_text": _( "Name of the user owning the default bayesian database")
            }),
            ("spamd_address", {
                "label": _("Spamd address"),
                "display":"sa_is_local=False",
                "help_text": _("The IP address where spamd can be reached")
            }),
            ("spamd_port", {
                "label": _("Spamd port"),
                "display":"sa_is_local=False",
                "help_text": _("The TCP port spamd is listening on")
            }),
            ("domain_level_learning", {
                "label": _("Enable per-domain manual learning"),
                "display":"manual_learning=True",
                "help_text": _("Allow domain administrators to train Spamassassin "
                                "(within dedicated per-domain databases)")
            }),
            ("user_level_learning", {
                "label": _("Enable per-user manual learning"),
                "display":"manual_learning=True",
                "help_text": _("Allow simple users to personally train Spamassassin "
                                "(within a dedicated database)")
            })
        ])
    })
])
