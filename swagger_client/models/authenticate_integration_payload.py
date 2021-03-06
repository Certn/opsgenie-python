# coding: utf-8

"""
    Opsgenie REST API

    Opsgenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AuthenticateIntegrationPayload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):  # noqa: E501
        """AuthenticateIntegrationPayload - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self.discriminator = None

        self.type = type

    @property
    def type(self):
        """Gets the type of this AuthenticateIntegrationPayload.  # noqa: E501


        :return: The type of this AuthenticateIntegrationPayload.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthenticateIntegrationPayload.


        :param type: The type of this AuthenticateIntegrationPayload.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Airbrake", "AlertLogic", "AlertSite", "AmazonCloudTrail", "AmazonEc2AutoScaling", "AmazonRds", "AmazonRoute53HealthCheck", "AmazonSes", "AmazonSns", "AmazonSnsOutgoing", "AmazonSecurityHub", "API", "Apica", "Apimetrics", "AppDynamics", "AppOptics", "AppSignal", "AppSignalV2", "Atatus", "AtlassianBambooEmail", "AutotaskAEMEmail", "AutoTaskEmail", "Azure", "AzureAutoScale", "AzureOMS", "AzureServiceHealth", "AzureResourceHealth", "BigPanda", "Bitbucket", "BlueMatador", "BMCFootPrintsV11", "BMCFootPrintsV12", "BMCRemedy", "BMCRemedyForce", "BMCRemedyOnDemand", "Boundary", "Campfire", "Catchpoint", "CheckMK", "Cherwell", "CircleCi", "Circonus", "CloudMonix", "CloudSploit", "CloudWatch", "CloudWatchEvents", "Codeship", "Compose", "ConnectWise", "ConnectWiseManage", "ConnectWiseManageV2", "ConnectWiseAutomate", "Consul", "CopperEgg", "Crashlytics", "Datadog", "DataloopIO", "Desk", "Detectify", "DNSCheck", "DripStat", "Ruxit", "DynatraceV2", "DynatraceAppMon", "Email", "Errorception", "ESWatcher", "EvidentIO", "Flock", "Flowdock", "FlowdockV2", "Freshdesk", "Freshservice", "GhostInspector", "GitHub", "GitLab", "GoogleStackdriver", "Grafana", "GrafanaV2", "Graylog", "Heartbeat", "HipChat", "HipChatV2", "HipChatAddOn", "Honeybadger", "HostedGraphite", "HPServiceManager", "Humio", "Icinga", "Icinga2", "IncomingCall", "Instana", "Jenkins", "Jira", "JiraServiceDesk", "Kapacitor", "Kayako", "Kore", "LabTechEmail", "Librato", "LibreNMS", "Lightstep", "Logentries", "Loggly", "LogicMonitor", "Logstash", "LogzIO", "Looker", "Loom", "Magentrix", "Marid", "OEC", "Mattermost", "MongoDBCloud", "Monitis", "MonitisEmail", "Moxtra", "MSTeams", "MSTeamsV2", "Nagios", "NagiosV2", "NagiosXI", "NagiosXIV2", "NeustarEmail", "Netuitive", "NewRelic", "NewRelicV2", "NewRelicSyntheticsEmail", "NodePing", "Observium", "ObserviumV2", "OEM", "OEMEmail", "OP5", "OpsDash", "OpsGenie", "Opsview", "PagerDutyCompatibility", "Panopta", "Papertrail", "Pingdom", "PingdomV2", "PingdomWebhook", "Pingometer", "Planio", "Prometheus", "Prtg", "Rackspace", "Raygun", "RedGateSqlMonitorEmail", "Riemann", "Rigor", "RingCentralEmail", "RingCentralGlip", "Rollbar", "Runscope", "SalesForceServiceCloud", "SaltStack", "Scalyr", "Sentry", "SCOM", "Scout", "SematextSpm", "Sensu", "ServerDensity", "ServerGuard24", "ServiceNow", "ServiceNowV2", "ServiceNowV3", "Signalfx", "SignalFXV2", "SignalSciences", "Site24x7", "Slack", "SlackApp", "Soasta", "Solarwinds", "SolarwindsMSPNCentral", "SolarWindsWebHelpDesk", "Splunk", "SplunkITSI", "Stackdriver", "StackStorm", "StatusCake", "StatusHub", "StatusIO", "StatusPageIO", "Statusy", "StruxureWare", "SumoLogic", "SysdigCloud", "ThousandEyes", "ThreatStack", "Thundra", "Tideways", "Trace", "TrackIt", "TravisCI", "Twilio", "UpdownIO", "UptimeRobot", "UptimeRobotEmail", "UptimeWebhook", "UptrendsEmail", "VCenter", "VCSA", "VividCortex", "Wavefront", "WhatsUpGold", "Webhook", "Workato", "XLRelease", "Xmpp", "Zabbix", "Zapier", "Zendesk", "Zenoss", "ZyrionEmail", "ManageEngine"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AuthenticateIntegrationPayload, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthenticateIntegrationPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
