import time

print('欢迎使用文件扩展名查询器！作者:b站system32ovo')
print('\u001b[32m1.0版本已收录100种后缀名\u001b[0m')
time.sleep(1)
while True:
    a = input('请输入你要查询的扩展名(不带.)：')

    if a == 'txt':
        print('.txt(文本文件)：包含纯文本，可以用任何文本编辑器打开和编辑。')

    elif a == 'docx' or a == 'doc':
        print('.docx/.doc（Word 文档）：Microsoft Word 文档文件，可包含文本、图像、表格、图表等元素')

    elif a == 'pdf':
        print('.pdf(PDF 文件)：Adobe Portable Document Format 文件，可以跨平台保留格式和布局的文档格式。')

    elif a == 'pptx' or a == 'ppt':
        print('.pptx/.ppt(PowerPoint 文档)：Microsoft PowerPoint 演示文稿文件，可以包含幻灯片、文字、图像、音频或视频等多媒体元素。')

    elif a == 'xlsx' or a == 'xls':
        print('.xlsx/.xls(Excel 表格)：Microsoft Excel 电子表格文件，可以包含数据、图表、公式等信息。')

    elif a == 'jpg' or a == 'jpeg':
        print('.jpg/.jpeg （JPEG 图像）：一种常见的图像格式，通常用于存储照片和其他图片。')

    elif a == 'png':
        print('.png (PNG 图像)：一种支持透明背景的图像格式，通常用于图标、徽标等图像设计。')

    elif a == 'mp3':
        print('.mp3 （MP3 音频）：一种常用的音频格式，通常用于存储音乐和其他音频文件。')

    elif a == 'mp4':
        print('.mp4 （MP4 视频）：一种常用的视频格式，通常用于存储电影、视频剪辑等多媒体文件。')

    elif a == 'c':
        print('.c （C语言源代码文件）：包含了 C 语言的代码，需要编译器执行以生成可执行文件。')

    elif a == 'cpp':
        print('.cpp （C++ 源代码文件）：包含了 C++ 语言的代码，需要编译器执行以生成可执行文件。')

    elif a == 'h':
        print('.h （头文件）：包含了 C/C++ 程序中定义的各种函数、宏定义和变量等声明。')

    elif a == 'java':
        print('.java （Java 源代码文件）：包含了 Java 代码，需要编译器编译后执行。')

    elif a == 'py':
        print('.py （Python 源代码文件）：包含了 Python 代码，可以通过解释器直接执行。')

    elif a == 'html':
        print('.html （HTML 文件）：包含了网页的标记语言，可以通过浏览器进行渲染。')

    elif a == 'css':
        print('.css （CSS 文件）：包含了网页的样式表，用于设置网页元素的样式。')

    elif a == 'js':
        print('.js （JavaScript 文件）：包含了网页的 JavaScript 代码，用于实现网页的交互效果。')

    elif a == 'json':
        print('.json （JSON 文件）：一种轻量级的数据交换格式，可以存储结构化数据。')

    elif a == 'xml':
        print('.xml （XML 文件）：一种类似于 HTML 的标记语言，用于描述和存储数据。')

    elif a == 'php':
        print('.php(PHP 脚本程序)扩展名的文件包含PHP代码，通常通过 Web 服务器来解释和运行，可以用于处理表单数据、访问数据库、生成动态内容等任务。')

    elif a == 'rb':
        print('.rb：Ruby 语言源代码文件，需要解释器执行。')

    elif a == 'go':
        print('go：Go 语言源代码文件，需要编译器执行。')

    elif a == 'swelift':
        print('.swelift：Swelift 语言源代码文件，需要编译器执行。')

    elif a == 'gelif':
        print('.gelif: 一种常见的图像文件格式，用于将静态图像以及简单的动画效果压缩和展示在互联网上。')

    elif a == 'pyw':
        print('.pyw 是 Python 的文件扩展名，用于在 Windows 平台上开发 GUI 应用程序。')

    elif a == 'pyc':
        print('.pyc 是 Python 的字节码文件扩展名，用于将 .py 文件编译成中间形式的字节码，并在下一次执行同样的代码时提高程序的执行速度。')

    elif a == 'jar':
        print('.jar(Java 归档文件)一种用于打包和分发 Java 类、资源文件和元数据的压缩文件格式，通常被用于将一个完整的 Java 应用程序或库打包为一个单独的可执行文件。')

    elif a == 'zip' or a == 'rar' or a == '7z' or a == 'tar':
        print('一种文件压缩格式的扩展名')

    elif a == 'exe':
        print('Windows 可执行文件的扩展名')

    elif a == 'dll':
        print('Windows 动态链接库文件的扩展名')

    elif a == 'app':
        print('MacOS 程序文件的扩展名')

    elif a == 'ipa':
        print('iOS 应用程序文件的扩展名')

    elif a == 'apk':
        print('Android 安装包文件的扩展名')

    elif a == 'deb':
        print('Debian/Ubuntu Linux 发行版软件包文件的扩展名')

    elif a == 'rpm':
        print('Red Hat/Fedora/CentOS Linux 发行版软件包文件的扩展名。')

    elif a == 'avi':
        print('一种音视频压缩格式的文件扩展名')

    elif a == 'mov':
        print('一种常见的音视频文件扩展名')

    elif a == 'wav':
        print('一种无损音频文件格式的扩展名')

    elif a == 'wma':
        print('.wma（Windows 媒体音频）是一种音频文件格式的扩展名')

    elif a == 'm4a':
        print('.m4a（MPEG-4 音频）是一种音频文件格式的扩展名')

    elif a == 'ogg':
        print('.ogg（Ogg Vorbis）是一种音频文件格式的扩展名')

    elif a == 'do':
        print('.do（Stata 批处理命令）一种数据文件格式的扩展名')

    elif a == 'webp':
        print('.webp（WebP 图像）是一种图片文件格式的扩展名')

    elif a == 'svg':
        print('.svg（可缩放矢量图形）用于创建可缩放、可交互的矢量图形和动画等。')

    elif a == 'url':
        print('.url（统一资源定位符）用于链接到特定的网页或 Web 应用。')

    elif a == 'ani':
        print('.ani（动画）一种动画文件的扩展名')

    elif a == 'cur':
        print('.cur 一种光标文件的扩展名')

    elif a == 'ini':
        print('.ini 是一种初始化文件的扩展名')

    elif a == 'inf':
        print('.inf 是一种安装信息文件的扩展名')

    elif a == 'reg':
        print('.reg 是一种注册表文件的扩展名')

    elif a == 'bat':
        print('.bat 是一种批处理文件的扩展名')

    elif a == 'cmd':
        print('.cmd 是一种Windows操作系统命令文件的扩展名')

    elif a == 'sh':
        print('.sh 是一种linux/unix Shell脚本文件的扩展名')

    elif a == 'iso':
        print('.iso 是一种光盘镜像文件的扩展名')

    elif a == 'img':
        print('''1.img 是一种磁盘映像文件扩展名，全称是 Image（镜像）文件。
        2.img文件 软盘映像文件的扩展名''')

    elif a == 'vhd':
        print('.vhd 是一种虚拟硬盘文件格式，全称是 Virtual Hard Disk（虚拟硬盘）')

    elif a == 'vhdx':
        print('.vhdx 是虚拟硬盘文件的一种格式，全称是 Virtual Hard Disk Extended（虚拟硬盘扩展）')

    elif a == 'hdd':
        print('.hdd 文件是一种虚拟硬盘文件格式')

    elif a == 'vmdk':
        print('.vmdk 是一种虚拟硬盘文件格式,该格式是 VMWare 虚拟机软件的专有格式')

    elif a == 'dmg':
        print('.dmg 文件是苹果公司Mac OS系统中的一种磁盘映像文件格式')

    elif a == 'pkg':
        print('.pkg 是 macOS 系统中的一个安装包格式')

    elif a == 'vmx':
        print('.vmx 是 VMware 虚拟机软件中虚拟机配置文件的文件名扩展名')

    elif a == 'vmsd':
        print('.vmsd 是 VMware 虚拟机软件中虚拟机快照描述文件的文件名扩展名')

    elif a == 'plist':
        print('.plist 是 macOS 系统中的一种属性列表文件格式')

    elif a == 'log':
        print('.log 是计算机系统中常见的日志文件格式')

    elif a == 'lnk':
        print('.lnk 是 Windows 操作系统中的一种快捷方式文件格式')

    elif a == 'vbs':
        print('.vbs 是 Windows 操作系统中的一种脚本文件格式，用于编写和运行 Visual Basic Script（VBScript）脚本程序。')

    elif a == 'icns':
        print('.icns 是Mac OS操作系统中常用的一种图标文件格式')

    elif a == 'ico':
        print('.ico 是 Windows 操作系统中常用的一种图标文件格式')

    elif a == 'yml':
        print('.yml 是一种轻量级的数据序列化格式，通常用于配置文件、数据交换和持久化等应用。它的全称为 YAML（Yet Another Markup Language）')

    elif a == 'lock':
        print('.lock 文件通常是一种用于管理软件依赖关系的文件。')

    elif a == 'dat':
        print('.dat 文件通常是指一种数据文件，它包含着特定的数据或信息，以供应用程序或系统使用。')

    elif a == 'mca':
        print('.mca 文件是 Minecraft（我的世界）游戏中的一种区域文件格式，用于存储游戏世界中的方块数据。')

    elif a == 'nbt':
        print('.nbt 文件是 Minecraft（我的世界）游戏中的一种数据格式，用于存储游戏世界中各种实体和方块的数据。')

    elif a == 'properties':
        print('.properties 文件是一种常见的配置文件格式，通常用于将应用程序或系统的各种设置和参数保存为文本形式。')

    elif a == 'conf':
        print('.conf 文件（或称为配置文件）是一种常见的文本文件格式，用于存储应用程序或系统的各种设置和配置。')

    elif a == 'dylib':
        print('.dylib 是 macOS 系统中动态链接库（Dynamic Link Library）的文件扩展名。')

    elif a == 'gz':
        print('.gz 是一种常见的文件压缩格式，又称为 Gzip 压缩格式。')

    elif a == 'deny':
        print('.deny 文件是 Linux 系统中的一种权限控制文件，用于限制用户对某些系统资源或命令的访问和使用。')

    elif a == 'lzma':
        print('.lzma 是一种数据压缩格式，通过应用 LZMA （Lempel–Ziv–Markov chain algorithm）算法，将文件数据压缩成更小的体积，以便于传输、存储和备份。')

    elif a == 'qcow2':
        print('qcow2（QEMU Copy On Write version 2）是 QEMU （Quick EMUlator）虚拟机系统中的一种虚拟磁盘映像格式，用于存储虚拟硬件设备的数据和操作系统的镜像文件。')

    elif a == 'vdi':
        print('.vdi 是 Oracle VirtualBox 虚拟机软件中使用的一种虚拟磁盘文件扩展名。')

    elif a == 'midi':
        print('.midi（Musical Instrument Digital Interface）是一种数字音频文件格式，也称为MIDI文件。')

    elif a == 'mid':
        print('.mid 是一种数字音频文件格式，也称为 MIDI 文件（Musical Instrument Digital Interface）')

    elif a == 'com':
        print('.com 是一个文件名扩展名，通常表示 DOS 或 Windows 操作系统中的可执行文件。')

    elif a == 'rm':
        print('rm 是一种数字音频/视频文件格式，通常指 RealMedia 文件（RealPlayer Media）。')

    elif a == 'ra':
        print('.ra 文件是一种数字音频文件格式，由 RealNetworks 公司开发')

    elif a == 'rv':
        print('.rv 文件是一种数字音频/视频文件格式，通常指 RealVideo 文件（RealPlayer Video）。')

    elif a == 'ram':
        print('ram 文件是一种基于文本的文件格式，通常用于存储 RealAudio 和 RealVideo 的音频/视频流的地址。')

    elif a == 'sparseimage':
        print('.sparseimage 是Mac OS上的一种磁盘映像文件格式。')

    elif a == 'sb':
        print('.sb 文件是基于 Scratch 编程语言的项目文件格式。')

    elif a == 'sb2':
        print('.sb2 是 Scratch 2.0 编程语言的项目文件格式。')

    elif a == 'sb3':
        print('sb3 是 Scratch 3.0 编程语言的项目文件格式。')

    elif a == 'ai':
        print('.ai 是 Adobe Illustrator 软件的文件后缀名。')

    elif a == 'mxf':
        print('.mxf (Material Exchange Format) 是一种专业的数字视频和音频文件格式')

    else:
        print("\u001b[31m你输入的扩展名可能不存在或者未收录！\u001b[0m")