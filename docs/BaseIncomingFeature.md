# BaseIncomingFeature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppress_notifications** | **bool** | If enabled, notifications that come from alerts will be suppressed. Defaults to false | [optional] 
**ignore_teams_from_payload** | **bool** | If enabled, the integration will ignore teams sent in request payloads. Defaults to false | [optional] 
**ignore_recipients_from_payload** | **bool** | If enabled, the integration will ignore recipients sent in request payloads. Defaults to false | [optional] 
**recipients** | [**list[Recipient]**](Recipient.md) | Optional user, schedule, teams or escalation names to calculate which users will receive the notifications of the alert. Recipients which are exceeding the limit are ignored | [optional] 
**is_advanced** | **bool** |  | [optional] 
**ignore_responders_from_payload** | **bool** |  | [optional] 
**ignore_tags_from_payload** | **bool** |  | [optional] 
**ignore_extra_properties_from_payload** | **bool** |  | [optional] 
**responders** | [**list[Recipient]**](Recipient.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**custom_priority** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**extra_properties** | **dict(str, str)** |  | [optional] 
**assigned_team** | [**TeamMeta**](TeamMeta.md) |  | [optional] 
**feature_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


