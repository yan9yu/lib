#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File Module provides file-relevant functions
    -
"""

import os
import sys
import shutil

try:
    import cPickle as pickle
except:
    import pickle

try:
    import simplejson as json
except:
    import json

import conv
import hash


def isExist(path):
    """
    Check whether a path is exist
        Input: path
        Output: True/False
    """
    return os.path.exists(path)


def isFile(path):
    """
    Check whether a path is a file or not
        Input: path
        Output: True/False
    """
    return os.path.isfile(path)


def isDir(path):
    """
    Check whether a path is directory
        Input: path
        Output: True/False
    """
    return os.path.isdir(path)


def mkDir(path):
    """
    Create a new directory
        Input: path
        Output:
    """
    if isExist(path):
        os.mkdir(path)


def mv(src_path, dest_path):
    """
    Move src to dest
        Input: src_path, dest_path
        Output:
    """
    return shutil.move(src_path, dest_path)


def rmDir(path):
    """
    Delete a directory
        Input: path
        Output: True/False
    """
    return os.rmdir(path)


def rm(path):
    """
    Delete a file
        Input: path
        Output: True/False
    """
    if isExist(path):
        return os.remove(path)


def touch(path):
    """
    Create a empty file
        Input: path
        Output:
    """
    if not isExist(path):
        open(path, "a").close()


def getFileList(path):
    """
    Return a file list of a directory
        Input: path
        Output: file list
    """
    return sorted([(path + item, item) for item in os.listdir(path) if isFile(path + item)])


def getDirList(path):
    """
    Return a directory list of a directory
        Input: path
        Output: directory list
    """
    return sorted([(path + item, item) for item in os.listdir(path) if isDir(path + item)])


def eptDir(path):
    """
    Delete all files in a directory and keep the directory empty
        Input: path
        Output: file list
    """
    files = getFileList(path)
    for file in files:
        filePath, filename = file
        print "Now deleting:\t%s " % (filePath)
        if isDir(filePath):
            eptDir(filePath)
        else:
            rm(filePath)


def read(path, type=None, quiet=False):
    """
    Read muti-types of files
        Input: path, type=["csv", "txt", "dat", "json", "pck"]
        Output: data
    """
    if type == None or type not in ["csv", "txt", "dat", "json", "pck"]:
        if not quiet:
            print "Use default format: dat"
        type = "dat"

    if isExist(path):
        if type == "json":
            with open(path, mode="r") as fp:
                data = fp.read()
                data = data.replace("\n", "")
                data = json.loads(data)
        if type == "txt" or type == "dat" or type == "csv":
            with open(path, mode="r") as fp:
                data = fp.readlines()
        if type == "pck":
            with open(path, mode="r") as fp:
                data = pickle.load(fp)

        if not quiet:
            filesize = conv.convertBytes(os.path.getsize(path))
            print "Read successfully: %s(%s)!" % (path, filesize)
        return data
    else:
        out_str = "ERROR: %s not exist!" % (path)
        return None


def readByYield(path):
    """
    Read dat/csv/txt files using generator yield
        Input: path, type=["csv", "txt", "dat"]
        Output: data
    """
    with open(path, mode="r") as fp:
        line = fp.readline()
        while line:
            yield line
            line = fp.readline()


def save(data, path, type=None, quiet=False):
    """
    Save muti-types of files
        Input: path, type=["csv", "txt", "dat", "json", "pck"]
        Output: data
    """

    if type == None or type not in ["csv", "txt", "dat", "json", "pck"]:
        print "Use default format: dat"
        type = "dat"

    if type == "csv" or type == "dat" or type == "txt":
        with open(path, mode="w") as fp:
            fp.write(str(data))
            fp.flush()
    if type == "json":
        with open(path, mode="w") as fp:
            json.dump(data, fp, indent=3, encoding="utf-8")
    if type == "pck":
        with open(path, mode="w") as fp:
            pickle.dump(data, fp)
    if not quiet:
        filesize = conv.convertBytes(os.path.getsize(path))
        print "Save successfully: %s(%s)!" % (path, filesize)


def flush(data, file):
    """
    Save List objects to txt file
        Input: path
        Output: data
    """
    try:
        with open(file, "w") as fp:
            length = len(data)
            for ii in xrange(0, length):
                out_str = ""
                item = data[ii]
                for jj in xrange(0, len(item)):
                    out_str += str(item[jj]) + "\t"
                fp.write(out_str.strip() + "\n")
    except Exception, e:
        print e.message


def getFileSize(path):
    """
    Get file size in int
        Input: path
        Output: file size in int
    """
    if isExist(path):
        return int(os.path.getsize(path))
    else:
        return -1


def getFileStatus(path):
    """
    Get file MD5 code and save to *.status file
        Input: path
        Output: MD5 checksum
    """
    md5 = hash.fileMD5(path)
    save(md5, path + ".status")
    print "Save %s status: %s" % (path, md5)


def fileSplit(path):
    """
    Split large files into small pieces using *nix command: Split
    """
    wc_comm = "more %s | wc -l " % (path)
    lines = os.popen(wc_comm).read()
    fileCount = lines / 1000
    comm = "split -l %s -d %s %s_" % (fileCount, path, path)
    os.system(comm)


def scp(host, user, passwd, port, src, dest):
    try:
        import paramiko
    except Exception, e:
        print e.message
    import datetime

    try:
        trans = paramiko.Transport((host, port))
        trans.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)
        print "scp file start %s" % (datetime.datetime.now())
        for root, dirs, files in os.walk(src):
            for file in files:
                src_file = os.path.join(root, file)
                a = src_file.replace(src, "")
                dest_file = os.path.join(dest, a)
                try:
                    sftp.put(src_file, dest_file)
                except Exception, e:
                    sftp.mkdir(os.path.split(dest)[0])
                    sftp.put(src_file, dest_file)
                print "scp %s from src to dest %s" % (src_file, dest_file)
            for name in dirs:
                src_path = os.path.join(root, name)
                a = src_path.replace(src, "")
                dest_path = os.path.join(dest_path, a)
                try:
                    sftp.mkdir(dest_path)
                    print "mkdir path: %s" % (dest_path)
                except Exception, e:
                    print e
        print "scp files successfully %s" % (datetime.datetime.now())
        t.close()
    except Exception, e:
        print e


def zip(src, dst):
    pass


def unzip(src, dst):
    """
    Unzip file to dst
        Input: src, dst
        Output: extracted files
    """

    import zipfile as zf

    z = zf.ZipFile(src, "r")
    if len(z.namelist()) == 1:
        for f in z.namelist():
            data = z.read(f)
            save(data, dst)
            print "unzip %s successfully!" % (f)
    else:
        count = 1
        for f in z.namelist():
            path = dst + "." + count
            count += 1
            data = z.read(f)
            save(data, path)
        print "unzip %s files successfully!" % (count)



