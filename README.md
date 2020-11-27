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
    