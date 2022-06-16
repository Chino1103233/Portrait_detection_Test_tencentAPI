import base64
import json

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.iai.v20200303 import iai_client, models

ID = ""
Key = ""
ImgPath = ''


def getApi(FilePath: str):
    with open(FilePath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = base64_data.decode()
    try:
        cred = credential.Credential(ID, Key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-shanghai", clientProfile)

        req = models.DetectFaceRequest()
        params = {
            "MaxFaceNum": 5,
            "MinFaceSize"
            "": 34,
            "Image": base64_code,
            "NeedFaceAttributes": 1,
            "NeedQualityDetection": 0,
            "FaceModelVersion": "3.0",
            "NeedRotateDetection": 0
        }

        req.from_json_string(json.dumps(params))

        resp = client.DetectFace(req)
        resp_str = resp.to_json_string()
        resp_dict = json.loads(resp_str)
        print(resp_str)
        return resp_dict

    except TencentCloudSDKException as err:
        print(err)


# json_data = getApi("C:/Users/wumxi/Desktop/5639f7021e924cbfba3e01818b63d0a0.png")
# print(json_data)

