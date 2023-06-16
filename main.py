import time
import random

# 随机生成一个文件 保持仓库处于活跃
open('dist-version','w+').write(time.strftime("%Y-%m-%d",time.localtime(time.time()))+'-'+''.join(random.sample('abcdefghigklmnopqrstuvwxyz1234567890',20)))
