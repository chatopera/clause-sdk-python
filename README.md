# py-clause

开源语义理解服务[Clause](https://github.com/chatopera/clause)的 Python 客户端。

## 安装

该Python包已经上传至[pypi](https://pypi.org/project/clause/)，用户可以使用pip直接安装。

```
pip install clause
```

当前稳定版本为 `1.x`。

示例代码:

```
from clause import Client, Data
from clause import CustomDict

bot = Client(HOST_IP, HOST_PORT)
# 创建自定义词典
data = Data()
data.customdict = CustomDict(name=customDictName, chatbotID=chatbot_id)
response = self.bot.postCustomDict(data)
```

更多使用请参考```示例程序```。

## 示例程序

前提是已经部署了 Clause 服务，该示例程序介绍了如何在 Python 应用中，使用 Clause 服务构建聊天机器人，包括创建意图、创建说法、创建词典、引用系统词典、创建槽位、训练机器人和对话等部分。

该示例程序实现的[对话场景介绍](https://github.com/chatopera/clause/wiki/%E7%A4%BA%E4%BE%8B%E7%A8%8B%E5%BA%8F)，熟悉对话场景有助于更好的掌握程序。

```
git clone https://github.com/chatopera/py-clause.git
cd py-clause
cp scripts/localrc.sample scripts/localrc
vim scripts/localrc # 使用文本编辑器编辑 scripts/localrc，更新CL_HOST和CL_PORT
./scripts/test.sh   # 执行测试程序
```

更详细的代码请参考[链接](https://github.com/chatopera/py-clause/blob/master/tests/tst-demo.py)。

## API 接口详细介绍

参考[链接](https://github.com/chatopera/py-clause/wiki)。

## 开源许可协议

Copyright (2019) <a href="https://www.chatopera.com/" target="_blank">北京华夏春松科技有限公司</a>

[Apache License Version 2.0](https://github.com/chatopera/clause/blob/master/LICENSE)

[![chatoper banner][co-banner-image]][co-url]

[co-banner-image]: https://user-images.githubusercontent.com/3538629/42383104-da925942-8168-11e8-8195-868d5fcec170.png
[co-url]: https://www.chatopera.com
