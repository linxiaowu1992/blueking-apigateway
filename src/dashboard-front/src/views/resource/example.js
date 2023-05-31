/*
 * TencentBlueKing is pleased to support the open source community by making
 * 蓝鲸智云 - API 网关(BlueKing - APIGateway) available.
 * Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 *     http://opensource.org/licenses/MIT
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * We undertake not to change the open source license (MIT license) applicable
 * to the current version of the project delivered to anyone in the future.
 */
export default {
  content: `\
# Swagger yaml format template example
swagger: '2.0'
basePath: /
info:
  version: '0.1'
  title: API Gateway Resources
schemes:
- http
paths:
  /users/:
    get:
      operationId: get_users
      description: get users
      x-bk-apigateway-resource:
        isPublic: true
        backend:
          type: HTTP
          method: get
          path: /users/
          timeout: 30
          upstreams:
            loadbalance: roundrobin
            hosts:
            - host: http://0.0.0.1
              weight: 100
        authConfig:
          userVerifiedRequired: false
      `
}