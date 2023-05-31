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
from blue_krill.data_types.enum import EnumField, StructuredEnum
from django.utils.translation import gettext_lazy as _

from apigateway.core.constants import ScopeTypeEnum


class PluginTypeEnum(StructuredEnum):
    IP_RESTRICTION = EnumField("ip-restriction", label=_("IP访问控制"))
    RATE_LIMIT = EnumField("rate_limit", label=_("频率控制"))
    CORS = EnumField("cors", label="CORS")
    CIRCUIT_BREAKER = EnumField("circuit_breaker", label=_("断路器"))
    VERIFIED_USER_EXEMPTED_APPS = EnumField("bk-verified-user-exempted-apps", label=_("免用户认证应用白名单"))


class PluginBindingScopeEnum(StructuredEnum):
    STAGE = EnumField(ScopeTypeEnum.STAGE.value, label=_("环境"))
    RESOURCE = EnumField(ScopeTypeEnum.RESOURCE.value, label=_("资源"))


class DimensionEnum(StructuredEnum):
    API = EnumField("api", label=_("全量资源"))
    RESOURCE = EnumField("resource", label=_("具体资源"))


class PluginStyleEnum(StructuredEnum):
    RAW = EnumField("raw", label=_("原生"))
    DYNAMIC = EnumField("dynamic", label=_("动态"))
    FIX = EnumField("fix", label=_("固定"))