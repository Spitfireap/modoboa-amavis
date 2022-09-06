"""Limits serializers for API v2."""

from rest_framework import serializers


class AmavisGlobalParameters(serializers.Serializer):
    """A serializer for global parameters."""

    #Amavis settings
    localpart_is_case_sensitive = serializers.BooleanField(default=False)
    recipient_delimiter = serializers.CharField(default="", required=False)

    #Quarantine setting
    max_message_age = serializers.IntegerField(default=14)
    
    #Message releasing
    released_msgs_cleanup = serializers.BooleanField(default=False)
    am_pdp_mode = serializers.ChoiceField(default="unix", 
                                        choices=["inet", "unix"])
    am_pdp_host = serializers.CharField(default="localhost")
    am_pdp_port = serializers.IntegerField(default=9998)
    am_pdp_socket = serializers.CharField(default="/var/amavis/amavisd.sock")
    user_can_release = serializers.BooleanField(default=False)
    self_service = serializers.BooleanField(default=False)
    notification_sender = serializers.EmailField(default="notification@modoboa.org")

    #Manual learning
    manual_learning = serializers.BooleanField(default=True)
    sa_is_local = serializers.BooleanField(default=True)
    default_user = serializers.CharField(default="Default user")
    spamd_address = serializers.CharField(default="127.0.0.1")
    spamd_port = serializers.IntegerField(default=783)
    domain_level_learning = serializers.BooleanField(default=False)
    user_level_learning = serializers.BooleanField(default=False)
