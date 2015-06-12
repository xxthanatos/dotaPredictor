import ConfigParser
import os

repo_cfg = ConfigParser.ConfigParser()
cfg_file = os.path.abspath(''.join([os.path.dirname(os.path.realpath(__file__)), "/repo_cfg.ini"]))
repo_cfg.read(cfg_file)

if __name__ == '__main__':
    for section in repo_cfg.sections():
        print (section)
        for option in repo_cfg.options(section):
            print (''.join([" Option:",  option, "     Value:", repo_cfg.get(section, option)]))
