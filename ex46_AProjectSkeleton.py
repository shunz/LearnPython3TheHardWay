# Exercise 46: A Project Skeleton

"""学习建立一个项目「骨架」目录，具备让项目运行起来的所有基本内容。包含：
 • 项目文件布局
 • 自动测试代码
 • 模块及安装脚本
当新建一个项目时，只要复制该目录，修改目录名，再编辑里边的文件即可
"""


"""用virtualenv创建一个「假的」Python安装环境，使管理不同项目的包版本更容易
 • mkdir ~/.venvs  # 创建一个目录，用来存储所有的虚拟环境
 • virtualenv --system-site-packages ~/.venvs/lpthw  # 执行virtualenv，让它
   包含系统站点包，然后在lpthw目录中创建一个虚拟环境
 • python3 -m venv lpthw  # 用标准库内置的venv模块创建虚拟环境
 • . ~/.venvs/lpthw/bin/activate  # 用source命令激活lpthw虚拟环境(用deactivate
   命令退出)
 • which python/python3 查看python在虚拟环境中的安装目录
 • pip3 install nose  # 安装nose测试框架
"""


"""创建骨架项目目录
 • mkdir projects && cd projects
 • mkdir skeleton && cd skeleton
 • mkdir bin NAME tests docs  # 同时创建多个目录
 • touch NAME/__init__.py
 • touch tests/__init__.py
 • vi setup.py  # 内容参考书
 • vi tests/NAME_tests.py  # 内容参考书
 • python3 -m "nose"  # 测试配置，如果有报错，就是上述内容有误
"""


"""使用骨架
1. 复制骨架目录，把名字改成新项目的名字
2. 将NAME目录更名为项目的名字，或者想给根模块起的名字
3. 编辑setup.py，让它包含新项目的相关信息
4. 重命名tests/NAME_tests.py，把NAME换成模块的名字
5. 使用nosetests检查有无错误
6. 开始写代码
"""
