## linux下使用Git

- yum install git : 安装git
- git init:初始化创建本地仓库
- git --version :查看git版本
- git add :项目放入本地的缓存区
- git commit -m '描述':将项目放入本地的仓库中,并附带描述
- git status:查看文件状态
- git log:查看日志
- git relog:当使用reset回到之前的版本时,可以使用该命令查看该版本之后的版本
- git reset --hard 标识码:可以回到标识码所标记的版本
- git checkout -- (文件名) :撤销缓冲区中的项目,需要修改之后重新提交到缓冲区
- git clone url:从服务器将项目拷贝到本地
- git push origin master:将本地仓库中的文件提交到服务器的master的分支上
- git pull:将服务器中的项目拉下来
- git remote add origin url:将本地仓库与远程仓库对接
- git push -u origin master:对接之后将项目提交到远程仓库
- git branch 分支名:在本地创建分支
- git branch:查看当前所处分支
- git checkout 分支名:切换分支
- git merge 分支名:将分支合并入master分支
- git push origin master:将项目提交到master分支
- git rm 文件名:删除文件
- git branch -D 分支名:删除本地某个分支
- git push origin :分支名:删除远程分支

## Git日常工作流程

- 从远端拉取项目(前提是本地无该项目):

1. git clone <url>    #从远端克隆项目
2. cd <dir>    #克隆到本地后,进入项目
3. git branch <name>   # 创建分支,一般修改项目不要在master主分支中修改
4. git branch #查看有哪些分支
5. git checkout <name> #切换到指定的分支,默认所处分支是master主分支
6. git add . # 切换成功后,在非主分支中,将修改的项目提交到缓冲区,<.>代表提交所有文件,也可以输入文件名提交指定的文件,文件不能为空,否则无法提交
7. git rm <filename> # 删除文件, 如果是文件夹需要输入git rm -r 文件夹进行遍历删除
8. git commit -m '描述' # 将缓冲区的文件提交到本地仓库中并附带描述
9. git push origin <branch> # 将本地仓库的文件提交到远程仓库的分支,哪个分支由自己指定

- 将本地文件上传到远端(前提是本地有文件):

1. cd 文件夹 # 进入文件夹
2. git init : # 初始化本地仓库,必须保证该文件夹中没有.git文件
3. git add . # 将文件中的内容提交到缓冲区
4. git commit -m '11' # 将缓冲区的文件提交到本地仓库
5. git remote add origin <url> # 将本地仓库与远程仓库对接
6. git pull --rebase orgin master #
7. git push -u origin master #将本地仓库的文件传到远端仓库,第一次传递时需要加上-u,以后就不需要了.一旦进行了仓库对接,直接.git在,那么该连接就是一直存在的,不会消失.

