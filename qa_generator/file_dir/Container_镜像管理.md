# 镜像管理

<!-- TOC -->

- [镜像管理](#镜像管理)
    - [docker镜像管理](#docker镜像管理)
        - [登录到镜像仓库](#登录到镜像仓库)
        - [从镜像仓库退出登录](#从镜像仓库退出登录)
        - [从镜像仓库拉取镜像](#从镜像仓库拉取镜像)
        - [删除镜像](#删除镜像)
        - [加载镜像](#加载镜像)
        - [列出镜像](#列出镜像)
        - [检视镜像](#检视镜像)
        - [双向认证](#双向认证)
    - [embedded镜像管理](#embedded镜像管理)
        - [加载镜像](#加载镜像-1)
        - [列出镜像](#列出镜像-1)
        - [检视镜像](#检视镜像-1)
        - [删除镜像](#删除镜像-1)

<!-- /TOC -->


## docker镜像管理

### 登录到镜像仓库

#### 描述

isula login命令用于登录到镜像仓库。登录成功后可以使用isula pull命令从该镜像仓库拉取镜像。如果镜像仓库不需要密码，则拉取镜像前不需要执行该命令。

#### 用法

```
isula login [OPTIONS] SERVER
```

#### 参数

login命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表1 表1-20 login命令参数列表" 。

#### 示例

```
$ isula login -u abc my.csp-edge.com:5000

Login Succeeded
```

### 从镜像仓库退出登录

#### 描述

isula logout命令用于从镜像仓库退出登录。退出登录成功后再执行isula pull命令从该镜像仓库拉取镜像会因为未认证而拉取失败。

#### 用法

```
isula logout SERVER
```

#### 参数

logout命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表2 logout命令参数列表"。

#### 示例

```
$ isula logout my.csp-edge.com:5000
Logout Succeeded
```

### 从镜像仓库拉取镜像

#### 描述

从镜像仓库拉取镜像到本地。

#### 用法

```
isula pull [OPTIONS] NAME[:TAG]
```

#### 参数

login命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表3 pull命令参数列表"。

#### 示例

```
$ isula pull localhost:5000/official/busybox
Image "localhost:5000/official/busybox" pulling
Image "localhost:5000/official/busybox@sha256:bf510723d2cd2d4e3f5ce7e93bf1e52c8fd76831995ac3bd3f90ecc866643aff" pulled
```

### 删除镜像

#### 描述

删除一个或多个镜像。

#### 用法

```
isula rmi [OPTIONS] IMAGE [IMAGE...]
```

#### 参数

rmi命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表4 rmi命令参数列表"。

#### 示例

```
$ isula rmi rnd-dockerhub.huawei.com/official/busybox
Image "rnd-dockerhub.huawei.com/official/busybox" removed
```

### 添加镜像标签

#### 描述

tag命令用于添加镜像标签

#### 用法

```
isula tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

#### 参数

tag命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表8 tag命令参数列表"。

#### 示例

```
$ isula tag busybox:latest test:latest
```

### 加载镜像

#### 描述

从一个tar包加载镜像。该tar包必须是使用docker save命令导出的tar包或格式一致的tar包。

#### 用法

```
isula load [OPTIONS]
```

#### 参数

load命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表5 load命令参数列表"。

#### 示例

```
$ isula load -i busybox.tar
Load image from "/root/busybox.tar" success
```

### 列出镜像

#### 描述

列出当前环境中所有镜像。

#### 用法

```
isula images [OPTIONS]
```

#### 参数

images命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表6 images命令参数列表"。

#### 示例

```
$ isula images
REPOSITORY                                   TAG        IMAGE ID             CREATED              SIZE
busybox                                      latest     beae173ccac6         2021-12-31 03:19:41  1.184MB
```

### 检视镜像

#### 描述

返回该镜像的配置信息。可以使用-f参数过滤出需要的信息。

#### 用法

```
isula inspect [options] CONTAINER|IMAGE [CONTAINER|IMAGE...]
```

#### 参数

inspect命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表7 inspect命令参数列表"。

#### 示例

```
$ isula inspect -f "{{json .image.id}}" rnd-dockerhub.huawei.com/official/busybox
"e4db68de4ff27c2adfea0c54bbb73a61a42f5b667c326de4d7d5b19ab71c6a3b"
```

### 双向认证

#### 描述

开启该功能后isulad和镜像仓库之间的通信采用https通信，isulad和镜像仓库都会验证对方的合法性。

#### 用法

要支持该功能，需要镜像仓库支持该功能，同时isulad也需要做相应的配置：

1.  修改isulad的配置\(默认路径/etc/isulad/daemon.json\)，将配置里的use-decrypted-key项配置为false。
2.  需要将相关的证书放置到/etc/isulad/certs.d目录下对应的镜像仓库命名的文件夹下，证书具体的生成方法见docker的官方链接：
    -   [https://docs.docker.com/engine/security/certificates/](https://docs.docker.com/engine/security/certificates/)
    -   [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)


1.  执行systemctl restart isulad重启isulad。

#### 参数

可以在/etc/isulad/daemon.json中配置参数，也可以在启动isulad时携带参数：

```
isulad --use-decrypted-key=false
```

#### 示例

配置use-decrypted-key参数为false

```
$ cat /etc/isulad/daemon.json
{
    "group": "isulad",
    "graph": "/var/lib/isulad",
    "state": "/var/run/isulad",
    "engine": "lcr",
    "log-level": "ERROR",
    "pidfile": "/var/run/isulad.pid",
    "log-opts": {
        "log-file-mode": "0600",
        "log-path": "/var/lib/isulad",
        "max-file": "1",
        "max-size": "30KB"
    },
    "log-driver": "stdout",
    "hook-spec": "/etc/default/isulad/hooks/default.json",
    "start-timeout": "2m",
    "storage-driver": "overlay2",
    "storage-opts": [
        "overlay2.override_kernel_check=true"
    ],
    "registry-mirrors": [
        "docker.io"
    ],
    "insecure-registries": [
        "rnd-dockerhub.huawei.com"
    ],
    "pod-sandbox-image": "",
    "image-opt-timeout": "5m",
    "native.umask": "secure",
    "network-plugin": "",
    "cni-bin-dir": "",
    "cni-conf-dir": "",
    "image-layer-check": false,
    "use-decrypted-key": false,
    "insecure-skip-verify-enforce": false
}
```

将证书放到对应的目录下

```
$ pwd
/etc/isulad/certs.d/my.csp-edge.com:5000
$ ls
ca.crt  tls.cert  tls.key
```

重启isulad

```
$ systemctl restart isulad
```

执行pull命令从仓库下载镜像

```
$ isula pull my.csp-edge.com:5000/busybox
Image "my.csp-edge.com:5000/busybox" pulling
Image "my.csp-edge.com:5000/busybox@sha256:f1bdc62115dbfe8f54e52e19795ee34b4473babdeb9bc4f83045d85c7b2ad5c0" pulled
```

### 导入rootfs

#### 描述

把包含了一个rootfs的tar包导入为镜像，该tar包一般是之前使用export命令导出的，也可以是格式兼容的包含rootfs的tar包。目前支持
格式(.tar, .tar.gz, .tgz, .bzip, .tar.xz, .txz)，请勿使用其他格式的tar包进行导入。

#### 用法

```
isula import file REPOSITORY[:TAG]
```
导入成功后打印的字符串是导入的rootfs生成的镜像id

#### 参数

import命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表9 import命令参数列表"。

#### 示例

```
$ isula import busybox.tar test
sha256:441851e38dad32478e6609a81fac93ca082b64b366643bafb7a8ba398301839d
$ isula images
REPOSITORY      TAG        IMAGE ID            CREATED                  SIZE
test            latest     441851e38dad        2020-09-01 11:14:35      1.168 MB
```

### 导出rootfs

#### 描述

把一个容器的rootfs文件系统内容导出成tar包，导出的rootfs的tar包可以在后面使用import功能重新导入成镜像。

#### 用法

```
isula export [OPTIONS] [ID|NAME]
```

#### 参数

export命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表10 export命令参数列表"。

#### 示例

```
$ isula run -tid --name container_test test sh
d7e601c2ef3eb8d378276d2b42f9e58a2f36763539d3bfcaf3a0a77dc668064b
$ isula export -o rootfs.tar d7e601c
$ ls
rootfs.tar
```


## embedded镜像管理

### 加载镜像

#### 描述

根据embedded镜像的manifest加载镜像。注意--type的值必须填写embedded。

#### 用法

```
isula load [OPTIONS] --input=FILE --type=TYPE
```

#### 参数

load命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表5 load命令参数列表"。

#### 示例

```
$ isula load -i test.manifest --type embedded
Load image from "/root/work/bugfix/tmp/ci_testcase_data/embedded/img/test.manifest" success
```

### 列出镜像

#### 描述

列出当前环境中所有镜像。

#### 用法

```
isula images [OPTIONS]
```

#### 参数

images命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表6 images命令参数列表"。

#### 示例

```
$ isula images
REPOSITORY                                   TAG        IMAGE ID             CREATED              SIZE
busybox                                      latest     beae173ccac6         2021-12-31 03:19:41  1.184MB
```

### 检视镜像

#### 描述

返回该镜像的配置信息。可以使用-f参数过滤出需要的信息。

#### 用法

```
isula inspect [options] CONTAINER|IMAGE [CONTAINER|IMAGE...]
```

#### 参数

inspect命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表7 inspect命令参数列表"。

#### 示例

```
$ isula inspect -f "{{json .created}}" test:v1
"2018-03-01T15:55:44.322987811Z"
```

### 删除镜像

#### 描述

删除一个或多个镜像。

#### 用法

```
isula rmi [OPTIONS] IMAGE [IMAGE...]
```

#### 参数

rmi命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表4 rmi命令参数列表"。

#### 示例

```
$ isula rmi test:v1
Image "test:v1" removed
```

### 添加名称

#### 描述

给镜像添加一个名称。

#### 用法

```
isula tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

#### 参数

tag命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表8 tag命令参数列表"。

#### 示例

```
$ isula tag test:v1 test:v2
```

### 导入镜像

#### 描述

将tar格式的rootfs导入生成一个新的镜像，该tar包必须是通过export命令导出的tar包。

#### 用法

```
isula export [command options] [ID|NAME]
```

#### 参数

export命令支持参数请参见"附录 > 命令行参数说明" 章节的 "表9 export命令参数列表"。

#### 示例

```
$ isula export -o test.tar containername
```
