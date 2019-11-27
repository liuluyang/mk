


# import file_server
# import docs
import os

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(root_path)
from file_server import app


if __name__ == '__main__':
    app.run('0.0.0.0')
    pass
