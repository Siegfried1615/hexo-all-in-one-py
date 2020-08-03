import os

def all_in_one(title):
    file_name = title
    py_path = os.getcwd().replace('\\', '/')
    os.system("hexo new " + file_name)
    full_path = py_path + "/source/_posts/" + file_name+'.md'
    try:
        os.system("start " "" + full_path)
        print("创建完毕,正在打开...")
        os.system('exit')  # 关闭窗口

    except Exception as e:
        print("出现错误，可能是文件路径不对导致的，请放于博客根目录，与_config.yml同级")


def deploy_posts_clean():
    try:
        os.system("hexo clean && hexo g && hexo d")
        print("上传完毕！")
        os.system('pause')  # 按任意键继续
        os.system('exit')  # 关闭窗口
    except Exception as e:
        print("上传失败，可能是由于没有正确进行配置或文件路径错误")


def deploy_posts():
    try:
        os.system("hexo g && hexo d")
        print("上传完毕！")
        os.system('pause')  # 按任意键继续
    except Exception as e:
        print("上传失败，可能是由于没有正确进行配置或文件路径错误")


def backup_blog():
    try:
        os.system("hexo b")
        print("备份完毕！")
        os.system('pause')  # 按任意键继续
    except Exception as e:
        print("上传失败，可能是由于没有配置hexo-git-backup插件")


if __name__ == '__main__':
    print("1. 新建文章")
    print("2. 推送文章")
    print("3. 备份博客")
    num_1 = input("选择功能: ")
    if num_1 == 1:
        input = input("文章标题: ")
        all_in_one(input)
    elif num_1 == 2:
        print("1. hexo g && hexo d")
        print("2. hexo clean && hexo g && hexo d")
        num_2 = input("选择功能: ")
        if num_2 == 1:
            deploy_posts()
        elif num_2 == 2:
            deploy_posts_clean()
        else:
            deploy_posts()
    elif num_1 == 3:
        backup_blog()
    else:
        input = input("文章标题: ")
        all_in_one(input)
