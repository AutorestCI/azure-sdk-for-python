# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .app_service_certificate import AppServiceCertificate
from .app_service_certificate_resource import AppServiceCertificateResource
from .certificate_details import CertificateDetails
from .app_service_certificate_order import AppServiceCertificateOrder
from .app_service_certificate_order_patch_resource import AppServiceCertificateOrderPatchResource
from .app_service_certificate_patch_resource import AppServiceCertificatePatchResource
from .certificate_email import CertificateEmail
from .certificate_order_action import CertificateOrderAction
from .name_identifier import NameIdentifier
from .proxy_only_resource import ProxyOnlyResource
from .reissue_certificate_order_request import ReissueCertificateOrderRequest
from .renew_certificate_order_request import RenewCertificateOrderRequest
from .resource import Resource
from .site_seal import SiteSeal
from .site_seal_request import SiteSealRequest
from .address import Address
from .contact import Contact
from .host_name import HostName
from .domain_purchase_consent import DomainPurchaseConsent
from .domain import Domain
from .domain_availablility_check_result import DomainAvailablilityCheckResult
from .domain_control_center_sso_request import DomainControlCenterSsoRequest
from .domain_ownership_identifier import DomainOwnershipIdentifier
from .domain_patch_resource import DomainPatchResource
from .domain_recommendation_search_parameters import DomainRecommendationSearchParameters
from .tld_legal_agreement import TldLegalAgreement
from .top_level_domain import TopLevelDomain
from .top_level_domain_agreement_option import TopLevelDomainAgreementOption
from .hosting_environment_profile import HostingEnvironmentProfile
from .certificate import Certificate
from .certificate_patch_resource import CertificatePatchResource
from .deleted_site import DeletedSite
from .csm_operation_display import CsmOperationDisplay
from .dimension import Dimension
from .metric_availability import MetricAvailability
from .metric_specification import MetricSpecification
from .service_specification import ServiceSpecification
from .csm_operation_description_properties import CsmOperationDescriptionProperties
from .csm_operation_description import CsmOperationDescription
from .recommendation import Recommendation
from .recommendation_rule import RecommendationRule
from .virtual_network_profile import VirtualNetworkProfile
from .worker_pool import WorkerPool
from .virtual_ip_mapping import VirtualIPMapping
from .stamp_capacity import StampCapacity
from .network_access_control_entry import NetworkAccessControlEntry
from .name_value_pair import NameValuePair
from .app_service_environment import AppServiceEnvironment
from .capability import Capability
from .csm_move_resource_envelope import CsmMoveResourceEnvelope
from .geo_region import GeoRegion
from .hosting_environment_deployment_info import HostingEnvironmentDeploymentInfo
from .deployment_locations import DeploymentLocations
from .sku_capacity import SkuCapacity
from .global_csm_sku_description import GlobalCsmSkuDescription
from .premier_add_on_offer import PremierAddOnOffer
from .resource_name_availability import ResourceNameAvailability
from .resource_name_availability_request import ResourceNameAvailabilityRequest
from .sku_infos import SkuInfos
from .source_control import SourceControl
from .user import User
from .validate_request import ValidateRequest
from .validate_response_error import ValidateResponseError
from .validate_response import ValidateResponse
from .vnet_parameters import VnetParameters
from .vnet_validation_test_failure import VnetValidationTestFailure
from .vnet_validation_failure_details import VnetValidationFailureDetails
from .api_definition_info import ApiDefinitionInfo
from .file_system_application_logs_config import FileSystemApplicationLogsConfig
from .azure_table_storage_application_logs_config import AzureTableStorageApplicationLogsConfig
from .azure_blob_storage_application_logs_config import AzureBlobStorageApplicationLogsConfig
from .application_logs_config import ApplicationLogsConfig
from .auto_heal_custom_action import AutoHealCustomAction
from .auto_heal_actions import AutoHealActions
from .requests_based_trigger import RequestsBasedTrigger
from .status_codes_based_trigger import StatusCodesBasedTrigger
from .slow_requests_based_trigger import SlowRequestsBasedTrigger
from .auto_heal_triggers import AutoHealTriggers
from .auto_heal_rules import AutoHealRules
from .azure_blob_storage_http_logs_config import AzureBlobStorageHttpLogsConfig
from .database_backup_setting import DatabaseBackupSetting
from .backup_item import BackupItem
from .backup_schedule import BackupSchedule
from .backup_request import BackupRequest
from .cloning_info import CloningInfo
from .conn_string_info import ConnStringInfo
from .conn_string_value_type_pair import ConnStringValueTypePair
from .connection_string_dictionary import ConnectionStringDictionary
from .continuous_web_job import ContinuousWebJob
from .cors_settings import CorsSettings
from .csm_publishing_profile_options import CsmPublishingProfileOptions
from .csm_slot_entity import CsmSlotEntity
from .localizable_string import LocalizableString
from .csm_usage_quota import CsmUsageQuota
from .error_entity import ErrorEntity
from .custom_hostname_analysis_result import CustomHostnameAnalysisResult
from .deployment import Deployment
from .enabled_config import EnabledConfig
from .ramp_up_rule import RampUpRule
from .experiments import Experiments
from .file_system_http_logs_config import FileSystemHttpLogsConfig
from .function_envelope import FunctionEnvelope
from .function_secrets import FunctionSecrets
from .handler_mapping import HandlerMapping
from .host_name_binding import HostNameBinding
from .host_name_ssl_state import HostNameSslState
from .http_logs_config import HttpLogsConfig
from .hybrid_connection import HybridConnection
from .hybrid_connection_key import HybridConnectionKey
from .identifier import Identifier
from .ip_security_restriction import IpSecurityRestriction
from .ms_deploy import MSDeploy
from .ms_deploy_log_entry import MSDeployLogEntry
from .ms_deploy_log import MSDeployLog
from .ms_deploy_status import MSDeployStatus
from .managed_service_identity import ManagedServiceIdentity
from .migrate_my_sql_request import MigrateMySqlRequest
from .migrate_my_sql_status import MigrateMySqlStatus
from .vnet_route import VnetRoute
from .vnet_info import VnetInfo
from .relay_service_connection_entity import RelayServiceConnectionEntity
from .network_features import NetworkFeatures
from .operation import Operation
from .perf_mon_sample import PerfMonSample
from .perf_mon_set import PerfMonSet
from .perf_mon_response import PerfMonResponse
from .premier_add_on import PremierAddOn
from .process_thread_info import ProcessThreadInfo
from .process_module_info import ProcessModuleInfo
from .process_info import ProcessInfo
from .public_certificate import PublicCertificate
from .push_settings import PushSettings
from .resource_metric_name import ResourceMetricName
from .resource_metric_property import ResourceMetricProperty
from .resource_metric_value import ResourceMetricValue
from .resource_metric import ResourceMetric
from .resource_metric_availability import ResourceMetricAvailability
from .resource_metric_definition import ResourceMetricDefinition
from .restore_request import RestoreRequest
from .restore_response import RestoreResponse
from .site_machine_key import SiteMachineKey
from .virtual_directory import VirtualDirectory
from .virtual_application import VirtualApplication
from .site_limits import SiteLimits
from .site_config import SiteConfig
from .snapshot_recovery_target import SnapshotRecoveryTarget
from .snapshot_recovery_request import SnapshotRecoveryRequest
from .slot_swap_status import SlotSwapStatus
from .site import Site
from .site_auth_settings import SiteAuthSettings
from .site_cloneability_criterion import SiteCloneabilityCriterion
from .site_cloneability import SiteCloneability
from .site_config_resource import SiteConfigResource
from .site_configuration_snapshot_info import SiteConfigurationSnapshotInfo
from .site_extension_info import SiteExtensionInfo
from .site_instance import SiteInstance
from .site_logs_config import SiteLogsConfig
from .site_patch_resource import SitePatchResource
from .site_php_error_log_flag import SitePhpErrorLogFlag
from .site_source_control import SiteSourceControl
from .slot_config_names_resource import SlotConfigNamesResource
from .slot_difference import SlotDifference
from .snapshot import Snapshot
from .storage_migration_options import StorageMigrationOptions
from .storage_migration_response import StorageMigrationResponse
from .string_dictionary import StringDictionary
from .triggered_job_run import TriggeredJobRun
from .triggered_job_history import TriggeredJobHistory
from .triggered_web_job import TriggeredWebJob
from .vnet_gateway import VnetGateway
from .web_app_collection import WebAppCollection
from .web_job import WebJob
from .address_response import AddressResponse
from .app_service_environment_resource import AppServiceEnvironmentResource
from .app_service_environment_patch_resource import AppServiceEnvironmentPatchResource
from .sku_description import SkuDescription
from .app_service_plan import AppServicePlan
from .hosting_environment_diagnostics import HostingEnvironmentDiagnostics
from .metric_availabilily import MetricAvailabilily
from .metric_definition import MetricDefinition
from .sku_info import SkuInfo
from .usage import Usage
from .worker_pool_resource import WorkerPoolResource
from .app_service_plan_patch_resource import AppServicePlanPatchResource
from .hybrid_connection_limits import HybridConnectionLimits
from .app_service_certificate_order_paged import AppServiceCertificateOrderPaged
from .app_service_certificate_resource_paged import AppServiceCertificateResourcePaged
from .domain_paged import DomainPaged
from .name_identifier_paged import NameIdentifierPaged
from .domain_ownership_identifier_paged import DomainOwnershipIdentifierPaged
from .top_level_domain_paged import TopLevelDomainPaged
from .tld_legal_agreement_paged import TldLegalAgreementPaged
from .certificate_paged import CertificatePaged
from .deleted_site_paged import DeletedSitePaged
from .csm_operation_description_paged import CsmOperationDescriptionPaged
from .source_control_paged import SourceControlPaged
from .geo_region_paged import GeoRegionPaged
from .premier_add_on_offer_paged import PremierAddOnOfferPaged
from .site_paged import SitePaged
from .backup_item_paged import BackupItemPaged
from .site_config_resource_paged import SiteConfigResourcePaged
from .site_configuration_snapshot_info_paged import SiteConfigurationSnapshotInfoPaged
from .continuous_web_job_paged import ContinuousWebJobPaged
from .deployment_paged import DeploymentPaged
from .identifier_paged import IdentifierPaged
from .function_envelope_paged import FunctionEnvelopePaged
from .host_name_binding_paged import HostNameBindingPaged
from .site_instance_paged import SiteInstancePaged
from .process_info_paged import ProcessInfoPaged
from .process_module_info_paged import ProcessModuleInfoPaged
from .process_thread_info_paged import ProcessThreadInfoPaged
from .resource_metric_definition_paged import ResourceMetricDefinitionPaged
from .resource_metric_paged import ResourceMetricPaged
from .perf_mon_response_paged import PerfMonResponsePaged
from .public_certificate_paged import PublicCertificatePaged
from .site_extension_info_paged import SiteExtensionInfoPaged
from .slot_difference_paged import SlotDifferencePaged
from .snapshot_paged import SnapshotPaged
from .triggered_web_job_paged import TriggeredWebJobPaged
from .triggered_job_history_paged import TriggeredJobHistoryPaged
from .csm_usage_quota_paged import CsmUsageQuotaPaged
from .web_job_paged import WebJobPaged
from .app_service_environment_resource_paged import AppServiceEnvironmentResourcePaged
from .stamp_capacity_paged import StampCapacityPaged
from .worker_pool_resource_paged import WorkerPoolResourcePaged
from .sku_info_paged import SkuInfoPaged
from .usage_paged import UsagePaged
from .app_service_plan_paged import AppServicePlanPaged
from .str_paged import StrPaged
from .hybrid_connection_paged import HybridConnectionPaged
from .web_site_management_client_enums import (
    KeyVaultSecretStatus,
    CertificateProductType,
    ProvisioningState,
    CertificateOrderStatus,
    CertificateOrderActionType,
    DomainStatus,
    AzureResourceType,
    CustomHostNameDnsRecordType,
    HostNameType,
    DnsType,
    DomainType,
    ResourceScopeType,
    NotificationLevel,
    Channels,
    HostingEnvironmentStatus,
    InternalLoadBalancingMode,
    ComputeModeOptions,
    WorkerSizeOptions,
    AccessControlEntryAction,
    AppServicePlanRestrictions,
    InAvailabilityReasonType,
    CheckNameResourceTypes,
    ValidateResourceTypes,
    LogLevel,
    AutoHealActionType,
    BackupItemStatus,
    DatabaseType,
    FrequencyUnit,
    BackupRestoreOperationType,
    ConnectionStringType,
    ContinuousWebJobStatus,
    WebJobType,
    PublishingProfileFormat,
    DnsVerificationTestResult,
    SslState,
    HostType,
    MSDeployLogEntryType,
    MSDeployProvisioningState,
    MySqlMigrationType,
    OperationStatus,
    RouteType,
    PublicCertificateLocation,
    UsageState,
    SiteAvailabilityState,
    ScmType,
    ManagedPipelineMode,
    SiteLoadBalancing,
    UnauthenticatedClientAction,
    BuiltInAuthenticationProvider,
    CloneAbilityResult,
    SiteExtensionType,
    TriggeredWebJobStatus,
    StatusOptions,
    SkuName,
)

__all__ = [
    'AppServiceCertificate',
    'AppServiceCertificateResource',
    'CertificateDetails',
    'AppServiceCertificateOrder',
    'AppServiceCertificateOrderPatchResource',
    'AppServiceCertificatePatchResource',
    'CertificateEmail',
    'CertificateOrderAction',
    'NameIdentifier',
    'ProxyOnlyResource',
    'ReissueCertificateOrderRequest',
    'RenewCertificateOrderRequest',
    'Resource',
    'SiteSeal',
    'SiteSealRequest',
    'Address',
    'Contact',
    'HostName',
    'DomainPurchaseConsent',
    'Domain',
    'DomainAvailablilityCheckResult',
    'DomainControlCenterSsoRequest',
    'DomainOwnershipIdentifier',
    'DomainPatchResource',
    'DomainRecommendationSearchParameters',
    'TldLegalAgreement',
    'TopLevelDomain',
    'TopLevelDomainAgreementOption',
    'HostingEnvironmentProfile',
    'Certificate',
    'CertificatePatchResource',
    'DeletedSite',
    'CsmOperationDisplay',
    'Dimension',
    'MetricAvailability',
    'MetricSpecification',
    'ServiceSpecification',
    'CsmOperationDescriptionProperties',
    'CsmOperationDescription',
    'Recommendation',
    'RecommendationRule',
    'VirtualNetworkProfile',
    'WorkerPool',
    'VirtualIPMapping',
    'StampCapacity',
    'NetworkAccessControlEntry',
    'NameValuePair',
    'AppServiceEnvironment',
    'Capability',
    'CsmMoveResourceEnvelope',
    'GeoRegion',
    'HostingEnvironmentDeploymentInfo',
    'DeploymentLocations',
    'SkuCapacity',
    'GlobalCsmSkuDescription',
    'PremierAddOnOffer',
    'ResourceNameAvailability',
    'ResourceNameAvailabilityRequest',
    'SkuInfos',
    'SourceControl',
    'User',
    'ValidateRequest',
    'ValidateResponseError',
    'ValidateResponse',
    'VnetParameters',
    'VnetValidationTestFailure',
    'VnetValidationFailureDetails',
    'ApiDefinitionInfo',
    'FileSystemApplicationLogsConfig',
    'AzureTableStorageApplicationLogsConfig',
    'AzureBlobStorageApplicationLogsConfig',
    'ApplicationLogsConfig',
    'AutoHealCustomAction',
    'AutoHealActions',
    'RequestsBasedTrigger',
    'StatusCodesBasedTrigger',
    'SlowRequestsBasedTrigger',
    'AutoHealTriggers',
    'AutoHealRules',
    'AzureBlobStorageHttpLogsConfig',
    'DatabaseBackupSetting',
    'BackupItem',
    'BackupSchedule',
    'BackupRequest',
    'CloningInfo',
    'ConnStringInfo',
    'ConnStringValueTypePair',
    'ConnectionStringDictionary',
    'ContinuousWebJob',
    'CorsSettings',
    'CsmPublishingProfileOptions',
    'CsmSlotEntity',
    'LocalizableString',
    'CsmUsageQuota',
    'ErrorEntity',
    'CustomHostnameAnalysisResult',
    'Deployment',
    'EnabledConfig',
    'RampUpRule',
    'Experiments',
    'FileSystemHttpLogsConfig',
    'FunctionEnvelope',
    'FunctionSecrets',
    'HandlerMapping',
    'HostNameBinding',
    'HostNameSslState',
    'HttpLogsConfig',
    'HybridConnection',
    'HybridConnectionKey',
    'Identifier',
    'IpSecurityRestriction',
    'MSDeploy',
    'MSDeployLogEntry',
    'MSDeployLog',
    'MSDeployStatus',
    'ManagedServiceIdentity',
    'MigrateMySqlRequest',
    'MigrateMySqlStatus',
    'VnetRoute',
    'VnetInfo',
    'RelayServiceConnectionEntity',
    'NetworkFeatures',
    'Operation',
    'PerfMonSample',
    'PerfMonSet',
    'PerfMonResponse',
    'PremierAddOn',
    'ProcessThreadInfo',
    'ProcessModuleInfo',
    'ProcessInfo',
    'PublicCertificate',
    'PushSettings',
    'ResourceMetricName',
    'ResourceMetricProperty',
    'ResourceMetricValue',
    'ResourceMetric',
    'ResourceMetricAvailability',
    'ResourceMetricDefinition',
    'RestoreRequest',
    'RestoreResponse',
    'SiteMachineKey',
    'VirtualDirectory',
    'VirtualApplication',
    'SiteLimits',
    'SiteConfig',
    'SnapshotRecoveryTarget',
    'SnapshotRecoveryRequest',
    'SlotSwapStatus',
    'Site',
    'SiteAuthSettings',
    'SiteCloneabilityCriterion',
    'SiteCloneability',
    'SiteConfigResource',
    'SiteConfigurationSnapshotInfo',
    'SiteExtensionInfo',
    'SiteInstance',
    'SiteLogsConfig',
    'SitePatchResource',
    'SitePhpErrorLogFlag',
    'SiteSourceControl',
    'SlotConfigNamesResource',
    'SlotDifference',
    'Snapshot',
    'StorageMigrationOptions',
    'StorageMigrationResponse',
    'StringDictionary',
    'TriggeredJobRun',
    'TriggeredJobHistory',
    'TriggeredWebJob',
    'VnetGateway',
    'WebAppCollection',
    'WebJob',
    'AddressResponse',
    'AppServiceEnvironmentResource',
    'AppServiceEnvironmentPatchResource',
    'SkuDescription',
    'AppServicePlan',
    'HostingEnvironmentDiagnostics',
    'MetricAvailabilily',
    'MetricDefinition',
    'SkuInfo',
    'Usage',
    'WorkerPoolResource',
    'AppServicePlanPatchResource',
    'HybridConnectionLimits',
    'AppServiceCertificateOrderPaged',
    'AppServiceCertificateResourcePaged',
    'DomainPaged',
    'NameIdentifierPaged',
    'DomainOwnershipIdentifierPaged',
    'TopLevelDomainPaged',
    'TldLegalAgreementPaged',
    'CertificatePaged',
    'DeletedSitePaged',
    'CsmOperationDescriptionPaged',
    'SourceControlPaged',
    'GeoRegionPaged',
    'PremierAddOnOfferPaged',
    'SitePaged',
    'BackupItemPaged',
    'SiteConfigResourcePaged',
    'SiteConfigurationSnapshotInfoPaged',
    'ContinuousWebJobPaged',
    'DeploymentPaged',
    'IdentifierPaged',
    'FunctionEnvelopePaged',
    'HostNameBindingPaged',
    'SiteInstancePaged',
    'ProcessInfoPaged',
    'ProcessModuleInfoPaged',
    'ProcessThreadInfoPaged',
    'ResourceMetricDefinitionPaged',
    'ResourceMetricPaged',
    'PerfMonResponsePaged',
    'PublicCertificatePaged',
    'SiteExtensionInfoPaged',
    'SlotDifferencePaged',
    'SnapshotPaged',
    'TriggeredWebJobPaged',
    'TriggeredJobHistoryPaged',
    'CsmUsageQuotaPaged',
    'WebJobPaged',
    'AppServiceEnvironmentResourcePaged',
    'StampCapacityPaged',
    'WorkerPoolResourcePaged',
    'SkuInfoPaged',
    'UsagePaged',
    'AppServicePlanPaged',
    'StrPaged',
    'HybridConnectionPaged',
    'KeyVaultSecretStatus',
    'CertificateProductType',
    'ProvisioningState',
    'CertificateOrderStatus',
    'CertificateOrderActionType',
    'DomainStatus',
    'AzureResourceType',
    'CustomHostNameDnsRecordType',
    'HostNameType',
    'DnsType',
    'DomainType',
    'ResourceScopeType',
    'NotificationLevel',
    'Channels',
    'HostingEnvironmentStatus',
    'InternalLoadBalancingMode',
    'ComputeModeOptions',
    'WorkerSizeOptions',
    'AccessControlEntryAction',
    'AppServicePlanRestrictions',
    'InAvailabilityReasonType',
    'CheckNameResourceTypes',
    'ValidateResourceTypes',
    'LogLevel',
    'AutoHealActionType',
    'BackupItemStatus',
    'DatabaseType',
    'FrequencyUnit',
    'BackupRestoreOperationType',
    'ConnectionStringType',
    'ContinuousWebJobStatus',
    'WebJobType',
    'PublishingProfileFormat',
    'DnsVerificationTestResult',
    'SslState',
    'HostType',
    'MSDeployLogEntryType',
    'MSDeployProvisioningState',
    'MySqlMigrationType',
    'OperationStatus',
    'RouteType',
    'PublicCertificateLocation',
    'UsageState',
    'SiteAvailabilityState',
    'ScmType',
    'ManagedPipelineMode',
    'SiteLoadBalancing',
    'UnauthenticatedClientAction',
    'BuiltInAuthenticationProvider',
    'CloneAbilityResult',
    'SiteExtensionType',
    'TriggeredWebJobStatus',
    'StatusOptions',
    'SkuName',
]
