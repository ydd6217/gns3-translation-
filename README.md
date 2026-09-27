gns3模拟器，界面纯英文，fedora使用不方便，利用chatgpt进行的翻译，可以使用translate_basic.py文件进行相关配置。

GNS3 中文化（Fedora）
项目说明

本项目用于 Fedora Linux 下 GNS3 GUI 中文化。

GNS3 基于 Qt 框架，使用 Qt Linguist 翻译机制：

.ts：Qt 翻译源文件

.qm：Qt 编译后的语言文件

通过生成中文翻译文件，并在 GNS3 启动时加载，实现界面中文显示。

环境

OS: Fedora Linux

Python: 3.14

GNS3 安装路径:

/usr/lib/python3.14/site-packages/gns3


Qt: Qt6 Linguist

文件结构
gns3-zh/
├── gns3_zh_CN.ts          # 中文翻译源文件
├── gns3_zh_CN.qm          # Qt 编译语言文件
├── translate_basic.py     # 基础翻译脚本
├── test_translation.py    # Qt 翻译测试
└── README.md

生成翻译文件

安装 Qt 翻译工具：

sudo dnf install qt6-qttools qt6-linguist


生成 TS 文件：

lupdate-qt6 \
/usr/lib/python3.14/site-packages/gns3 \
-recursive \
-source-language en \
-target-language zh_CN \
-ts gns3_zh_CN.ts

编译 QM 文件
lrelease-qt6 gns3_zh_CN.ts


生成：

gns3_zh_CN.qm

安装中文语言文件

创建目录：

mkdir -p ~/.local/share/gns3/translations


复制：

cp gns3_zh_CN.qm \
~/.local/share/gns3/translations/


最终路径：

~/.local/share/gns3/translations/gns3_zh_CN.qm

GNS3 加载中文翻译

修改：

/usr/lib/python3.14/site-packages/gns3/main.py


在创建应用程序后、创建窗口前加入：

global app
    app = Application(sys.argv) ## 在这下面加入

    translator = QtCore.QTranslator()
    translation_file = os.path.expanduser(
    "~/.local/share/gns3/translations/gns3_zh_CN.qm"
    )
    if translator.load(translation_file):
        app.installTranslator(translator)
        log.info("Chinese translation loaded: %s", translation_file)
    else:
        log.warning("Chinese translation not found: %s", translation_file)

加载顺序：

Application
    ↓
QTranslator
    ↓
installTranslator()
    ↓
MainWindow

启动测试

运行：

gns3


如果加载成功，GNS3 界面显示中文。

更新翻译

修改：

gns3_zh_CN.ts


重新编译：

lrelease-qt6 gns3_zh_CN.ts


替换：

cp gns3_zh_CN.qm \
~/.local/share/gns3/translations/


重新启动 GNS3。

注意事项

GNS3 更新后：

/usr/lib/python3.14/site-packages/gns3/main.py


可能被覆盖，需要重新加入 Translator 加载代码。

建议升级前备份：

cp /usr/lib/python3.14/site-packages/gns3/main.py \
main.py.backup

完成状态

 GNS3 Qt 翻译机制确认

 中文 TS 文件生成

 中文 QM 文件编译

 Qt Translator 测试

 GNS3 启动加载中文

 Fedora 环境运行测试

License

个人学习与技术交流使用。
