#webapp for study
建站笔记
day1
    搭建python环境，版本3.8.5
    编辑器选用vscode，安装必要的插件，例如code runner
    
    下载pipenv, pip3 install pipenv
    通过pipenv搭建虚拟环境，目前虽然只有一种python版本，但是考虑之后开发， 直接先搭建虚拟环境
        1 在项目根目录下执行下列命令新建虚拟环境
        pipenv install
        2 安装必要的包，例如aiohttp，jinja2，aiomysql
        pipenv install aiohttp jinja2 aiomysql
        3 此时根目录下会出现Pipfile，Pipfile.lock两个文件
        pipfile：python应用程序或库指定开发和执行所需的包
        Pipfile.lock：避免自动升级破坏相互依赖的包和破坏项目依赖树的风险

    构建工作目录
    同步到git


day2
    编写web app骨架
    1 导入logging模块
        基础配置 logging.basicConfig(level=logging.INFO)
        DEBUG：详细的信息,通常只出现在诊断问题上
        INFO：确认一切按预期运行
        WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
        ERROR：更严重的问题,软件没能执行一些功能
        CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
    
    2 通过async def将index标记成一个coroutine（协程），接受一个request实例为唯一参数，翻回一个response实例

    3 创建一个application实例，并用特定的http方法和路径注册请求处理程序

    4 通过run_app()调用运行程序

