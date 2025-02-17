#
# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - API 网关(BlueKing - APIGateway) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.
#
from django.utils.translation import gettext as _

from apigateway.apps.access_strategy.constants import AccessStrategyTypeEnum
from apigateway.common.error_codes import error_codes
from apigateway.core.constants import ProxyTypeEnum
from apigateway.schema import instances
from apigateway.schema.models import Schema


class SchemaFactory:
    def _get_schema_instance(self, obj):
        try:
            return Schema.objects.get(name=obj.name, type=obj.type, version=obj.version)
        except Schema.DoesNotExist:
            raise error_codes.COMMON_ERROR.format(_("Schema 不存在。"), replace=True)

    def get_proxy_schema(self, proxy_type):
        if proxy_type == ProxyTypeEnum.HTTP.value:
            return self._get_schema_instance(instances.ProxyHTTP())
        elif proxy_type == ProxyTypeEnum.MOCK.value:
            return self._get_schema_instance(instances.ProxyMock())
        raise error_codes.INVALID_ARGS.format(f"unsupported proxy_type: {proxy_type}")

    def get_context_api_bkauth_schema(self):
        return self._get_schema_instance(instances.ContextAPIBKAuth())

    def get_context_resource_bkauth_schema(self):
        return self._get_schema_instance(instances.ContextResourceBKAuth())

    def get_context_stage_proxy_http_schema(self):
        return self._get_schema_instance(instances.ContextStageProxyHTTP())

    def get_context_stage_rate_limit_schema(self):
        return self._get_schema_instance(instances.ContextStageRateLimit())

    def get_context_api_feature_flag_schema(self):
        return self._get_schema_instance(instances.ContextAPIFeatureFlag())

    def get_access_strategy_schema(self, access_strategy_type):
        if access_strategy_type == AccessStrategyTypeEnum.IP_ACCESS_CONTROL.value:
            return self._get_schema_instance(instances.AccessStrategyIPAccessControl())

        elif access_strategy_type == AccessStrategyTypeEnum.RATE_LIMIT.value:
            return self._get_schema_instance(instances.AccessStrategyRateLimit())

        elif access_strategy_type == AccessStrategyTypeEnum.USER_VERIFIED_UNREQUIRED_APPS.value:
            return self._get_schema_instance(instances.AccessStrategyUserVerifiedUnrequiredApps())

        elif access_strategy_type == AccessStrategyTypeEnum.ERROR_STATUS_CODE_200.value:
            return self._get_schema_instance(instances.AccessStrategyErrorStatusCode200())

        elif access_strategy_type == AccessStrategyTypeEnum.CORS.value:
            return self._get_schema_instance(instances.AccessStrategyCORS())

        elif access_strategy_type == AccessStrategyTypeEnum.CIRCUIT_BREAKER.value:
            return self._get_schema_instance(instances.AccessStrategyCircuitBreaker())

        raise error_codes.INVALID_ARGS.format(f"unsupported access_strategy_type: {access_strategy_type}")

    def get_monitor_alarm_strategy_schema(self):
        return self._get_schema_instance(instances.MonitorAlarmStrategy())

    def get_monitor_alarm_filter_schema(self):
        return self._get_schema_instance(instances.MonitorAlarmFilter())

    def get_api_sdk_schema(self):
        return self._get_schema_instance(instances.APISDK())

    def get_micro_gateway_schema(self):
        return self._get_schema_instance(instances.MicroGateway())
