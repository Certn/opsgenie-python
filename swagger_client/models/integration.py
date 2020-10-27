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


class Integration(object):
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
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'enabled': 'bool',
        'owner_team': 'TeamMeta',
        'is_global': 'bool',
        'read_only': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'enabled': 'enabled',
        'owner_team': 'ownerTeam',
        'is_global': 'isGlobal',
        'read_only': '_readOnly'
    }

    discriminator_value_class_map = {
        'AppDynamics': 'AppDynamicsIntegration',
        'GitHub': 'GitHubIntegration',
        'Monitis': 'MonitisIntegration',
        'NewRelic': 'NewRelicIntegration',
        'CloudMonix': 'CloudMonixIntegration',
        'Scout': 'ScoutIntegration',
        'AmazonRds': 'AmazonRdsIntegration',
        'Grafana': 'GrafanaIntegration',
        'SCOM': 'ScomIntegration',
        'Detectify': 'DetectifyIntegration',
        'RedGateSqlMonitorEmail': 'RedGateSqlMonitorEmailIntegration',
        'DataloopIO': 'DataloopIOIntegration',
        'Site24x7': 'Site24x7Integration',
        'Humio': 'HumioIntegration',
        'AmazonSns': 'AmazonSnsIntegration',
        'SplunkITSI': 'SplunkITSIIntegration',
        'AlertLogic': 'AlertLogicIntegration',
        'RingCentralEmail': 'RingCentralEmailIntegration',
        'Sentry': 'SentryIntegration',
        'SignalFXV2': 'SignalFXV2Integration',
        'PagerDutyCompatibility': 'PagerDutyCompatibilityIntegration',
        'Slack': 'SlackIntegration',
        'Honeybadger': 'HoneybadgerIntegration',
        'Zapier': 'ZapierIntegration',
        'Freshservice': 'FreshserviceIntegration',
        'MongoDBCloud': 'MongoDBCloudIntegration',
        'Xmpp': 'XmppIntegration',
        'Tideways': 'TidewaysIntegration',
        'AmazonCloudTrail': 'AmazonCloudTrailIntegration',
        'StatusHub': 'StatusHubIntegration',
        'HipChatV2': 'HipChatIntegrationV2',
        'ConnectWiseManageV2': 'ConnectWiseManageV2Integration',
        'ObserviumV2': 'ObserviumV2Integration',
        'Kapacitor': 'KapacitorIntegration',
        'Workato': 'WorkatoIntegration',
        'Kore': 'KoreIntegration',
        'AmazonSnsOutgoing': 'AmazonSnsOutgoingIntegration',
        'NeustarEmail': 'NeustarIntegration',
        'ServiceNowV2': 'ServiceNowV2Integration',
        'VCSA': 'VCSAIntegration',
        'Catchpoint': 'CatchpointIntegration',
        'MSTeamsV2': 'MSTeamsV2Integration',
        'SolarwindsMSPNCentral': 'SolarwindsMSPNCentralIntegration',
        'Prometheus': 'PrometheusIntegration',
        'Boundary': 'BoundaryIntegration',
        'Librato': 'LibratoIntegration',
        'Campfire': 'CampfireIntegration',
        'SumoLogic': 'SumoLogicIntegration',
        'Papertrail': 'PapertrailIntegration',
        'BMCFootPrintsV12': 'BMCFootPrintsV12Integration',
        'BlueMatador': 'BlueMatadorIntegration',
        'Icinga2': 'Icinga2Integration',
        'Ruxit': 'DynatraceIntegration',
        'SolarWindsWebHelpDesk': 'SolarWindsWebHelpDeskIntegration',
        'XLRelease': 'XLReleaseIntegration',
        'AppOptics': 'AppOpticsIntegration',
        'Moxtra': 'MoxtraIntegration',
        'Cherwell': 'CherwellIntegration',
        'DripStat': 'DripStatIntegration',
        'Panopta': 'PanoptaIntegration',
        'AlertSite': 'AlertSiteIntegration',
        'UptimeRobot': 'UptimeRobotIntegration',
        'VividCortex': 'VividCortexIntegration',
        'Flowdock': 'FlowdockIntegration',
        'CloudWatch': 'CloudWatchIntegration',
        'Rigor': 'RigorIntegration',
        'BMCRemedyOnDemand': 'BMCRemedyOnDemandIntegration',
        'AzureOMS': 'AzureOMSIntegration',
        'NodePing': 'NodePingIntegration',
        'Lightstep': 'LightstepIntegration',
        'Zendesk': 'ZendeskIntegration',
        'PingdomV2': 'PingdomV2Integration',
        'BMCRemedyForce': 'BMCRemedyForceIntegration',
        'FlowdockV2': 'FlowdockV2Integration',
        'Freshdesk': 'FreshdeskIntegration',
        'OpsGenie': 'OpsGenieIntegration',
        'AzureResourceHealth': 'AzureResourceHealthIntegration',
        'Riemann': 'RiemannIntegration',
        'AutoTaskEmail': 'AutoTaskEmailIntegration',
        'ManageEngine': 'ManageEngineIntegrationDTO',
        'Azure': 'AzureIntegration',
        'Compose': 'ComposeIntegration',
        'Splunk': 'SplunkIntegration',
        'NewRelicV2': 'NewRelicV2Integration',
        'AmazonSecurityHub': 'AmazonSecurityHubIntegration',
        'GitLab': 'GitLabIntegration',
        'CheckMK': 'CheckMKIntegration',
        'Kayako': 'KayakoIntegration',
        'OpsDash': 'OpsDashIntegration',
        'AutotaskAEMEmail': 'AutotaskAEMEmailIntegration',
        'Codeship': 'CodeshipIntegration',
        'DNSCheck': 'DnsCheckIntegration',
        'AtlassianBambooEmail': 'AtlassianBambooIntegration',
        'Opsview': 'OpsviewIntegration',
        'ServiceNow': 'ServiceNowIntegration',
        'LogzIO': 'LogzIOIntegration',
        'AzureServiceHealth': 'AzureServiceHealthIntegration',
        'OEM': 'OEMIntegration',
        'StackStorm': 'StackStormIntegration',
        'DynatraceAppMon': 'DynatraceAppMonIntegration',
        'API': 'ApiIntegration',
        'Apimetrics': 'ApimetricsIntegration',
        'Instana': 'InstanaIntegration',
        'Logstash': 'LogstashIntegration',
        'Consul': 'ConsulIntegration',
        'Runscope': 'RunscopeIntegration',
        'ConnectWiseAutomate': 'ConnectWiseAutomateIntegration',
        'SematextSpm': 'SematextSpmIntegration',
        'Trace': 'TraceIntegration',
        'UpdownIO': 'UpdownIOIntegration',
        'AmazonEc2AutoScaling': 'AmazonEc2AutoScalingIntegration',
        'Magentrix': 'MagentrixIntegration',
        'Solarwinds': 'SolarwindsIntegration',
        'Logentries': 'LogentriesIntegration',
        'Marid': 'MaridIntegration',
        'WhatsUpGold': 'WhatsUpGoldIntegration',
        'Planio': 'PlanioIntegration',
        'Crashlytics': 'CrashlyticsIntegration',
        'BMCFootPrintsV11': 'BMCFootPrintsV11Integration',
        'Soasta': 'SoastaIntegration',
        'Circonus': 'CirconusIntegration',
        'UptimeRobotEmail': 'UptimeRobotEmailIntegration',
        'HostedGraphite': 'HostedGraphiteIntegration',
        'OP5': 'OP5Integration',
        'Loom': 'LoomIntegration',
        'ThousandEyes': 'ThousandEyesIntegration',
        'SaltStack': 'SaltStackIntegration',
        'Airbrake': 'AirbrakeIntegration',
        'ESWatcher': 'XPackAlertingIntegration',
        'CloudWatchEvents': 'CloudWatchEventsIntegration',
        'MSTeams': 'MSTeamsIntegration',
        'Desk': 'DeskIntegration',
        'HipChat': 'HipChatIntegration',
        'BigPanda': 'BigPandaIntegration',
        'StatusCake': 'StatusCakeIntegration',
        'Email': 'EmailIntegration',
        'CircleCi': 'CircleCiIntegration',
        'SlackApp': 'SlackAppIntegration',
        'Zabbix': 'ZabbixIntegration',
        'ZyrionEmail': 'ZyrionIntegration',
        'TravisCI': 'TravisCIIntegration',
        'Icinga': 'IcingaIntegration',
        'Pingometer': 'PingometerIntegration',
        'Jenkins': 'JenkinsIntegration',
        'Atatus': 'AtatusIntegration',
        'CloudSploit': 'CloudSploitIntegration',
        'UptrendsEmail': 'UptrendsEmailIntegration',
        'Twilio': 'TwilioIntegration',
        'Observium': 'ObserviumIntegration',
        'JiraServiceDesk': 'JiraServiceDeskIntegration',
        'GoogleStackdriver': 'GoogleStackDriverIntegration',
        'Statusy': 'StatusyIntegration',
        'Raygun': 'RaygunIntegration',
        'CopperEgg': 'CopperEggIntegration',
        'BMCRemedy': 'BMCRemedyIntegration',
        'Datadog': 'DatadogIntegration',
        'HipChatAddOn': 'HipChatAddOnIntegration',
        'StruxureWare': 'StruxureWareIntegration',
        'Heartbeat': 'HeartbeatIntegration',
        'SalesForceServiceCloud': 'SalesForceServiceCloudIntegration',
        'HPServiceManager': 'HPServiceManagerIntegration',
        'Pingdom': 'PingdomIntegration',
        'ConnectWiseManage': 'ConnectWiseManageIntegration',
        'OEC': 'OECIntegration',
        'Wavefront': 'WavefrontIntegration',
        'ServerDensity': 'ServerDensityIntegration',
        'Netuitive': 'NetuitiveIntegration',
        'ThreatStack': 'ThreatStackIntegration',
        'PingdomWebhook': 'PingdomWebhookIntegration',
        'MonitisEmail': 'MonitisEmailIntegration',
        'AzureAutoScale': 'AzureAutoScaleIntegration',
        'GhostInspector': 'GhostInspectorIntegration',
        'LabTechEmail': 'LabTechEmailIntegration',
        'OEMEmail': 'OEMEmailIntegration',
        'NagiosXIV2': 'NagiosXIIntegrationV2',
        'NagiosXI': 'NagiosXIIntegrationV1',
        'AmazonRoute53HealthCheck': 'AmazonRoute53HealthCheckIntegration',
        'Looker': 'LookerIntegration',
        'Nagios': 'NagiosIntegrationV1',
        'NagiosV2': 'NagiosIntegrationV2',
        'Zenoss': 'ZenossIntegration',
        'Jira': 'JiraIntegration',
        'Bitbucket': 'BitbucketIntegration',
        'Signalfx': 'SignalfxIntegration',
        'ConnectWise': 'ConnectWiseIntegration',
        'EvidentIO': 'EvidentIOIntegration',
        'VCenter': 'VCenterIntegration',
        'SignalSciences': 'SignalSciencesIntegration',
        'IncomingCall': 'IncomingCallIntegration',
        'Graylog': 'GraylogIntegration',
        'Flock': 'FlockIntegration',
        'LogicMonitor': 'LogicMonitorIntegration',
        'Apica': 'ApicaIntegration',
        'Rackspace': 'RackspaceIntegration',
        'RingCentralGlip': 'RingCentralGlipIntegration',
        'Stackdriver': 'StackdriverIntegration',
        'AppSignalV2': 'AppSignalV2Integration',
        'SysdigCloud': 'SysdigCloudIntegration',
        'StatusPageIO': 'StatusPageIOIntegration',
        'Mattermost': 'MattermostIntegration',
        'TrackIt': 'TrackItIntegration',
        'StatusIO': 'StatusIOIntegration',
        'Errorception': 'ErrorceptionIntegration',
        'DynatraceV2': 'DynatraceV2Integration',
        'Scalyr': 'ScalyrIntegration',
        'UptimeWebhook': 'UptimeWebhookIntegration',
        'AmazonSes': 'AmazonSesIntegration',
        'AppSignal': 'AppSignalIntegration',
        'ServiceNowV3': 'ServiceNowV3Integration',
        'Sensu': 'SensuIntegration',
        'Thundra': 'ThundraIntegration',
        'Webhook': 'WebhookIntegration',
        'Loggly': 'LogglyIntegration',
        'ServerGuard24': 'ServerGuard24Integration',
        'Rollbar': 'RollbarIntegration',
        'GrafanaV2': 'GrafanaV2Integration',
        'LibreNMS': 'LibreNMSIntegration',
        'Prtg': 'PrtgIntegration'
    }

    def __init__(self, type=None, id=None, name=None, enabled=None, owner_team=None, is_global=None, read_only=None):  # noqa: E501
        """Integration - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._id = None
        self._name = None
        self._enabled = None
        self._owner_team = None
        self._is_global = None
        self._read_only = None
        self.discriminator = 'type'

        self.type = type
        if id is not None:
            self.id = id
        self.name = name
        if enabled is not None:
            self.enabled = enabled
        if owner_team is not None:
            self.owner_team = owner_team
        if is_global is not None:
            self.is_global = is_global
        if read_only is not None:
            self.read_only = read_only

    @property
    def type(self):
        """Gets the type of this Integration.  # noqa: E501

        Type of the integration. (For instance, \"API\" for API Integration)  # noqa: E501

        :return: The type of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Integration.

        Type of the integration. (For instance, \"API\" for API Integration)  # noqa: E501

        :param type: The type of this Integration.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Airbrake", "AlertLogic", "AlertSite", "AmazonCloudTrail", "AmazonEc2AutoScaling", "AmazonRds", "AmazonRoute53HealthCheck", "AmazonSecurityHub", "AmazonSes", "AmazonSns", "AmazonSnsOutgoing", "API", "Apica", "Apimetrics", "AppDynamics", "AppOptics", "AppSignal", "AppSignalV2", "Atatus", "AtlassianBambooEmail", "AutotaskAEMEmail", "AutoTaskEmail", "Azure", "AzureAutoScale", "AzureOMS", "AzureResourceHealth", "AzureServiceHealth", "BigPanda", "Bitbucket", "BlueMatador", "BMCFootPrintsV11", "BMCFootPrintsV12", "BMCRemedy", "BMCRemedyForce", "BMCRemedyOnDemand", "Boundary", "Campfire", "Catchpoint", "CheckMK", "Cherwell", "CircleCi", "Circonus", "CloudMonix", "CloudSploit", "CloudWatch", "CloudWatchEvents", "Codeship", "Compose", "ConnectWise", "ConnectWiseAutomate", "ConnectWiseManage", "ConnectWiseManageV2", "Consul", "CopperEgg", "Crashlytics", "Datadog", "DataloopIO", "Desk", "Detectify", "DNSCheck", "DripStat", "DynatraceAppMon", "DynatraceV2", "Email", "Errorception", "ESWatcher", "EvidentIO", "Flock", "Flowdock", "FlowdockV2", "Freshdesk", "Freshservice", "GhostInspector", "GitHub", "GitLab", "GoogleStackdriver", "Grafana", "GrafanaV2", "Graylog", "Heartbeat", "HipChat", "HipChatAddOn", "HipChatV2", "Honeybadger", "HostedGraphite", "HPServiceManager", "Humio", "Icinga", "Icinga2", "IncomingCall", "Instana", "Jenkins", "Jira", "JiraServiceDesk", "Kapacitor", "Kayako", "Kore", "LabTechEmail", "Librato", "LibreNMS", "Lightstep", "Logentries", "Loggly", "LogicMonitor", "Logstash", "LogzIO", "Looker", "Loom", "Magentrix", "ManageEngine", "Marid", "Mattermost", "MongoDBCloud", "Monitis", "MonitisEmail", "Moxtra", "MSTeams", "MSTeamsV2", "Nagios", "NagiosV2", "NagiosXI", "NagiosXIV2", "Netuitive", "NeustarEmail", "NewRelic", "NewRelicV2", "NodePing", "Observium", "ObserviumV2", "OEC", "OEM", "OEMEmail", "OP5", "OpsDash", "OpsGenie", "Opsview", "PagerDutyCompatibility", "Panopta", "Papertrail", "Pingdom", "PingdomV2", "PingdomWebhook", "Pingometer", "Planio", "Prometheus", "Prtg", "Rackspace", "Raygun", "RedGateSqlMonitorEmail", "Riemann", "Rigor", "RingCentralEmail", "RingCentralGlip", "Rollbar", "Runscope", "Ruxit", "SalesForceServiceCloud", "SaltStack", "Scalyr", "SCOM", "Scout", "SematextSpm", "Sensu", "Sentry", "ServerDensity", "ServerGuard24", "ServiceNow", "ServiceNowV2", "ServiceNowV3", "Signalfx", "SignalFXV2", "SignalSciences", "Site24x7", "Slack", "SlackApp", "Soasta", "Solarwinds", "SolarwindsMSPNCentral", "SolarWindsWebHelpDesk", "Splunk", "SplunkITSI", "Stackdriver", "StackStorm", "StatusCake", "StatusHub", "StatusIO", "StatusPageIO", "Statusy", "StruxureWare", "SumoLogic", "SysdigCloud", "ThousandEyes", "ThreatStack", "Thundra", "Tideways", "Trace", "TrackIt", "TravisCI", "Twilio", "UpdownIO", "UptimeRobot", "UptimeRobotEmail", "UptimeWebhook", "UptrendsEmail", "VCenter", "VCSA", "VividCortex", "Wavefront", "Webhook", "WhatsUpGold", "Workato", "XLRelease", "Xmpp", "Zabbix", "Zapier", "Zendesk", "Zenoss", "ZyrionEmail"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this Integration.  # noqa: E501


        :return: The id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Integration.


        :param id: The id of this Integration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Integration.  # noqa: E501

        Name of the integration. Name must be unique for each integration  # noqa: E501

        :return: The name of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Integration.

        Name of the integration. Name must be unique for each integration  # noqa: E501

        :param name: The name of this Integration.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this Integration.  # noqa: E501

        This parameter is for specifying whether the integration will be enabled or not  # noqa: E501

        :return: The enabled of this Integration.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Integration.

        This parameter is for specifying whether the integration will be enabled or not  # noqa: E501

        :param enabled: The enabled of this Integration.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def owner_team(self):
        """Gets the owner_team of this Integration.  # noqa: E501


        :return: The owner_team of this Integration.  # noqa: E501
        :rtype: TeamMeta
        """
        return self._owner_team

    @owner_team.setter
    def owner_team(self, owner_team):
        """Sets the owner_team of this Integration.


        :param owner_team: The owner_team of this Integration.  # noqa: E501
        :type: TeamMeta
        """

        self._owner_team = owner_team

    @property
    def is_global(self):
        """Gets the is_global of this Integration.  # noqa: E501


        :return: The is_global of this Integration.  # noqa: E501
        :rtype: bool
        """
        return self._is_global

    @is_global.setter
    def is_global(self, is_global):
        """Sets the is_global of this Integration.


        :param is_global: The is_global of this Integration.  # noqa: E501
        :type: bool
        """

        self._is_global = is_global

    @property
    def read_only(self):
        """Gets the read_only of this Integration.  # noqa: E501


        :return: The read_only of this Integration.  # noqa: E501
        :rtype: list[str]
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Integration.


        :param read_only: The read_only of this Integration.  # noqa: E501
        :type: list[str]
        """

        self._read_only = read_only

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(Integration, dict):
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
        if not isinstance(other, Integration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other