#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from pykube.config import KubeConfig
from pykube.http import HTTPClient


def get_kube_api(transport):
    config = {
        "apiVersion": "v1",
        "clusters": [
            {
                "cluster":{
                    "server": "http://{0}:{1}".format(transport['host'],
                                                      transport['port'])
                },
                "name": "opensnek"
            }
        ],
        "contexts": [
            {
                "context": {
                    "cluster": "opensnek",
                    "namespace": "",
                    "user": "user"
                },
                "name": "osctx"
            }
        ],
        "users": [
            {
                "user": {},
                "name": "user"
            }
        ],
        "current-context": "osctx",
        "kind": "Config",
        "preferences": {}
    }

    return HTTPClient(KubeConfig(config))
