from distutils.dir_util import copy_tree

def copy(src, dst, book):
    """ Create Queue of items to copy and launch taks for each items"""

    sUrl = str(src.joinpath(book['author']).joinpath(book['title']))
    dUrl = str(dst.joinpath(book['author']).joinpath(book['title']))
    print(sUrl, " to ", dUrl)
    copy_tree(sUrl, dUrl)

